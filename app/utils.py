import re
import spacy
import pdfplumber
from docx import Document
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file) -> str:
    try:
        file.seek(0)
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"PDF extraction error: {e}")
        return ""

def extract_text_from_docx(file) -> str:
    try:
        file.seek(0)
        doc = Document(file)
        full_text = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n".join(full_text)
    except Exception as e:
        print(f"DOCX extraction error: {e}")
        return ""

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_email(text: str) -> str:
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Email not found"

def extract_name(text: str) -> str:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    for line in lines[:3]:
        
        if 2 <= len(line.split()) <= 5 and sum(c.isalpha() for c in line) / max(len(line),1) > 0.7:
            return line
    
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Name not found"

def extract_skills(text: str) -> List[str]:
    skill_keywords = ['python', 'java', 'sql', 'excel', 'tableau', 'machine learning',
                      'deep learning', 'nlp', 'pandas', 'numpy', 'c++', 'aws', 'azure']
    text_lower = text.lower()
    found_skills = [skill for skill in skill_keywords if skill in text_lower]
    return found_skills or ["Relevant skills not found"]

def extract_experience(text: str) -> str:
    experience_keywords = ["experience", "worked", "employment", "job", "internship", "role"]
    sentences = text.split('.')
    experience = [sent.strip() for sent in sentences if any(word in sent.lower() for word in experience_keywords)]
    return '. '.join(experience[:3]) if experience else "Experience details not found"

def parse_resume(text: str) -> Dict:
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Skills": extract_skills(text),
        "Experience": extract_experience(text)
    }

def compute_similarity(job_desc: str, resumes: List[str]) -> List[Dict]:
    
    pass

