def fuse_emotions(text_result, face_result):
    try:
        text_emotion = text_result.get("emotion")
        face_emotion = face_result.get("emotion")

        text_conf = text_result.get("confidence")
        face_conf = face_result.get("confidence")

        
        try:
            text_conf = float(text_conf)
        except:
            text_conf = 0.0

        try:
            face_conf = float(face_conf)
        except:
            face_conf = 0.0

        # CASE 1: Both models agree
        if text_emotion == face_emotion:
            return {
                "final_emotion": text_emotion,
                "confidence": round((text_conf + face_conf) / 2, 2),
                "text_emotion": text_emotion,
                "face_emotion": face_emotion,
                "decision": "Both models agree"
            }

        # CASE 2: Face clearly stronger
        if face_conf > text_conf + 0.2:
            return {
                "final_emotion": face_emotion,
                "confidence": face_conf,
                "text_emotion": text_emotion,
                "face_emotion": face_emotion,
                "decision": "Face model more confident"
            }

        # CASE 3: Text clearly stronger
        if text_conf > face_conf + 0.2:
            return {
                "final_emotion": text_emotion,
                "confidence": text_conf,
                "text_emotion": text_emotion,
                "face_emotion": face_emotion,
                "decision": "Text model more confident"
            }

        # CASE 4: Close → weighted fusion
        final_conf = (text_conf * 0.4) + (face_conf * 0.6)

        return {
            "final_emotion": face_emotion,  # slight bias to face
            "confidence": round(final_conf, 2),
            "text_emotion": text_emotion,
            "face_emotion": face_emotion,
            "decision": "Weighted fusion (combined decision)"
        }

    except Exception as e:
        return {
            "error": str(e),
            "final_emotion": None,
            "confidence": 0
        }