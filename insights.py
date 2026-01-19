def generate_insights(lda_topics, sentiment_summary):
    insights = []

    for topic in lda_topics:
        insights.append(
            f"Topic '{topic['topic']}' mainly discusses: {topic['words']}."
        )

    insights.append(
        f"Overall dataset sentiment is {sentiment_summary}, indicating the general emotional tone of the documents."
    )

    return insights
