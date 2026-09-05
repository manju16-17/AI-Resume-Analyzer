import streamlit as st
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume
from matcher import calculate_match

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.caption("Analyze your resume, discover skills, and compare it with a job description.")

with st.sidebar:
    st.header("About")
    st.write("Upload a PDF resume and optionally paste a job description. "
             "The app uses NLP techniques to score the resume and estimate job matching.")
    st.info("This is an educational AIML project using TF-IDF, cosine similarity, and keyword extraction.")

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area(
    "Paste Job Description (optional)",
    height=180,
    placeholder="Example: We are looking for a Python developer with machine learning, SQL and NLP skills..."
)

if resume_file:
    try:
        resume_text = extract_text_from_pdf(resume_file)
        if not resume_text.strip():
            st.error("No readable text was found in the PDF.")
            st.stop()

        result = analyze_resume(resume_text)

        st.subheader("📊 Resume Overview")
        c1, c2, c3 = st.columns(3)
        c1.metric("Resume Score", f"{result['score']}/100")
        c2.metric("Skills Found", len(result["skills"]))
        c3.metric("Words", result["word_count"])

        st.progress(result["score"] / 100)

        st.subheader("🧠 Detected Skills")
        if result["skills"]:
            st.write(" • ".join(result["skills"]))
        else:
            st.warning("No skills detected from the built-in skill list.")

        st.subheader("💡 Suggestions")
        for suggestion in result["suggestions"]:
            st.write(f"• {suggestion}")

        if job_description.strip():
            match = calculate_match(resume_text, job_description)
            st.subheader("🎯 Job Match")
            m1, m2 = st.columns(2)
            m1.metric("Match Score", f"{match['score']}%")
            m2.metric("Matched Keywords", len(match["matched_keywords"]))
            st.progress(match["score"] / 100)

            st.write("**Matched keywords:** " + (", ".join(match["matched_keywords"]) or "None"))
            st.write("**Suggested keywords to consider:** " +
                     (", ".join(match["missing_keywords"]) or "None"))

        with st.expander("View extracted resume text"):
            st.text(resume_text[:12000])

    except Exception as e:
        st.error(f"Could not analyze the resume: {e}")
else:
    st.info("👆 Upload a PDF resume to start the analysis.")
