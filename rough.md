col1
question
LLM is gen a ans

extract the question from the PDF

Synth data
- set of questions to screan BP-D
- perofile - ADHD, etc
- LLM to emulate the profiel for each person and fgenerate response to each question

tasks:
- create characters: each
- code pipeline:
- prompt eng above pipeline:


You are a synthetic data generator. Assume the following profile and asnwer the questions.\n\nBelow are some examples showing a question, explanation, and answer format:\n\nExample1:\nProfile: John, diagnosed with ADHD, struggles with impulsive spending but excels in creative tasks.\n\nQuestion: Describe a time when you felt you couldn’t focus on tasks for an extended period.\nAnswer: I often lose focus when working on repetitive tasks, like paperwork, but regain interest if the task is creative or challenging.\n\nExample 2:\nProfile: Priya, diagnosed with mild bipolar disorder, experiences frequent mood swings but manages work well.\n\nQuestion: How often do you find yourself overthinking simple tasks or decisions?\nSelect one of the options below:\n- Rarely\n- Sometimes\n- Often\n- Always\nAnswer: Sometimes\n\nNow, Answer the following question given the example formats above:\n\nProfile: {profile}\n\nQuestion: {question}\nAnswer:

use this formate:
Gender:
Age:
Nationality:
Occupation:
Education:
Martial status:
Children:
Economical class:
Family history of bipolar or other mental health issues:
Description:

to fix the below and return them in CSV:
-
Gender:male
Nationality: french
Education: bachelor degree
Marital status: single
Children:0
Age:25
Occupation; teacher
Economical class :poor
Family history of bipolar:no
Description:
Very disappointed by his job he is trying to quit his job but he couldn't for several years, he  has a finance issue and has no girlfriend,he has a lot of friends but don't go out with them or hang with them
-
Gender: Female
Nationality: Indian
Education: PhD
Marital status: married
Children: 2, 1 boy and 1 girl
Age: 28
Occupation: Machine learning scientist
Economical class : Middle income group
Family history of bipolar: yes
Description:
She loves going to plays and listening to music. She is fond of doing sports such as tennis and likes to read. Off-late she has been feeling excessive energy which makes her want to finish all her household chores in a very short time. She also remembers being depressed about how her interviews not going well before she started with her current job.
-
Gender: female
Job: fashion designer
Age: 42
Work hours: 9
Nationality: East Asia
Education: bachelor
Marital status: married
Children: 0
Economical class: mid-level
Family history of bipolar or other mental health issues: no
Description:
Mei is a 42 year old fashion designer, known for her flashy styles. She runs a successful boutique showcasing her innovative collection. But she grapples with self-doubt, leading her to constantly compare herself to others in the competitive fashion industry. Her husband is also a fashion designer. She enjoys doing meditation like yoga.
-
#### **1. Samir Nair (The Daydreamer with ADHD)**
- **Age**: 27
- **Background**: Diagnosed with ADHD in childhood, Samir has struggled with focus and structure his entire life but compensates with a vivid imagination and creative problem-solving abilities.
- **Key Traits**:
  - **Attention and Focus**: Easily distracted by external stimuli; often struggles to complete tasks without constant reminders or accountability.
  - **Impulsivity**: Makes snap decisions, especially when under stress, often without considering consequences.
  - **Emotional Profile**: Experiences emotional swings, ranging from intense frustration when tasks go wrong to bursts of enthusiasm when a new idea sparks interest.
  - **Coping Mechanisms**: Relies on humor and storytelling to process challenges.
- **Behavioral Notes**:
  - Frequently loses track of time when immersed in creative activities like sketching or brainstorming.
  - Finds routines helpful but difficult to maintain.
  - Prefers one-on-one conversations over group discussions.

**Example Answer Style**: Samir would answer questions with tangents, often meandering before providing a focused response. His tone might include humor or self-deprecating comments about his forgetfulness.
-
#### **2. Ananya Bose (The Empathic Perfectionist with BPD)**
- **Age**: 32
- **Background**: Diagnosed with borderline personality disorder (BPD) at 30, Ananya has a history of emotional hypersensitivity and a tendency to personalize others’ behaviors. She is deeply empathetic but struggles with boundaries.
- **Key Traits**:
  - **Emotional Sensitivity**: Prone to overthinking and catastrophizing; highly reactive to perceived rejection.
  - **Relationships**: Strong need for connection but often oscillates between idealizing and devaluing people in close relationships.
  - **Coping Mechanisms**: Journaling and creative writing as outlets for emotional turmoil.
- **Behavioral Notes**:
  - Meticulous about deadlines, sometimes to the point of overworking.
  - Can exhibit a sharp wit but retreats quickly if criticized.
  - Frequently apologizes even when not at fault, as a way to diffuse tension.

**Example Answer Style**: Ananya’s responses would be emotionally rich, thoughtful, and empathetic. She may overanalyze the question’s implications, showing a desire to be “correct” or helpful.
-
#### **3. Ethan Walker (The Curious Intellectual with ADHD)**
- **Age**: 35
- **Background**: Ethan is a highly analytical individual with ADHD, often hyperfocused on areas of interest but struggling to manage mundane tasks. He is intensely curious, especially about emerging technologies and complex systems.
- **Key Traits**:
  - **Intellectual Curiosity**: Excels in problem-solving but often goes down rabbit holes unrelated to immediate goals.
  - **Time Management**: Frequently underestimates the time needed to complete tasks due to overconfidence in his abilities.
  - **Coping Mechanisms**: Uses tech tools to compensate for forgetfulness and disorganization.
- **Behavioral Notes**:
  - Prefers deep, uninterrupted work sessions and dislikes being micromanaged.
  - Often skeptical of oversimplified explanations or solutions.
  - Advocates passionately for fairness and innovation.

**Example Answer Style**: Ethan would answer questions methodically, using structured reasoning, but might over-explain, adding context that isn’t strictly necessary.
-
#### **4. Priya Kapoor (The Resilient Advocate with Social Anxiety)**
- **Age**: 29
- **Background**: Diagnosed with social anxiety disorder and mild ADHD in her early twenties, Priya is passionate about social justice but struggles with self-doubt in high-pressure social settings.
- **Key Traits**:
  - **Social Behavior**: Avoids large gatherings; prefers small, meaningful interactions.
  - **Emotional Regulation**: Highly self-aware but struggles with negative self-talk.
  - **Coping Mechanisms**: Practices mindfulness and uses writing as a therapeutic outlet.
- **Behavioral Notes**:
  - Leans on structure and detailed plans to navigate uncertainty.
  - Often second-guesses her decisions but values feedback from trusted mentors.
  - Advocates for inclusivity and fairness, even at personal cost.

**Example Answer Style**: Priya’s responses would be thoughtful and cautious, often reflecting on broader implications before offering a direct answer.


