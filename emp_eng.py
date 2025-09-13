from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive"
        response = "I’m glad to hear that! Keep spreading positivity."
    elif polarity < -0.2:
        sentiment = "Negative"
        response = "I understand that things feel tough . You’re not alone."
    else:
        sentiment = "Neutral"
        response = "Thanks for sharing your thoughts. I’m here to listen."

    return sentiment, response
