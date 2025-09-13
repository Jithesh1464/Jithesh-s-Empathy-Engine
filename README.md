# Jithesh-s-Empathy-Engine 🎙️

## Overview
The **Empathy Engine** is a Python-based project that transforms plain text into emotionally expressive speech. Unlike standard monotonic text-to-speech (TTS) systems, this engine detects the sentiment of the input text (Positive, Negative, Neutral) and dynamically modulates voice parameters like **rate**, **pitch**, and **volume** to sound more human-like.

This project was built as part of a hackathon challenge with a time constraint of ~1.5 hours. The focus is on simplicity, clarity, and demonstrable functionality.

---

## Features
- Accepts text input (via CLI or web interface).
- Detects sentiment using **TextBlob**.
- Maps emotions (Positive / Negative / Neutral) to vocal parameters.
- Generates expressive speech output via **pyttsx3** (offline, no API keys required).
- Outputs playable `.wav` or `.mp3` audio files.
- Optional: Run as a **Flask web app** with a text box + audio player.

---

## Tech Stack
- **Python 3.9+**
- [TextBlob](https://textblob.readthedocs.io/en/dev/) → Sentiment analysis
- [pyttsx3](https://pyttsx3.readthedocs.io/) → Offline text-to-speech
- [Flask](https://flask.palletsprojects.com/) → Web UI (optional)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/empathy-engine.git
   cd empathy-engine
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download TextBlob corpora (needed for sentiment analysis):
   ```bash
   python -m textblob.download_corpora
   ```

---

## Usage

### CLI Mode (Quick Demo)
Run:
```bash
python empathy_engine.py
```

Enter text when prompted, and the system will:
- Detect sentiment
- Adjust speech parameters
- Generate spoken output

An audio file (`output.wav`) will also be saved.

---

### Flask Web UI (Optional)
To launch the web interface:
```bash
python empathy_engine.py --web
```

- Open your browser at `http://127.0.0.1:5000/`
- Enter text → Hear expressive voice output instantly.

---

## Example Emotion-to-Voice Mapping
- **Positive** → Faster rate, higher pitch, louder volume
- **Negative** → Slower rate, lower pitch, softer volume
- **Neutral** → Default values

---

## Folder Structure
```
empathy-engine/
│── empathy_engine.py       # Main script
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── static/                 # (Optional) Web assets
│── output.wav              # Generated audio
```

---

## Future Improvements
- Add more granular emotions (e.g., excited, calm, angry, surprised).
- Scale intensity based on sentiment polarity score.
- Integrate SSML for advanced vocal control.
- Deploy as a hosted web demo.

---

## License
This project is for educational and hackathon purposes.
