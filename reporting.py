from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(
    filename,
    overall_sentiment,
    lda_topics,
    extractive_summary,
    abstractive_summary
):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "NarrativeNexus - Analysis Report")

    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Overall Sentiment:")
    y -= 20
    c.setFont("Helvetica", 11)
    c.drawString(60, y, overall_sentiment)

    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Topic Modeling Results:")
    y -= 20

    c.setFont("Helvetica", 10)
    for topic in lda_topics:
        c.drawString(60, y, f"{topic['topic']}: {topic['words']}")
        y -= 15
        if y < 80:
            c.showPage()
            y = height - 40

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Extractive Summary:")
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, extractive_summary[:500])

    y -= 60
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Abstractive Summary:")
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, abstractive_summary[:500])

    c.save()
