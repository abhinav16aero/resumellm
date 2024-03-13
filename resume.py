# import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html

# import sys
# sys.path.append('/Users/sharmas/Downloads/Hack2024/spsp/sparkathon-ai-2k24/AI_hackathon/for_resume')
# print(sys.path)
import streamlit as st
import os
from werkzeug.utils import secure_filename
from for_resume.pdfToText import *
from for_resume.api import *
import markdown
import base64

class Messg:
    def __init__(self, text) -> None:
        self.text = text

def perform_ocr(pdf_path):
    return pdfToText(pdf_path).convertit()

def enhanceResume(resume_text, user_name ,target_job):
    enhanced_resume = f"{resume_text}"
    # user_message =  Messg(f"Enhanced this resume {enhanced_resume} which is  for {user_name} ,with the target job profile of {target_job}.")
    enhanced_resume,s,w = prompt.get_chat_response(enhanced_resume, user_name, target_job)
    return markdown.markdown(enhanced_resume), s, w

prompt = promptLLM()

def resume_enhancer_page():
    
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

    st.title("Resume Enhancer")

    user_name = st.text_input('Your Name:')
    target_job = st.text_input('Target Job Profile:')
    resume_file = st.file_uploader('Upload Resume (PDF, PNG, JPG, JPEG):', type=['pdf', 'png', 'jpg', 'jpeg'])

    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    if st.button('Enhance Resume'):
        if resume_file is not None:
            resume_path = os.path.join(UPLOAD_FOLDER, secure_filename(resume_file.name))
            with open(resume_path, 'wb') as f:
                f.write(resume_file.getvalue())

            resume_text = perform_ocr(resume_path)

            enhanced_resume, s, w = enhanceResume(resume_text, user_name, target_job)

            new_file_path = resume_path.split('/')[-1]
            makepdf(enhanced_resume, new_file_path)

            st.header('Enhanced Resume Result')
            st.markdown(f"**Strengths:** {s}")
            st.markdown(f"**Weaknesses:** {w}")
             # st.markdown(f"**User Name:** {user_name}")
            # st.markdown(f"**Original Resume:** {resume_text}")
            # st.markdown(f"**Enhanced Resume:** {enhanced_resume}")

            # Display the enhanced PDF using an iframe
            st.markdown(f"**Enhanced PDF:**")
            st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(os.path.join("downloads",f"enhanced_{new_file_path}"), "rb").read()).decode("utf-8")}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)
