# Empathy Engine Demo

🎙️ **Empathy Engine** is a local AI-powered web application that detects the emotional tone of a text input, generates a supportive response, and converts it into expressive speech. The web interface features an interactive bubble background for a visually engaging experience.

---

## Features

* **Text Input:** Enter a short paragraph (3–5 sentences recommended) in the input box.
* **Emotion Detection:** Detects the emotional tone (Positive, Negative, Neutral) using TextBlob.
* **Audio Output:** Generates a local `.wav` file with expressive speech using pyttsx3.
* **Interactive Web UI:** Engaging black-background interface with floating, clickable bubbles.
* **Enhanced Buttons:**

  * `Analyze & Speak` button (blue)
  * `Clear` and `Replay` buttons (red)
  * Download button styled to match the theme.

---

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Libraries:**

  * `TextBlob` for sentiment/emotion detection
  * `pyttsx3` for local text-to-speech
* **Design:** Interactive bubble animation using CSS + JS

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Jithesh1464/Jithesh-s-Empathy-Engine.git
cd EmpathyEngine
```

2. **Create a virtual environment (optional but recommended)**

```
python -m venv venv
```

Activate it:

* **Windows:** `venv\Scripts\activate`
* **Linux/Mac:** `source venv/bin/activate`

3. **Install dependencies**

```
pip install -r requirements.txt
```

> If you don't have a `requirements.txt`, install manually:

```
pip install flask textblob pyttsx3
python -m textblob.download_corpora
```

---

## Running the Application

1. **Start the Flask server**

```
python app.py
```

2. **Open your browser** and go to:

```
http://127.0.0.1:5000
```

3. **Use the interface:**

   * Type or paste text in the input box.
   * Click **Analyze & Speak** to detect emotion and generate speech.
   * Replay or download the audio using the buttons.

---

## Sample Input & Expected Output

### Input 1:

```
I just got a promotion at work! I am so happy and excited about my future.
```

**Expected Output:**

* **Emotion:** Positive
* **Intensity:** High
* **Response Text:** "That's fantastic! Congratulations on your well-deserved success!"
* **Audio:** Plays a happy, enthusiastic voice reflecting the positive sentiment.

---

### Input 2:

```
I am frustrated with my project; nothing seems to be working as expected.
```

**Expected Output:**

* **Emotion:** Negative
* **Intensity:** Medium
* **Response Text:** "I understand your frustration. Take a deep breath, and let's try to find a solution together."
* **Audio:** Plays a calm, empathetic voice reflecting concern.

---

### Input 3:

```
Today is an ordinary day, nothing special happened.
```

**Expected Output:**

* **Emotion:** Neutral
* **Intensity:** Low
* **Response Text:** "Thanks for sharing. Let's see what interesting things might come next!"
* **Audio:** Plays a neutral, calm voice.

---

## Notes

* **All audio processing is local** — no API keys or external TTS services are required.
* The **bubble animation and black background** create a visually immersive experience without affecting functionality.
* Adjust the **text length** to get more accurate emotional detection and richer audio output.

---

## Future Improvements

* Adding more nuanced emotions (e.g., excited, surprised, concerned).
* Using HuggingFace Transformers for advanced emotion detection.
* Adding **intensity scaling** to modulate pitch and speed based on emotional strength.
* Integrating **SSML** for finer control over speech synthesis.
* Making the application **fully responsive** on mobile devices.

---

## Author

Developed by **\Jithesh Kottu** as part of the Empathy Engine project demo for  Darwix AI Hackathon.
