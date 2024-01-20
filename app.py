# Application functionality requirements
"""
1. A field to put job description
2. Upload the PDF
3. Convert PDF to image ---> Processing ----> Google Gemini Pro
4. Prompt Templates 
"""

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import io
import base64
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_api_key"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:

        # Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # covert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type":"image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() #encode to base 64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file Uploaded")

## Streamlit App
st.set_page_config(page_title="Application Tracking System - Resume Checker")
st.header("Application Tracking System")
input_text=st.text_area("Job Description: ", key="imput")
uploaded_file=st.file_uploader("Upload your resumer (PDF)   ", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uplaoded Successfully")

submit1 = st.button("Tell me about the Resume")

submit2 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager with experience in the field of Data Science, Data Analyst, Full Stack web development, Big Data Engineering.
 Your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""


input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Data Analyst, Full Stack web development, Big Data Engineering,
 and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
