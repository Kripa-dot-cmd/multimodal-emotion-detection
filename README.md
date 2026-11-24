# Multimodal Emotion Detection System

A Flask REST API that detects emotion from text and facial expressions and
combines both predictions using confidence-based decision-level fusion.
Built as my BSc Computer Science dissertation at London South Bank University.

## How it works
- **Text:** TF-IDF features + LinearSVC classifier
- **Face:** DeepFace facial expression analysis (TensorFlow backend)
- **Fusion:** each modality returns an emotion with a confidence score;
  the system combines them at decision level, [describe your rule, e.g.
  choosing the higher-confidence prediction]

## Tech stack
Python 3.10, Flask, scikit-learn, DeepFace, TensorFlow

## Setup
1. `git clone https://github.com/Kripa-dot-cmd/multimodal-emotion-detection.git`
2. `python -m venv venv && venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python [your main file].py`

## API endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /[your route] | [what it accepts and returns] |

## Example request/response
[paste a real example]

## Challenges solved
- Resolved DeepFace/TensorFlow (tf-keras) compatibility issues
- Fixed JSON serialisation errors for NumPy float32 model outputs

## Evaluation
[Add precision, recall, F1 and the test split once you've run them. Leave
this section out until you have real figures.]

## Licence
MIT


