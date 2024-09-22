# pip install openai
# pip install langchain
# pip install langchain_community
# pip install streamlit

import streamlit as st
from langchain.llms import OpenAI
import subprocess


def create_requirements():
    # Define the file path for requirements.txt
    file_path = "requirements.txt"

    # Open the file and write the output of pip freeze to it
    with open(file_path, "w") as file:
        subprocess.run(["pip", "freeze"], stdout=file)

    print(f"requirements.txt created at: {file_path}")


# Call the function to create the requirements file
create_requirements()

# My App title
st.title('NewbieLM 🐼')

# Input sidebar
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')


# function to generate a response
def generate_response(input_text):
    # Initializing the OpenAI model with a specified temperature and API key
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))


# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input with a default prompt
    text = st.text_area('Enter text:', '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠️')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
