from transformers import pipeline

summarizer = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_summary(resume_text: str, job_description: str) -> str:
    
    resume_snippet = resume_text[:1500].replace("\n", " ").strip()
    job_keywords = job_description[:400].replace("\n", " ").strip()

    prompt = (
        "You are an AI hiring assistant. Based ONLY on the candidate's resume, "
        "write 2-3 sentences summarizing their main skills, achievements, and experiences. "
        "Highlight the qualities that make them suitable for the job, but do not restate "
        "or copy any part of the job description.\n\n"
        f"RESUME:\n{resume_snippet}\n\n"
        f"JOB KEYWORDS (for context only): {job_keywords}\n\n"
        "CANDIDATE SUMMARY:"
    )

    try:
        outputs = summarizer(prompt, max_length=120, truncation=True)
        return outputs[0]["generated_text"].strip()
    except Exception as e:
        return f"Summary not available due to error: {e}"
