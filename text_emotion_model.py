import joblib
import os

BASE_DIR = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE_DIR, "emotion_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

def predict_emotion(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]

    try:
        probabilities = model.predict_proba(text_vector)
        confidence = float(max(probabilities[0]))
    except:
        confidence = 0.0   

    return {
        "emotion": prediction,
        "confidence": round(confidence, 2)
    }