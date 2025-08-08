# app/keyword_extractor.py

from keybert import KeyBERT

kw_model = KeyBERT()

def extract_keywords(text, top_n=10):
    if not text:
        return []
    keywords = kw_model.extract_keywords(text, top_n=top_n, stop_words='english')
    return [kw for kw, _ in keywords]
