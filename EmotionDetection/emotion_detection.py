import requests

def emotion_detector(text_to_analyze):
   HF_API_KEY = os.environ.get("HF_API_KEY")
MODEL_URL = (
    "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
)
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": text_to_analyze}  # لاحظ هنا inputs بدل text

    try:
        response = requests.post(url, json=payload, headers=headers)
        result = response.json()

        if isinstance(result, list) and len(result) > 0:
            emotions_list = result[0]  
            emotions = {item["label"]: item["score"] for item in emotions_list}

            dominant_emotion = max(emotions, key=emotions.get)
        else:
            emotions = {}
            dominant_emotion = "unknown"

        return {
            "emotion": emotions,
            "dominant_emotion": dominant_emotion
        }

    except Exception as e:
        print("Error in emotion_detector:", e)
        return {
            "emotion": {},
            "dominant_emotion": "unknown"
        }

