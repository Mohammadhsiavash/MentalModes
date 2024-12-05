import textwrap

import google.generativeai as genai

from IPython.display import Markdown

import os
from dotenv import load_dotenv

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
