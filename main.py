import os
import re
import time
import hashlib
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from textblob import TextBlob
import pyttsx3


BASE_DIR = Path(__file__).parent.resolve()
AUDIO_DIR = BASE_DIR / "static" / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__, static_folder="static", template_folder="templates")


def detect_emotion_and_intensity(text):
    tb = TextBlob(text)
    polarity = tb.sentiment.polarity  
    intensity = min(1.0, abs(polarity))

    
    lowered = text.lower()
    if lowered.strip().endswith("?"):
        return "inquisitive", polarity, intensity
    if re.search(r"\b(wow|amazing|unbelievable|surprised|astonished)\b", lowered):
       
        return "surprised", polarity, intensity
    if re.search(r"\b(worried|concerned|anxious|uneasy|nervous)\b", lowered):
        return "concerned", polarity, intensity

 
    if polarity > 0.15:
        return "happy", polarity, intensity
    elif polarity < -0.15:
        return "frustrated", polarity, intensity
    else:
        return "neutral", polarity, intensity


def map_emotion_to_params(emotion, intensity, engine):
    # base defaults
    base_rate = engine.getProperty("rate") or 150
    base_volume = engine.getProperty("volume") or 1.0
    voices = engine.getProperty("voices") or []

    
    voice_id = None
    try:
        
        vlist = list(voices)
        if emotion == "happy":
            
            for v in vlist:
                if "female" in (v.name.lower() + v.id.lower()):
                    voice_id = v.id; break
        elif emotion == "frustrated" or emotion == "concerned":
            for v in vlist:
                if "male" in (v.name.lower() + v.id.lower()):
                    voice_id = v.id; break
       
        if not voice_id and len(vlist) > 0:
            voice_id = vlist[0].id
    except Exception:
        voice_id = None

    
    rate_delta = int(40 * intensity)  # up to +-40 change
    vol_delta = 0.0 + (0.25 * intensity)  # up to +0.25 or -0.25

    # default params
    rate = base_rate
    volume = max(0.1, min(1.0, base_volume))

    if emotion == "happy" or emotion == "surprised":
        rate = base_rate + rate_delta  # faster
        volume = min(1.0, volume + vol_delta)  # louder
    elif emotion == "frustrated":
        rate = max(80, base_rate - rate_delta)  # slower
        volume = max(0.1, volume - vol_delta)  # softer
    elif emotion == "concerned":
        rate = max(90, base_rate - int(rate_delta/1.5))
        volume = max(0.1, volume - vol_delta/1.2)
    elif emotion == "inquisitive":
        # slightly faster with varied intonation (we emulate with rate)
        rate = base_rate + int(rate_delta/2)
        volume = min(1.0, volume + vol_delta/2)
    else:  # neutral
        rate = base_rate
        volume = volume

    return {"rate": int(rate), "volume": float(volume), "voice_id": voice_id}


def synthesize_text_to_wav(text, params):
    engine = pyttsx3.init()
    
    try:
        if params.get("voice_id"):
            engine.setProperty("voice", params["voice_id"])
    except Exception:
        pass
    try:
        engine.setProperty("rate", int(params.get("rate", engine.getProperty("rate"))))
    except Exception:
        pass
    try:
        engine.setProperty("volume", float(params.get("volume", engine.getProperty("volume"))))
    except Exception:
        pass

    # unique filename using timestamp + hash
    stamp = str(time.time()).encode("utf-8")
    h = hashlib.sha1(stamp + text.encode("utf-8")).hexdigest()[:10]
    filename = f"speech_{h}.wav"
    out_path = AUDIO_DIR / filename

    # save to file and block until finished
    engine.save_to_file(text, str(out_path))
    engine.runAndWait()

    return filename


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    user_text = request.form.get("user_input", "").strip()
    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    emotion, polarity, intensity = detect_emotion_and_intensity(user_text)

    
    engine_local = pyttsx3.init()
    params = map_emotion_to_params(emotion, intensity, engine_local)


    if emotion == "happy":
        reply_text = "That's wonderful to hear! I'm really happy for you."
    elif emotion == "frustrated":
        reply_text = "I'm sorry you're facing this. I understand — that must be frustrating."
    elif emotion == "neutral":
        reply_text = "Thank you for sharing that. I'm here to listen."
    elif emotion == "surprised":
        reply_text = "Wow — that's surprising! Tell me more, I'm intrigued."
    elif emotion == "inquisitive":
        reply_text = "That's a good question. Let's explore it together."
    elif emotion == "concerned":
        reply_text = "I can see why you'd be worried. It's okay to feel that way."
    else:
        reply_text = "Thanks for sharing."

    # Optionally append a short clarifying or supportive line scaled by intensity
    if intensity >= 0.6:
        reply_text += " (You seem pretty strongly about this.)"

    # create TTS file
    filename = synthesize_text_to_wav(reply_text, params)
    audio_url = url_for('static', filename=f"audio/{filename}")

    # return structured JSON
    return jsonify({
        "emotion": emotion,
        "polarity": polarity,
        "intensity": round(float(intensity), 3),
        "text_response": reply_text,
        "audio_url": audio_url
    })

# Serve audio files (Flask static already serves /static, but this helper exists if needed)
@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == "__main__":
    # run local dev server
    app.run(debug=True)

