import re
import string
import nltk
# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

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
    return ' '.join([wordnet_lemmatizer.lemmatize(w) for w in tokens])

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from pyngrok import ngrok
import nest_asyncio
from fastapi.responses import RedirectResponse

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest", tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest")

# Initialize FastAPI app
app = FastAPI()

# Input data model
class TextInput(BaseModel):
    text: str

# Welcome endpoint that redirects to Swagger UI
@app.get("/")
async def welcome():
    return RedirectResponse(url='/docs')

# Sentiment analysis endpoint
@app.post("/analyze/")
async def analyze_text(text_input: TextInput):
    text = text_input.text

    # Preprocess the text
    text = remove_urls(text)
    text = remove_punctuation(text)
    text = lower_case(text)
    text = lemmatize(text)

    # Perform sentiment analysis
    try:
        result = sentiment_analyzer(text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app using Uvicorn and ngrok
if __name__ == "__main__":
    # Setup ngrok
    ngrok_tunnel = ngrok.connect(8000)
    print('Public URL:', ngrok_tunnel.public_url)

    # Allow nested asyncio calls
    nest_asyncio.apply()

    # Run the app with Uvicorn
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
