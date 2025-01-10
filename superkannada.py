import streamlit as st
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text(text, src, dest):
    try:
        return GoogleTranslator(source=src, target=dest).translate(text)
    except Exception as e:
        return f"Error: {e}"

# App Title and Description
st.title("SuperKannada Chatbot")
st.markdown("""
### Learn Kannada with Ease

This AI assistant is your friendly guide to mastering Kannada. Simply ask any Kannada-related question, and it will respond with:

1. The correct Kannada word/sentence
2. English transliteration
3. Meaning in your selected language
4. Usage examples

Feel free to ask anything about Kannada vocabulary, grammar, or daily conversational phrases!

*Powered by Learn AI*
""")

# Sidebar for Theme Selection
st.sidebar.title("Chatbot Theme")
selected_theme = st.sidebar.radio(
    "Choose your preferred theme:",
    ["Light", "Dark"]
)

if selected_theme == "Dark":
    st.markdown(
        "<style>body { background-color: #2c2c2c; color: #ffffff; }</style>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<style>body { background-color: #ffffff; color: #000000; }</style>",
        unsafe_allow_html=True
    )

# User Input
query = st.text_input("Enter your Kannada-related query:", placeholder="Type your question here...")
user_language = st.selectbox(
    "Select your language for translation:", ["en", "hi", "ta", "te", "ml", "mr"]
)

if query:
    # Sample response (to be replaced with AI logic or advanced NLP)
    kannada_translation = "ನೀವು ಕೇಳಿರುವ ಪ್ರಶ್ನೆಯ ಉತ್ತರ ಇಲ್ಲಿದೆ!"
    transliteration = "Nīvu kēḷiruva praśneya uttara illide!"
    meaning = translate_text(kannada_translation, src="kn", dest=user_language)
    usage_example = "ನಾನು ಕನ್ನಡದಲ್ಲಿ ಮಾತನಾಡಲು ಬಯಸುತ್ತೇನೆ. (I want to speak in Kannada.)"

    # Display the results
    st.subheader("Response")
    st.write(f"**Kannada Translation:** {kannada_translation}")
    st.write(f"**Transliteration:** {transliteration}")
    st.write(f"**Meaning in Selected Language:** {meaning}")
    st.write(f"**Usage Example:** {usage_example}")

    st.markdown("*Powered by Learn AI*")
