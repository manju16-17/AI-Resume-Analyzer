import re

SKILLS = [
    "python", "java", "c", "c++", "sql", "mysql", "mongodb",
    "machine learning", "deep learning", "artificial intelligence",
    "nlp", "natural language processing", "computer vision",
    "tensorflow", "pytorch", "scikit-learn", "sklearn",
    "pandas", "numpy", "matplotlib", "seaborn", "opencv",
    "streamlit", "flask", "django", "html", "css", "javascript",
    "react", "git", "github", "docker", "aws", "azure",
    "power bi", "tableau", "excel", "data analysis", "data science"
]

def normalize(text):
    return re.sub(r"\s+", " ", text.lower())

def find_skills(text):
    clean = normalize(text)
    found = []
    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, clean):
            found.append(skill.title() if skill != "c++" else "C++")
    return sorted(set(found))

def analyze_resume(text):
    word_count = len(re.findall(r"\b[\w+#.-]+\b", text))
    skills = find_skills(text)

    # Simple transparent educational scoring model.
    score = 30
    score += min(len(skills) * 3, 45)
    if 250 <= word_count <= 900:
        score += 15
    elif word_count >= 150:
        score += 8

    section_terms = ["education", "experience", "project", "skills", "contact"]
    section_count = sum(term in normalize(text) for term in section_terms)
    score += min(section_count * 2, 10)
    score = min(score, 100)

    suggestions = []
    clean = normalize(text)
    if "summary" not in clean and "objective" not in clean:
        suggestions.append("Add a short professional summary or career objective.")
    if "project" not in clean:
        suggestions.append("Add 2–3 relevant projects with technologies and measurable outcomes.")
    if "experience" not in clean:
        suggestions.append("Include internship, training, freelance, or relevant experience if available.")
    if len(skills) < 8:
        suggestions.append("Add relevant technical skills that you genuinely know.")
    if word_count < 250:
        suggestions.append("Your resume appears short; add useful project, education, and achievement details.")
    if not suggestions:
        suggestions.append("Good structure detected. Tailor keywords and achievements to each job description.")

    return {
        "score": score,
        "skills": skills,
        "word_count": word_count,
        "suggestions": suggestions
    }
