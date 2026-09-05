import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from analyzer import SKILLS

STOPWORDS = {
    "the","and","for","with","from","this","that","are","you","our","your",
    "will","have","has","using","use","looking","work","role","team","into",
    "who","their","they","job","years","experience","required","preferred"
}

def tokens(text):
    return set(
        w for w in re.findall(r"[a-zA-Z][a-zA-Z+#.-]{2,}", text.lower())
        if w not in STOPWORDS
    )

def calculate_match(resume, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform([resume, job_description])
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

    resume_tokens = tokens(resume)
    job_tokens = tokens(job_description)
    matched = sorted(resume_tokens & job_tokens)
    missing = sorted(job_tokens - resume_tokens)

    # Blend semantic TF-IDF similarity with keyword overlap.
    keyword_score = len(matched) / max(len(job_tokens), 1)
    score = round((similarity * 0.65 + keyword_score * 0.35) * 100)
    return {
        "score": min(score, 100),
        "matched_keywords": matched[:30],
        "missing_keywords": missing[:30]
    }
