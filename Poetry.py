def Main():
    st.title("Multilingual Poetry Bot")
    col1, col2 = st.columns(2)

    with col1:
        PoetryLevel = st.selectbox("Complexity Level", ["Simple", "Advanced"])
    with col2:
        Language = st.selectbox("Language", ["English", "Tamil"])

    UserInput = st.text_input("Main Theme (e.g., Love, Friendship):")
    Hints = st.text_area("Life Hints/Details (optional, max 2 sentences):", max_chars=200)

    if st.button("Generate Poetry"):
        if not UserInput.strip():
            st.warning("Please enter a main theme/title!")
        else:
            with st.spinner("Crafting your poem..."):
                try:
                    Poetry = GeneratePoetryWithLangChain(UserInput, PoetryLevel, Language, Hints)
                    st.subheader("Your Custom Poem:")
                    st.write(Poetry)
                except Exception as e:
                    st.error(f"Error generating poem: {str(e)}")

Main() 
