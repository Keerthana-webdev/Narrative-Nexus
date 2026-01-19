import pandas as pd
import PyPDF2
from docx import Document

def get_file_details(file):
    return {
        "name": file.name,
        "type": file.type,
        "size_kb": round(len(file.getvalue()) / 1024, 2),
        "extension": file.name.split(".")[-1]
    }

def extract_text(file):
    try:
        if file.type == "text/plain":
            return file.read().decode("utf-8")
        
        elif file.type == "application/pdf":
            pdf = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
        
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(file)
            return "\n".join([p.text for p in doc.paragraphs])
        
        elif file.type == "text/csv":
            df = pd.read_csv(file)
            return " ".join(df.astype(str).values.flatten())
        
        else:
            return ""
    except Exception as e:
        return f"ERROR: {e}"
