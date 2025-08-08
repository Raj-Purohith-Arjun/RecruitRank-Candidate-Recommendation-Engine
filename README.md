# RecruitRank-Candidate-Recommendation-Engine


An AI-powered web application that recommends the most relevant candidates for a given job description based on **semantic similarity**.  

---

## 📌 Overview

This application allows recruiters to:
- Paste a **Job Description**
- Upload multiple **Candidate Resumes** (`.pdf`, `.docx`, `.txt`)
- Automatically rank candidates based on **relevance** to the job
- View **AI-generated summaries** explaining why each candidate is a great fit

---

## 🚀 Features

✅ **Multi-format Resume Support** — PDF, DOCX, and TXT parsing  
✅ **Semantic Matching** — Finds relevance beyond exact keyword matching  
✅ **Top N Ranking** — Shows the top 5–10 candidates with similarity scores  
✅ **AI Candidate Summaries** — Personalized explanation of why they fit the role  
✅ **Streamlit UI** — Simple web-based interface for interaction  
✅ **Testable via Terminal** — CLI scripts for debugging and testing  

---

## 🛠 Tech Stack

**Frontend / Interface**
- [Streamlit](https://streamlit.io/) — Fast, interactive web app framework

**Natural Language Processing**
- [Sentence Transformers](https://www.sbert.net/) — `all-MiniLM-L6-v2` for embeddings
- [scikit-learn](https://scikit-learn.org/) — Cosine similarity computation
- [transformers](https://huggingface.co/transformers/) — Flan T5 Large

**File Parsing**
- [pdfplumber](https://github.com/jsvine/pdfplumber) — Extract text from PDFs
- [python-docx](https://python-docx.readthedocs.io/) — Extract text from Word docs

**Backend**
- Python 3.8+  
- Modular architecture with `app/` package for matching, summarization, and utilities

---

## 📂 Project Structure

```
CREngine/
│
├── main.py                # Streamlit app entry point
│
├── app/
│   ├── matching.py        # Embedding + similarity logic
│   ├── utils.py           # Resume file parsing
│   ├── summarizer.py      # AI summary generation
│   ├── __init__.py
│
├── requirements.txt       # Python dependencies
├── .gitignore
```

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/<your-username>/CREngine.git
cd CREngine
```

### **2️⃣ Create Virtual Environment**
```bash
python -m venv venv
```

### **3️⃣ Activate Virtual Environment**
- **Windows (PowerShell)**
```bash
venv\Scripts\activate
```
- **Mac/Linux**
```bash
source venv/bin/activate
```

### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Application

### **Streamlit Web App**
From the project root:
```bash
streamlit run main.py
```
The app will open in your browser (default: `http://localhost:8501`).

---

## 🧪 Running Matching Logic from Terminal

Test candidate ranking without UI:
```bash
python app/matching.py
```

Example output:
```
candidate1.txt: 0.8086
candidate3.txt: 0.6374
candidate2.txt: 0.2847
```

---

## 📦 Dependencies

Core libraries:
- `streamlit` — Interactive web interface
- `sentence-transformers` — Embedding generation
- `scikit-learn` — Similarity computation
- `pdfplumber` — PDF text extraction
- `python-docx` — DOCX text extraction
- `transformers` — AI-powered summarization

Full list is available in [`requirements.txt`](requirements.txt).

---

## 🔍 How It Works

1. **Input** — User pastes job description & uploads resumes.
2. **Text Extraction** — Resumes parsed into plain text.
3. **Embeddings Generation** — Both job & resumes converted to semantic vectors.
4. **Similarity Computation** — Cosine similarity measures closeness in meaning.
5. **Ranking** — Candidates sorted by relevance score.
6. **AI Summary** — Summarizer model explains why each candidate fits.

---

## 📌 Example Output

| Rank | Candidate Name | Score  | Summary |
|------|---------------|--------|---------|
| 1    | Jane Doe      | 0.81   | Jane has 5+ years in data science with expertise in Python, SQL, and ML model deployment, making her a strong match for the role. |
| 2    | John Smith    | 0.76   | John has a background in analytics, BI tools, and cloud computing, aligning well with the job requirements. |


---

## 🚀 Future Improvements (Free Enhancements)

- OCR support for scanned resumes  
- Named Entity Recognition for structured skill extraction  
- Advanced summarization with fine-tuned LLMs  
- Bulk resume processing in batches  
- Multi-job comparison & candidate database storage

---

## 📜 License

This project is for educational/demo purposes only.

---

## ✉️ Contact

Developed by **Raj Purohith Arjun, MS Data Science, Texas A&M University**  
📧 Email: rajpurohitharjun58@gmail.com
Linkedin: https://www.linkedin.com/in/raj-purohith-arjun-20a652200/
