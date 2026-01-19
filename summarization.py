from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from transformers import pipeline

# Download tokenizer once
nltk.download("punkt")

#EXTRACTIVE SUMMARIZATION
def extractive_summary(text, num_sentences=3):
    if not text or len(text.split()) < 20:
        return "Text too short for extractive summarization."

    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    freq = Counter(words)

    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    summary = " ".join(ranked_sentences[:num_sentences])
    return summary


#ABSTRACTIVE SUMMARIZATION
def abstractive_summary(text):
    if not text or len(text.split()) < 50:
        return "Text too short for abstractive summarization."

    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

    result = summarizer(
        text,
        max_length=130,
        min_length=40,
        do_sample=False
    )

    return result[0]["summary_text"]
