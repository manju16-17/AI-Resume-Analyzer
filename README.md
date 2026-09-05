# 📄 AI Resume Analyzer

An easy **Artificial Intelligence / Machine Learning** project built with Python and Streamlit.

The application reads a resume PDF, detects common technical skills, calculates a transparent resume score, gives improvement suggestions, and optionally compares the resume against a job description.

## 🚀 Features

- Upload a resume in PDF format
- Extract resume text using `pdfplumber`
- Detect technical skills using NLP-style keyword matching
- Generate a resume score out of 100
- Count words and inspect basic resume sections
- Give personalized improvement suggestions
- Compare a resume with a job description
- Calculate a job-match score using **TF-IDF + cosine similarity**
- Simple Streamlit interface

## 🛠️ Technologies

- Python
- Streamlit
- Scikit-learn
- pdfplumber
- Regular Expressions
- NLP / Text Processing
- TF-IDF
- Cosine Similarity

## 📁 Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── resume_parser.py
├── analyzer.py
├── matcher.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## ▶️ How to Run

### 1. Install Python

Use Python 3.10 or newer.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
streamlit run app.py
```

The browser will open the local Streamlit application.

## 🧠 How It Works

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Text Cleaning
    ↓
Skill Detection + Resume Analysis
    ↓
Resume Score + Suggestions
    ↓
Optional Job Description
    ↓
TF-IDF + Cosine Similarity
    ↓
Job Match Score
```

## 📊 Scoring Logic

The educational scoring model considers:

- Number of detected skills
- Resume word count
- Presence of basic sections such as Education, Experience, Projects, Skills and Contact
- Resume-to-job-description similarity when a job description is supplied

The score is intended for demonstration and learning, not professional recruitment decisions.

## 🎓 Academic Use

This project is suitable for a beginner/intermediate AIML portfolio and can be extended with:

- Named Entity Recognition
- BERT or sentence-transformer embeddings
- LLM-based resume feedback
- More advanced skill extraction
- Database storage
- Login system
- Resume ranking
- Deployment on Streamlit Community Cloud

## 👨‍💻 Author

**Manjunath N**
