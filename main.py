import streamlit as st
from app.utils import (
    extract_text_from_pdf,
    extract_text_from_docx,
    clean_text,
    parse_resume,
)
from app.summarizer import generate_summary  
from app.matching import match_candidates    


def main():
    st.title("RecruitRank: Candidate Recommendation Engine")

    job_description = st.text_area("Enter Job Description", height=150)

    uploaded_files = st.file_uploader(
        "Upload Candidate Resumes (PDF, DOCX, TXT)", 
        accept_multiple_files=True,
        type=['pdf', 'docx', 'txt']
    )

    if st.button("Find Matches"):
        if not job_description:
            st.error("Please enter a job description.")
            return
        if not uploaded_files:
            st.error("Please upload at least one resume.")
            return

        resumes_texts = []
        file_names = []
        parse_results = []

        for uploaded_file in uploaded_files:
            ext = uploaded_file.name.split('.')[-1].lower()
            try:
                if ext == 'pdf':
                    text = extract_text_from_pdf(uploaded_file)
                elif ext == 'docx':
                    text = extract_text_from_docx(uploaded_file)
                else:
                    # TXT or fallback
                    uploaded_file.seek(0)
                    text = uploaded_file.read().decode('utf-8', errors='ignore')
                text = clean_text(text)
            except Exception as e:
                st.warning(f"Failed to extract text from {uploaded_file.name}: {e}")
                continue

            if len(text) < 50:
                st.warning(f"Text extracted from {uploaded_file.name} is too short or invalid, skipping.")
                continue

            resumes_texts.append(text)
            file_names.append(uploaded_file.name)
            parse_results.append(parse_resume(text))

        if not resumes_texts:
            st.error("No valid resumes to process.")
            return

        
        resume_pairs = [(file_names[i], resumes_texts[i]) for i in range(len(resumes_texts))]

        
        matched_candidates = match_candidates(job_description, resume_pairs, top_n=5)

        st.header("Top Candidate Matches (Semantic Similarity)")

        for rank, match in enumerate(matched_candidates, 1):
            candidate_id = match['candidate_id']
            score = match['score']

            
            try:
                idx = file_names.index(candidate_id)
            except ValueError:
                idx = None

            if idx is not None:
                info = parse_results[idx]

                st.subheader(f"{rank}. {candidate_id} — Similarity Score: {score:.4f}")
                st.markdown(f"**Name:** {info.get('Name', 'N/A')}")
                st.markdown(f"**Email:** {info.get('Email', 'N/A')}")
                skills = info.get('Skills', [])
                if isinstance(skills, list):
                    skills_str = ', '.join(skills)
                else:
                    skills_str = str(skills)
                st.markdown(f"**Skills:** {skills_str if skills_str else 'Not found'}")

                
                ai_summary = generate_summary(resumes_texts[idx], job_description)
                st.markdown(f"**AI Summary:** {ai_summary}")
                st.markdown("---")

if __name__ == "__main__":
    main()
