from flask import Flask, request, jsonify
from models.text_emotion_model import predict_emotion  
from models.face_emotion_model import predict_face_emotion  
from models.fusion_model import fuse_emotions   
from flask_cors import CORS 

app = Flask(__name__)  # Create Flask application
CORS(app)

# ------------------------------
# ROOT ENDPOINT (TEST API)
# ------------------------------

@app.route("/")
def home():
    return "API Running"

# ------------------------------
# TEXT EMOTION ENDPOINT
# ------------------------------

@app.route("/predict/text", methods=["POST"])
def predict_text():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    return jsonify(predict_emotion(data["text"]))

# ------------------------------
# FACE EMOTION ENDPOINT
# ------------------------------

@app.route("/predict/image", methods=["POST"])
def predict_image():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({"error": "No image provided"}), 400

    return jsonify(predict_face_emotion(data["image"]))

# ------------------------------
# FUSION ENDPOINT (MAIN LOGIC)
# ------------------------------

@app.route("/predict/fusion", methods=["POST"])
def predict_fusion():
    data = request.get_json()

    text_result = predict_emotion(data["text"])
    face_result = predict_face_emotion(data["image"])

    print("TEXT RESULT:", text_result)
    print("FACE RESULT:", face_result)

    final_result = fuse_emotions(text_result, face_result)

    print("FINAL RESULT:", final_result)

    return jsonify(final_result)

# ------------------------------
# RUN APPLICATION
# ------------------------------

if __name__ == "__main__":
    app.run(debug=True)