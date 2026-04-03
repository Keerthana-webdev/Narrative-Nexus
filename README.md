## AI Narrative Nexus - Dynamic Text Analysis Platform
NarrativeNexus is an end-to-end NLP-powered web application built using Streamlit that performs advanced text analysis on multiple document formats. It integrates text preprocessing, sentiment analysis, topic modeling, summarization, visualization, and automated reporting into a single interactive platform.

---

### Tech Stack
- Frontend/UI: Streamlit
- Backend: Python
- NLP Libraries: NLTK, Scikit-learn
- Deep Learning: Hugging Face Transformers
- Visualization: Matplotlib, WordCloud
- Reporting: ReportLab
- Data Handling: Pandas

---

### Project Architecture
```bash
NarrativeNexus/
│
├── app.py                  # Entry point
├── streamlit_ui.py         # UI rendering logic
├── collection.py           # File handling & text extraction
├── preprocessing.py        # Text preprocessing pipeline
├── cleaning.py             # Regex-based cleaning
├── sentiment.py            # Sentiment analysis (VADER)
├── model.py                # LDA topic modeling
├── summarization.py        # Extractive + Abstractive summarization
├── insights.py             # Insight generation
├── visualization.py        # Word cloud & charts
├── reporting.py            # PDF report generation
├── css.py                  # Custom UI styling
└── requirements.txt
```
---

### Workflow Pipeline
```bash
Input (Files/Text)
        ↓
Text Extraction
        ↓
Preprocessing (Clean → Tokenize → Lemmatize)
        ↓
Sentiment Analysis
        ↓
Topic Modeling (LDA)
        ↓
Summarization (Extractive + Abstractive)
        ↓
Insight Generation
        ↓
Visualization Dashboard
        ↓
Report Generation (PDF + CSV)
```
---

### Installation & Setup
1️⃣ Clone Repository

git clone https://github.com/Keerthana-webdev/Narrative-Nexus.git

cd NarrativeNexus

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Application

streamlit run app.py

---

### Usage
1. Upload files or paste text
2. Click "🚀 Analyze Text"
3. Explore:
   - Text statistics
   - Sentiment results
   - Topics
   - Summaries
   - Insights & visualizations
4. Download:
   - CSV output
   - PDF report

---

### Output Samples
- ✔ Sentiment classification with scores
- ✔ Topic keywords (LDA)
- ✔ Extractive & abstractive summaries
- ✔ Word cloud visualization
- ✔ Sentiment distribution charts
- ✔ Auto-generated PDF report

---

### Future Enhancements
- Real-time API integration
- Multi-language support
- Named Entity Recognition (NER)
- Keyword trend analysis

---

### Conclusion
NarrativeNexus demonstrates a complete NLP pipeline by combining classical machine learning and modern deep learning techniques into a scalable, user-friendly platform. It bridges the gap between raw text data and actionable insights.

---

### Author

#### Keerthana S

