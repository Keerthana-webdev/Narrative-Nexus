from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

#WORD CLOUD 
def show_wordcloud(text):
    if not text.strip():
        st.warning("No text available for Word Cloud.")
        return

    wordcloud = WordCloud(
        width=400,
        height=200,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)


#SENTIMENT DISTRIBUTION CHART
def show_sentiment_chart(download_list):
    sentiments = {
        "Positive": 0,
        "Neutral": 0,
        "Negative": 0
    }

    for item in download_list:
        score = item["compound_score"]
        if score > 0.05:
            sentiments["Positive"] += 1
        elif score < -0.05:
            sentiments["Negative"] += 1
        else:
            sentiments["Neutral"] += 1

    df = pd.DataFrame.from_dict(sentiments, orient="index", columns=["Count"])
    st.bar_chart(df)
