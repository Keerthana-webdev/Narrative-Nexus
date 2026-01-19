import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Performs sentiment analysis using VADER
    Returns sentiment label + scores
    """

    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive 😊"
    elif compound <= -0.05:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    return {
        "sentiment": sentiment,
        "positive": scores["pos"],
        "neutral": scores["neu"],
        "negative": scores["neg"],
        "compound": compound
    }
