# Application Tracking System - Resume Checker

## Overview

This Streamlit application serves as an Application Tracking System (ATS) for evaluating resumes against job descriptions. It utilizes the Google Gemini Pro API to generate responses based on predefined prompts.

## Features

1. **Job Description Input Field:**
   - Users can enter the job description in a text area.

2. **Resume Upload:**
   - Users can upload a resume in PDF format.

3. **PDF to Image Conversion:**
   - The application converts the uploaded PDF to an image using the pdf2image library.

4. **Google Gemini Pro Integration:**
   - The application interacts with Google Gemini Pro to generate responses based on user-inputted prompts, job description, and resume content.

5. **Prompt Templates:**
   - Two prompt templates are provided for professional evaluation and percentage match calculation.

6. **Buttons:**
   - Users can trigger two actions - "Tell me about the Resume" and "Percentage match."

## How to Run

1. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up a `.env` file:
   - Obtain a Google Gemini Pro API key and add it to the `.env` file.

3. Run the application:
   ```bash
   streamlit run your_script_name.py
   ```

## Usage

1. Enter the job description in the text area.

2. Upload a resume in PDF format.

3. Click on either "Tell me about the Resume" or "Percentage match" button to receive responses from Google Gemini Pro.

## Important Note

Ensure that the Google Gemini Pro API key is kept confidential and not shared publicly.

## Why Application Tracking System (ATS) is Useful

An Application Tracking System streamlines the hiring process by automating the collection, organization, and evaluation of resumes. Key benefits include:

- **Efficiency:** ATS eliminates manual sorting and enables quick resume screening.

- **Consistency:** It ensures a standardized evaluation process for all applicants.

- **Keyword Matching:** ATS can identify relevant keywords in resumes to match job requirements.

- **Centralized Storage:** All applicant data is stored in a centralized system, making it easy to manage.

- **Data-driven Decisions:** ATS provides insights and analytics for informed hiring decisions.

- **Collaboration:** It facilitates collaboration among hiring team members.

- **Compliance:** ATS helps in maintaining compliance with hiring regulations.
