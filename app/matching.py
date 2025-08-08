# matching.py
from typing import List, Tuple, Dict
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text: str, max_words: int = 200) -> List[str]:
    """
    Split text into chunks of approximately max_words words each.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

def embed_text(text: str) -> np.ndarray:
    """
    Encode text by chunking if too long and averaging embeddings.
    """
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)
    avg_embedding = np.mean(embeddings, axis=0)
    return avg_embedding

def match_candidates(
    job_description: str,
    resume_texts: List[Tuple[str, str]],  
    top_n: int = 10
) -> List[Dict]:
    """
    Match resumes to job description using semantic similarity with chunked embedding.
    """

    
    job_embedding = embed_text(job_description)

    results = []

    for candidate_id, resume_text in resume_texts:
        if not resume_text.strip():
            continue

        
        resume_embedding = embed_text(resume_text)

    
        similarity = cosine_similarity(
            [job_embedding],
            [resume_embedding]
        )[0][0]

        results.append({
            'candidate_id': candidate_id,
            'score': round(float(similarity), 4),
            'resume_text': resume_text,
            
        })

    
    results = sorted(results, key=lambda x: x['score'], reverse=True)

    return results[:top_n]
