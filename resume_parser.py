import pdfplumber

def extract_text_from_pdf(file):
    """Extract text from all readable pages of an uploaded PDF."""
    text_parts = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return "\n".join(text_parts)
