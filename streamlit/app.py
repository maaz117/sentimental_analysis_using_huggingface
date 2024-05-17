import streamlit as st
from transformers import pipeline
import nltk
import re
import string

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest", tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest")

# Text preprocessing functions
def remove_urls(text):
    return re.sub(r'http[s]?://\S+', '', text)

def remove_punctuation(text):
    regular_punct = string.punctuation
    return re.sub(r'[' + regular_punct + ']', '', text)

def lower_case(text):
    return text.lower()

def lemmatize(text):
    wordnet_lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(text)
    lemmatized_text = [wordnet_lemmatizer.lemmatize(w) for w in tokens]
    return ' '.join(lemmatized_text)

# Streamlit UI
def main():
    st.title("Sentiment Analysis")
    st.write("Enter the text you'd like to analyze:")

    user_input = st.text_input("Text Input")  # Changed from st.text_area to st.text_input for single-line input
    if st.button("Analyze Sentiment"):
        if user_input:
            # Preprocess the text
            text = remove_urls(user_input)
            text = remove_punctuation(text)
            text = lower_case(text)
            text = lemmatize(text)

            # Perform sentiment analysis
            try:
                result = sentiment_analyzer(text)
                st.write(result)
            except Exception as e:
                st.error(f"Error analyzing sentiment: {str(e)}")
        else:
            st.error("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
