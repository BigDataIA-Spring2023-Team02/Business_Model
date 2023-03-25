import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')
model_engine = "text-davinci-002"

def parse_python_code(code):
    # This is a simple implementation that just returns the input code as a string
    return str(code)

def convert_python_javascript(python_code):
    # You will need to develop a parser for this step
    parsed_code = parse_python_code(python_code)
    # You will need to define the prompts for this step
    # Here is an example prompt for generating JavaScript code
    prompt = f"Convert the following Python code to JavaScript: {parsed_code}"
    # Call the OpenAI API to generate JavaScript code
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Extract the generated JavaScript code from the API response
    generated_code = response.choices[0].text
    
    return generated_code

def generate_sql_queries(prom):
    # You will need to define the prompts for this step
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prom +"\n give me a sql query for the following statement i have mentioned",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    sql_query = response.choices[0].text.strip()
    
    return sql_query

def interview_question(job_info):
    # Set OpenAI model and prompt
    # model_engine = "davinci"
    prompt = "Generate interview questions and answers for a data scientist role."
    
    # Create OpenAI API request
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + "\n Give me relevant question that can be asked for the following job description: " + job_info,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract question and answer pairs from OpenAI response
    question_answers = completions.choices[0].text.split("\n")

    return question_answers