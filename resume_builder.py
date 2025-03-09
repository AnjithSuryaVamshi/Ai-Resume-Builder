import streamlit as st
import google.generativeai as genai
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


# Function to generate resume text using AI
def generate_resume(name, skills, experience, education, projects):
    prompt = f"""
    Generate a professional resume with proper sections, headings, and formatting:

    Name: {name}
    Skills: {skills}
    Experience: {experience}
    Education: {education}
    Projects: {projects}

    - Use structured sections with bold headings.
    - Ensure clear spacing and indentation for better readability.
    - Keep the tone formal and professional.
    """

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    return response.text if response else "Error generating resume."

# Function to create a well-formatted PDF
def create_pdf(resume_text, filename, name):
    pdf_path = f"./{filename}"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles for a professional look
    title_style = ParagraphStyle(
        "Title",
        fontSize=18,
        leading=22,
        spaceAfter=12,
        alignment=1,  # Center text
        textColor=colors.darkblue,
        fontName="Helvetica-Bold"
    )

    section_header = ParagraphStyle(
        "Header",
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.black,
        fontName="Helvetica-Bold"
    )

    content_style = ParagraphStyle(
        "Content",
        fontSize=12,
        leading=15,
        spaceAfter=8,
        textColor=colors.black,
        fontName="Helvetica"
    )

    # Parse resume text into sections
    sections = resume_text.split("\n")
    elements = []

    # Add Name as Title
    elements.append(Paragraph(name.upper(), title_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Format the resume text properly
    for section in sections:
        if section.strip():  # Skip empty lines
            if ":" in section:  # Heading detection
                elements.append(Paragraph(section, section_header))
            else:
                elements.append(Paragraph(section, content_style))

    doc.build(elements)
    return pdf_path

# Streamlit Web App UI
st.title("📄 AI Resume Generator")
st.write("Generate a professional resume with AI and download it as a PDF!")

name = st.text_input("Enter your Name")
skills = st.text_area("Enter your Skills (comma-separated)")
experience = st.text_area("Enter your Work Experience")
education = st.text_area("Enter your Education Details")
projects = st.text_area("Enter your Projects")

if st.button("Generate Resume"):
    if name and skills and experience and education and projects:
        resume_text = generate_resume(name, skills, experience, education, projects)

        # Save as PDF with improved formatting
        pdf_filename = f"{name}_Resume.pdf"
        pdf_path = create_pdf(resume_text, pdf_filename, name)

        # Provide download button
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(label="📄 Download Resume PDF", 
                               data=pdf_file, 
                               file_name=pdf_filename, 
                               mime="application/pdf")
        
        st.success("Resume generated successfully! 🎉")
    else:
        st.warning("Please fill all the details!")
