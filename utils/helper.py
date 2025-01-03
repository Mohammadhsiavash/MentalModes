import textwrap

import google.generativeai as genai

from IPython.display import Markdown

import os
import json
from dotenv import load_dotenv
import pandas as pd

class GenAIHelper:
    def __init__(self, model_name="gemini-1.5-pro"):
        load_dotenv()
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        print(f'Using Google API key: {self.google_api_key[:4]}...')

        genai.configure(api_key=self.google_api_key)
        self.model_name = model_name

    def set_model(self, model_name: str):
        self.model_name = model_name

    def generate_response(self, prompt: str):
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(prompt)
        return response.text

    def model_list(self):
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

    def to_markdown(self, text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

class PromptHelper:
    def __init__(self, prompts_file):
        """
        Initializes the PromptHelper with the path to the JSON file containing prompts.

        Args:
            prompts_file (str): Path to the JSON file with system prompts.
        """
        if not os.path.exists(prompts_file):
            raise FileNotFoundError(f"Prompts file '{prompts_file}' not found.")
        self.prompts_file = prompts_file
        self.prompts = self._load_prompts_from_file()

    def _load_prompts_from_file(self):
        """Loads prompts from a JSON file and returns them as a dictionary."""
        with open(self.prompts_file, 'r', encoding='utf-8') as f:
            prompts_list = json.load(f)
        # Convert to a dictionary for quick lookup
        prompts_dict = {}
        for item in prompts_list:
            name = item.get("name")
            prompt = item.get("prompt")
            if name and prompt:
                prompts_dict[name] = prompt
            else:
                print(f"Warning: Missing 'name' or 'prompt' in item: {item}")
        return prompts_dict

    def build_prompt(self, system_prompt_name, user_prompt):
        """
        Builds a formatted prompt by retrieving a system prompt by name and appending the user prompt.

        Args:
            system_prompt_name (str): Name of the system prompt to retrieve.
            user_prompt (str): The user's input to append to the system prompt.

        Returns:
            str: The concatenated and formatted prompt.
        """
        system_prompt = self.prompts.get(system_prompt_name)
        if not system_prompt:
            raise ValueError(f"System prompt with name '{system_prompt_name}' not found.")
        # Concatenate system prompt and user prompt
        full_prompt = f"{system_prompt}\n{user_prompt}"
        return full_prompt

# Define the function to process a single row
def process_row(row):
    question = row['question']
    question_type = row['question_type']

    if question_type == "description":
        # For description type
        return f"{question}\nPlease describe your answer.\n"
    elif question_type == "multiple-choice":
        # For multiple-choice type
        options = [row[f"choice_{i}"] for i in range(1, 5) if pd.notna(row[f"choice_{i}"])]
        options_str = "\n".join([f"- {option}" for option in options])
        return f"{question}\nSelect one of the options below:\n{options_str}\n"

def row_to_string(row):
    """
    Convert a row of data into a structured string format.
    """
    return (
        f"Gender: {row['Gender']}\n"
        f"Age: {row['Age']}\n"
        f"Nationality: {row['Nationality']}\n"
        f"Occupation: {row['Occupation']}\n"
        f"Education: {row['Education']}\n"
        f"Marital status: {row['Marital status']}\n"
        f"Children: {row['Children']}\n"
        f"Economical class: {row['Economical class']}\n"
        f"Family history of bipolar or other mental health issues: {row['Family history of bipolar or other mental health issues']}\n"
        f"Description: {row['Description']}\n"
    )