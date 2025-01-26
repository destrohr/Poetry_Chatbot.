import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI

OpenAIAPIKey = st.secrets["OPENAI_API_KEY"]

def GeneratePoetryWithLangChain(UserInput, Level):
    if Level == "Simple":
        Template = """
        You are a poetic assistant that writes sweet English poems in simple language.
        Write a sweet English poem about: {UserInput}.
        """
    else:
        Template = """
        You are a poetic assistant that writes sweet English poems in advanced language (C1 level).
        Write a sweet English poem about: {UserInput}.
        """
    Prompt = PromptTemplate(input_variables=["UserInput"], template=Template)  # Fixed typo here
    LLM = OpenAI(api_key=OpenAIAPIKey, temperature=0.7, max_tokens=100)
    PoetryChain = LLMChain(llm=LLM, prompt=Prompt)
    Poetry = PoetryChain.run(UserInput)
    return Poetry


def Main():
    st.title("Sweet Poetry Chatbot ")
    PoetryLevel = st.selectbox("Select Poetry Level", ["Simple", "Advanced"])
    UserInput = st.text_input("Write a few sentences:")
    if st.button("Generate Poetry"):
        if UserInput.strip() == "":
            st.warning("Please enter some text!")
        else:
            Poetry = GeneratePoetryWithLangChain(UserInput, PoetryLevel)
            st.write("Here's your sweet poetry:")
            st.write(Poetry)
Main()