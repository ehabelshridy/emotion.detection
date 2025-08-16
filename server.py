"""Flask app for detecting emotions using Hugging Face API."""
import os
from dotenv import load_dotenv
import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)
load_dotenv()
# Hugging Face API configuration
HF_API_KEY = os.environ.get("HF_API_KEY")
MODEL_URL = (
    "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
)
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

@app.route("/", methods=["GET"])
def index():
    """
    Render the home page.
    
    Returns:
        HTML template: index.html
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector():
    """
    Detect the dominant emotion from the provided text.
    
    Query Params:
        textToAnalyze (str): The text to analyze.
    
    Returns:
        str: The dominant emotion or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "No text provided"

    # Send request to Hugging Face model
    response = requests.post(
        MODEL_URL, headers=HEADERS, json={"inputs": text_to_analyze}, timeout=10
    )

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    result = response.json()

    # Extract the dominant emotion
    if isinstance(result, list) and len(result) > 0:
        emotions = result[0]
        dominant_emotion = max(emotions, key=lambda x: x["score"])["label"]
        return f"The dominant emotion is {dominant_emotion}"

    return "The dominant emotion is unknown"


if __name__ == "__main__":
    app.run(debug=True)
