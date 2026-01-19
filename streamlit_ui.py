import streamlit as st
from collection import extract_text, get_file_details
from preprocessing import preprocess_text
from model import lda_topic_model
from css import load_css
from sentiment import analyze_sentiment
from summarization import extractive_summary, abstractive_summary
from insights import generate_insights
from visualization import show_wordcloud, show_sentiment_chart
from reporting import generate_pdf_report
import pandas as pd

def render_ui():

    if "overall_sentiment" not in st.session_state:
        st.session_state.overall_sentiment = None

    if "lda_topics" not in st.session_state:
        st.session_state.lda_topics = []

    if "extractive" not in st.session_state:
        st.session_state.extractive = ""

    if "abstractive" not in st.session_state:
        st.session_state.abstractive = ""

    # PAGE SETUP
    st.set_page_config(page_title="NarrativeNexus", layout="wide")
    st.markdown(load_css(), unsafe_allow_html=True)

    st.markdown("<h1 class='page-title'>📘 NarrativeNexus</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='page-subtitle'>Dynamic Text Analysis Platform</h3>", unsafe_allow_html=True)

    # FILE UPLOAD
    st.markdown("<div class='card-section'>", unsafe_allow_html=True)
    st.markdown("<h4 class='section-title'>📥 Upload Your Files</h4>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader("", type=["txt", "pdf", "docx", "csv"], accept_multiple_files=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # DIRECT INPUT
    st.markdown("<div class='card-section'>", unsafe_allow_html=True)
    st.markdown("<h4 class='section-title'>✍ Paste Text Directly</h4>", unsafe_allow_html=True)
    direct_text = st.text_area("", height=180)
    st.markdown("</div>", unsafe_allow_html=True)

    # PROCESS BUTTON
    st.markdown("<div class='card-section center'>", unsafe_allow_html=True)

    if st.button("🚀Analyze Text", use_container_width=True):

        all_inputs = []

        # Uploaded Files
        if uploaded_files:
            for file in uploaded_files:
                details = get_file_details(file)
                text = extract_text(file)
                all_inputs.append((details, text))

        # Direct Text
        if direct_text.strip():
            all_inputs.append((
                {"name": "Direct Input", "type": "text/plain",
                 "size_kb": round(len(direct_text) / 1024, 2), "extension": "txt"},
                direct_text
            ))

        if not all_inputs:
            st.error("❌ No valid input provided.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        st.markdown("</div>", unsafe_allow_html=True)

        # DISPLAY ANALYSIS
        download_list = []

        for details, text in all_inputs:

            # File title card
            st.markdown(f"<div class='file-title'>📄 {details['name']}</div>", unsafe_allow_html=True)

            with st.container():
                colA, colB, colC = st.columns([1.5, 1, 1])
                colA.markdown("**File Type:** " + details['type'])
                colB.markdown(f"**Size:** {details['size_kb']} KB")
                colC.markdown("**Extension:** " + details['extension'])

            # Preprocessing
            result = preprocess_text(text)

            # Statistics
            st.markdown("<h3 class='section-title'>📊 Text Statistics</h3>", unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)
            col1.markdown(f"<div class='stat-card blue'><div class='stat-number'>{result['original_words']}</div><div class='stat-label'>Original Words</div></div>", unsafe_allow_html=True)
            col2.markdown(f"<div class='stat-card purple'><div class='stat-number'>{result['original_chars']}</div><div class='stat-label'>Original Characters</div></div>", unsafe_allow_html=True)
            col3.markdown(f"<div class='stat-card blue'><div class='stat-number'>{result['cleaned_words']}</div><div class='stat-label'>Cleaned Words</div></div>", unsafe_allow_html=True)
            col4.markdown(f"<div class='stat-card purple'><div class='stat-number'>{result['cleaned_chars']}</div><div class='stat-label'>Cleaned Characters</div></div>", unsafe_allow_html=True)

            # Reduction Stats
            st.markdown("<br>", unsafe_allow_html=True)
            colr1, colr2 = st.columns(2)
            colr1.markdown(f"<div class='reduce-card'>Word Reduction: {result['word_reduction']}%</div>", unsafe_allow_html=True)
            colr2.markdown(f"<div class='reduce-card'>Character Reduction: {result['char_reduction']}%</div>", unsafe_allow_html=True)

            # Text Comparison
            st.markdown("<h3 class='section-title'>🔍 Text Comparison</h3>", unsafe_allow_html=True)
            colA, colB = st.columns(2)
            colA.markdown("<div class='text-box-title'>⛔ Original Text</div>", unsafe_allow_html=True)
            colA.markdown(f"<div class='text-box'>{result['original_text']}</div>", unsafe_allow_html=True)
            colB.markdown("<div class='text-box-title'>✔ Cleaned Text</div>", unsafe_allow_html=True)
            colB.markdown(f"<div class='text-box'>{result['processed_text']}</div>", unsafe_allow_html=True)

            # SENTIMENT ANALYSIS
            sentiment_result = analyze_sentiment(result["processed_text"])
            st.markdown("<h3 class='section-title'>😊 Sentiment Analysis</h3>", unsafe_allow_html=True)
            colS1, colS2, colS3, colS4 = st.columns(4)
            colS1.markdown(f"<div class='stat-card blue'><div class='stat-number'>{sentiment_result['positive']}</div><div class='stat-label'>Positive</div></div>", unsafe_allow_html=True)
            colS2.markdown(f"<div class='stat-card purple'><div class='stat-number'>{sentiment_result['neutral']}</div><div class='stat-label'>Neutral</div></div>", unsafe_allow_html=True)
            colS3.markdown(f"<div class='stat-card blue'><div class='stat-number'>{sentiment_result['negative']}</div><div class='stat-label'>Negative</div></div>", unsafe_allow_html=True)
            colS4.markdown(f"<div class='stat-card purple'><div class='stat-number'>{sentiment_result['compound']}</div><div class='stat-label'>Compound Score</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='reduce-card'>Overall Sentiment: <b>{sentiment_result['sentiment']}</b></div>", unsafe_allow_html=True)
            
            if abs(sentiment_result["compound"]) < 0.05:
                st.info("ℹ Sentiment confidence is low (near neutral).")

            # STORE FOR CSV + LDA
            download_list.append({
                "name": details['name'],
                "cleaned_text": result["processed_text"],
                "sentiment": sentiment_result["sentiment"],
                "compound_score": sentiment_result["compound"]
            })

        if not download_list:
            st.warning("No data available for sentiment summary.")
            return

        # DOWNLOAD CSV
        df = pd.DataFrame(download_list)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="💾 Download Cleaned Text CSV", data=csv, file_name="cleaned_output.csv", mime="text/csv", use_container_width=True)
        st.success("✔ Analysis Completed successfully!")

        # LDA TOPIC MODELING
        st.markdown("## 🧠 Topic Modeling (LDA)")
        processed_texts = [item["cleaned_text"] for item in download_list if item.get("cleaned_text")]

        if len(processed_texts) >= 2:
            lda_topics = lda_topic_model(processed_texts, num_topics=5)

            st.session_state.lda_topics = lda_topics

            st.markdown("### 📝 Topic Coherence Check")
            for topic in lda_topics:
                words = topic['words'].split(", ")
                if any(words.count(word) > 1 for word in words):
                    st.warning(f"⚠ Topic '{topic['topic']}' may have low coherence: repeated words.")
                st.markdown(f"**{topic['topic']}**: {topic['words']}")
        else:
            st.warning("⚠ Upload at least 2 documents for topic modeling.")

        st.success("✔ Topic Modeling completed successfully!")

        # TOPIC + SENTIMENT SUMMARY
        st.markdown("## 🔗 Topic + Sentiment Summary")
        avg_sentiment = sum(item["compound_score"] for item in download_list) / len(download_list)
        st.session_state.overall_sentiment = (
            "Positive 😊" if avg_sentiment >= 0.05 else
            "Negative 😠" if avg_sentiment <= -0.05 else
            "Neutral 😐"
        )
        st.markdown(f"<div class='reduce-card'>Overall Dataset Sentiment: <b>{st.session_state.overall_sentiment}</b></div>", unsafe_allow_html=True)

        # SENTIMENT DISTRIBUTION
        pos_count = sum(1 for item in download_list if item["compound_score"] > 0.05)
        neg_count = sum(1 for item in download_list if item["compound_score"] < -0.05)
        neu_count = sum(1 for item in download_list if -0.05 <= item["compound_score"] <= 0.05)
        total_docs = len(download_list)
        st.markdown(f"<div class='reduce-card'>📊 Sentiment Distribution: Positive: {pos_count} ({round(pos_count/total_docs*100,1)}%), Neutral: {neu_count} ({round(neu_count/total_docs*100,1)}%), Negative: {neg_count} ({round(neg_count/total_docs*100,1)}%)</div>", unsafe_allow_html=True)

        # SENTIMENT VS TOPICS VALIDATION
        st.markdown("### 🔄 Sentiment vs Topics Validation")
        for item in download_list:
            text = item["cleaned_text"]
            sentiment = item["sentiment"]
            warning_flag = False
            for topic in lda_topics if len(processed_texts) >= 2 else []:
                for word in topic["words"].split(", "):
                    if word.lower() in text.lower():
                        if sentiment == "Positive 😊" and word.lower() in ["bad","problem","fail","error"]:
                            warning_flag = True
                        if sentiment == "Negative 😠" and word.lower() in ["good","success","win","happy"]:
                            warning_flag = True
            if warning_flag:
                st.info(f"ℹ Check document '{item['name']}': Sentiment may conflict with topic keywords.")

        # SENTIMENT PER TOPIC VISUALIZATION
        topic_sentiments = []
        for topic in lda_topics if len(processed_texts) >= 2 else []:
            relevant_docs = [item["compound_score"] for item in download_list if any(word in item["cleaned_text"] for word in topic["words"].split(", "))]
            avg_score = sum(relevant_docs)/len(relevant_docs) if relevant_docs else 0
            topic_sentiments.append({"topic": topic["topic"], "avg_sentiment": avg_score})

        if topic_sentiments:
            df_topic_sent = pd.DataFrame(topic_sentiments)
            st.bar_chart(df_topic_sent.set_index("topic"))

        #INSIGHTS & SUMMARIZATION
        st.markdown("## 🧾Automatic Summarization & Insights")
        combined_text = " ".join(processed_texts)

        #Extractive Summary
        st.markdown("### ✂ Extractive Summary")
        extractive = extractive_summary(combined_text)
        st.session_state.extractive = extractive
        st.markdown(f"<div class='text-box'>{extractive}</div>", unsafe_allow_html=True)

        #Abstractive Summary
        st.markdown("### 🧠 Abstractive Summary")
        try:
            abstractive = abstractive_summary(combined_text[:1000])
            st.session_state.abstractive = abstractive
            st.markdown(f"<div class='text-box'>{abstractive}</div>", unsafe_allow_html=True)
        except Exception:
            st.warning("⚠ Abstractive summarization failed due to model limitations.")

        #Insights Generation
        st.markdown("### 💡 Generated Insights")
        insights = generate_insights(lda_topics, st.session_state.overall_sentiment)

        for insight in insights:
            st.markdown(f"✔ {insight}")

        
        #VISUALIZATION DASHBOARD

        st.markdown("## 📊 Visualization Dashboard")

        #WORD CLOUD
        st.markdown("### ☁ Word Cloud")
        show_wordcloud(combined_text)

        #SENTIMENT DISTRIBUTION
        st.markdown("### 📈 Sentiment Distribution Chart")
        show_sentiment_chart(download_list)

    #REPORT GENERATION
    import os

    st.markdown("## 📄 Generate Analysis Report")

    report_file = "NarrativeNexus_Report.pdf"

    if st.button("📥 Generate PDF Report"):

        if st.session_state.overall_sentiment is None:
            st.error("❌ Please analyze text before generating the report.")
        else:
            generate_pdf_report(
                report_file,
                st.session_state.overall_sentiment,
                st.session_state.lda_topics,
                st.session_state.extractive,
                st.session_state.abstractive
            )
            st.success("✔ Report generated successfully!")

    #Show download button ONLY if file exists
    if os.path.exists(report_file):
        with open(report_file, "rb") as f:
            st.download_button(
                label="⬇ Download Report",
                data=f,
                file_name=report_file,
                mime="application/pdf"
            )




