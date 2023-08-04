
# Langchain Repository Setup Guide

## Getting Started

1. **Clone the repository**  
   You can clone the Langchain repository by running the following command in your terminal:
   ```
   git clone https://github.com/username/langchain.git
   ```
   Make sure to replace "username" with the actual username.

2. **Set up a Python virtual environment**  
   It's a good practice to create a virtual environment for your project. To create a virtual environment, run:
   ```
   python3 -m venv venv
   ```
   To activate the virtual environment, run:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

3. **Install the requirements**  
   After you've activated the virtual environment, install the required packages using:
   ```
   pip install -r requirements.txt
   ```

4. **Create a data directory and place the required file in it**  
   Create a directory named "data" and place the "Snake Bite Order set.pdf" file in it. You can do this using the following commands:
   ```
   mkdir data
   cp /path/to/Snake\ Bite\ Order\ set.pdf data/
   ```
   Replace "/path/to/Snake\ Bite\ Order\ set.pdf" with the actual path to the file.

5. **Set up the OpenAI API Key**  
   Create a `.env` file in the root directory of the project and add your OpenAI API Key to it like this:
   ```
   OPENAI_API_KEY=<<your api key>>
   ```
   **Important**: Make sure your `.gitignore` file contains `.env`, otherwise you'll risk committing your API key to GitHub!

## Using SageMaker

To use the project with SageMaker, create a new SageMaker instance and run the following Python code in one of the cells:

```python
from IPython.display import display, Markdown
from agents import create_qa_agent

queries = ["40 year old with CHF, Type II DM brought after he was bit by Krait. Vital signs on arrival are stable. What is the initial assessment I have to do, also list labs to be done.",
    "21 year old with snake bite, patient is not breathing well on examination and has symptoms of paralysis. what are the medications to be given along with the doses?",
    "I'm doing the clotting test, and the blood is not clotting, what should I do",
    "What is the dose of epinephrine for ASV reaction?",
    "How should ASV be administered?"]

index = create_qa_agent('data/Snake Bite Order set.pdf')

for query in queries:

    print(f"\n{query}\n\nResponse:\n")

    response = index.query(query)
    display(Markdown(response))
```
