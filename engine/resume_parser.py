import pdfplumber
from docx import Document
import re

class ResumeParser:

    def extract_pdf(self, file_path):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def extract_docx(self, file_path):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    def clean_text(self, text):
        # Remove special characters
        text = re.sub(r'[^A-Za-z0-9\n ]+', '', text)

        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text)

        return text.strip()

    def process(self, file_path):
        if file_path.endswith(".pdf"):
            raw = self.extract_pdf(file_path)
        elif file_path.endswith(".docx"):
            raw = self.extract_docx(file_path)
        else:
            return {"error": "Unsupported format"}

        clean = self.clean_text(raw)

        return {
            "raw_text": raw,
            "cleaned_text": clean
        }