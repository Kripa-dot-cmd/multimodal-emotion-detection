from deepface import DeepFace
import base64
import tempfile
import os

def predict_face_emotion(image_data):
    try:
        # Decode image
        img_bytes = base64.b64decode(image_data)

        
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            tmp.write(img_bytes)
            tmp_path = tmp.name

        
        result = DeepFace.analyze(
            img_path=tmp_path,
            actions=["emotion"],
            enforce_detection=False
        )

        
        os.unlink(tmp_path)

        
        dominant_emotion = result[0]["dominant_emotion"]
        confidence = result[0]["emotion"][dominant_emotion]

        return {
            "emotion": str(dominant_emotion),
            "confidence": round(float(confidence) / 100, 2)
        }

    except Exception as e:
        return {"error": str(e)}