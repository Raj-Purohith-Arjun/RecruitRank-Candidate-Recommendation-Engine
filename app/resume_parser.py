import os
import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_email(text):
    match = re.search(r"[\w.-]+@[\w.-]+", text)
    return match.group(0) if match else None


def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


def extract_skills(text, skill_keywords):
    skills_found = []
    text = text.lower()
    for skill in skill_keywords:
        if skill.lower() in text:
            skills_found.append(skill)
    return list(set(skills_found))


def extract_experience(text):
    
    exp_matches = re.findall(r"(\d+)\+?\s+(?:years|yrs)\s+experience", text.lower())
    if exp_matches:
        return max(map(int, exp_matches))
    return None


def parse_resume(text, skill_keywords):
    name = extract_name(text)
    email = extract_email(text)
    skills = extract_skills(text, skill_keywords)
    experience = extract_experience(text)

    return {
        "name": name,
        "email": email,
        "skills": skills,
        "experience": experience
    }


def parse_top_resumes(matched_resumes, skill_keywords, resume_dir):
    parsed_results = []

    for match in matched_resumes:
        file_name = match['file_name']
        score = match['score']
        file_path = os.path.join(resume_dir, file_name)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                resume_text = f.read()

            parsed_data = parse_resume(resume_text, skill_keywords)
            parsed_data['match_score'] = round(score, 2)
            parsed_data['file_name'] = file_name
            parsed_results.append(parsed_data)

        except Exception as e:
            parsed_results.append({
                "file_name": file_name,
                "error": str(e),
                "match_score": round(score, 2)
            })

    return parsed_results
