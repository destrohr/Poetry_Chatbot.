import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
OpenAI.model_rebuild()

OpenAIAPIKey = st.secrets["OPENAI_API_KEY"]

def GeneratePoetryWithLangChain(UserInput, Level, Language, Hints=""):
    if Language == "English":
        if Level == "Simple":
            Template = f"""Write a heartfelt 4-line poem from my perspective, using "I" and "you".
            Theme: {{UserInput}}.
            {f"Include these details: {Hints}" if Hints else ""}
            Use simple, emotional language with rhyme."""
        else:
            Template = f"""Compose an intimate 4-line love poem using "I" and "you".
            Theme: {{UserInput}}.
            {f"Weave in these elements: {Hints}" if Hints else ""}
            Use sophisticated metaphors and lyrical flow."""
    elif Language == "Tamil":
        if Level == "Simple":
            Template = f"""என்னுடைய கண்ணோட்டத்தில் 4 வரி காதல் கவிதை எழுது. "நான்" மற்றும் "நீ" பயன்படுத்து.
            தலைப்பு: {{UserInput}}.
            {f"இந்த விவரங்களை சேர்: {Hints}" if Hints else ""}
            எளிய தமிழ் மற்றும் ஓசை நயம்."""
        else:
            Template = f"""அதிநவீன 4 வரி தமிழ்க் கவிதை உருவாக்கு. "நான்" மற்றும் "நீ" ஐ கையாளு.
            தலைப்பு: {{UserInput}}.
            {f"இந்த உணர்வுகளை பின்னு: {Hints}" if Hints else ""}
            பண்டைய தமிழ் கவிதை மரபுகளை பயன்படுத்து."""
    Prompt = PromptTemplate(input_variables=["UserInput"], template=Template)
    LLM = OpenAI(api_key=OpenAIAPIKey, temperature=0.7, max_tokens=200)
    PoetryChain = LLMChain(llm=LLM, prompt=Prompt)
    return PoetryChain.run(UserInput)

def Main():
    st.title("Multilingual Poetry Bot ")
    col1, col2 = st.columns(2)
    with col1:
        PoetryLevel = st.selectbox("Complexity Level", ["Simple", "Advanced"])
    with col2:
        Language = st.selectbox("Language", ["English", "Tamil"])
    UserInput = st.text_input("Main Theme (e.g., Love, Friendship):")
    Hints = st.text_area("Life Hints/Details (optional, max 2 sentences):",
                         placeholder="e.g., We met in college, she loved roses...",
                         max_chars=200)

    if st.button("Generate Poetry"):
        if not UserInput.strip():
            st.warning("Please enter a main theme/title!")
        else:
            with st.spinner("Crafting your poem..."):
                try:
                    Poetry = GeneratePoetryWithLangChain( UserInput, PoetryLevel,Language, Hints)
                    st.subheader("Your Custom Poem:")
                    st.write(Poetry)
                except Exception as e:
                    st.error(f"Error generating poem: {str(e)}")
Main()
