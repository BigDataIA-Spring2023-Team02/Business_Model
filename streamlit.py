import os
import openai
import streamlit as st
from functions import convert_python_javascript, interview_question, generate_sql_queries

def python_javascript_function():
    # Define the Streamlit app layout
    st.title("Python to JavaScript Converter")
    st.write('')
    
    python_code = st.text_area("Input Python code")
    javascript_code = st.empty()
    # Parse the Python code and generate equivalent JavaScript code using GPT-3.5-turbo
    if st.button("Convert to JavaScript"):
        generated_code = convert_python_javascript(python_code)
        # Output the generated JavaScript code
        javascript_code.text_area("Generated JavaScript code", value=generated_code, height=400)

def sql_translate():
    # Define the Streamlit app layout
    st.title("SQL Request - Random query Generator")
    st.write('')
    
    # Define Streamlit components
    query = st.text_input("The query for the follwoing statement:")
    submit_button = st.button("Submit")
    sql_code = st.empty()

    if submit_button:
        sql_query = generate_sql_queries(query)
        sql_code.text_area("Generated SQL query for the following statement:", value=sql_query, height=400)

def job_interview_question():
    # Define Streamlit app layout
    st.title("Interview Questions Generator")
    st.write('')
    st.write("Enter any relevant information about the job role below to generate interview questions and answers:")

    # Collect user input
    job_info = st.text_input("Job Information:")

    # Generate questions and answers on button click
    if st.button("Generate Q&A"):
        st.write("Generating questions")
        # inter_ques = st.empty()
        # Extract question and answer pairs from OpenAI response
        question_answers = interview_question(job_info)

        # inter_ques.text_area("Generated Interview Questions", value=question_answers, height=400)
        # Display generated questions and answers
        for qa in question_answers:
            st.write(qa)

def app():
    st.title('Programming Application AI')
    page = st.sidebar.selectbox("Choose a page", ["--Select Page--", "Python Converter", "SQL Translate", "Interview Questions"])
    
    if page == "--Select Page--":
        st.write('')
        st.subheader("Please select a page from the list given on the sidebar")
    
    elif page == "Python Converter":
        st.write('')
        python_javascript_function()
    
    elif page == "SQL Translate":
        st.write('')
        sql_translate()
    
    elif page == "Interview Questions":
        st.write('')
        job_interview_question()

if __name__ == "__main__":
    app()
