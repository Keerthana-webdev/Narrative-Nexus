import nltk #natural lang toolkit(used fr text processing n tokenization)
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from cleaning import clean_text

#Downloads
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):

    #Original stats
    original_words = len(text.split())
    original_chars = len(text)

    #Cleaning
    cleaned = clean_text(text)

    #Tokenization
    tokens = nltk.word_tokenize(cleaned)

    #Stopwords removal
    tokens = [t for t in tokens if t not in stop_words]

    #Lemmatization
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    #Final processed text
    processed_text = " ".join(tokens)

    #Cleaned stats
    cleaned_words = len(tokens)
    cleaned_chars = len(processed_text)

    #Reduction %
    word_reduction = round(((original_words - cleaned_words)/original_words)*100,2) if original_words else 0
    char_reduction = round(((original_chars - cleaned_chars)/original_chars)*100,2) if original_chars else 0

    return {
        "original_text": text,
        "processed_text": processed_text,
        "original_words": original_words,
        "original_chars": original_chars,
        "cleaned_words": cleaned_words,
        "cleaned_chars": cleaned_chars,
        "word_reduction": word_reduction,
        "char_reduction": char_reduction,
        "tokens": tokens
    }
