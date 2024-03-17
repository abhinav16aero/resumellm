import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Importing custom modules for different pages
# from interview import ai_interviewer_page
from resume import resume_enhancer_page

# Setting the page configuration
st.set_page_config(page_title="CareerCraft", layout="wide")


def load_lottiefile(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


lottie_file_path = "Welcome.json"
lottie_animation = load_lottiefile(lottie_file_path)

sidebar_lottie_path = "sidebar_animation.json"
sidebar_lottie_animation = load_lottiefile(sidebar_lottie_path)

with st.sidebar:
    st_lottie(sidebar_lottie_animation, height=200, key="sidebar_lottie")

    st.markdown("# Explore")
    page = st.radio(
        "Choose a Page", ["Welcome Page", "AI Interviewer", "Resume Enhancer"]
    )

    st.markdown("---")
    st.markdown("## Connect with Us")

    email_button_html = """
    <a href="mailto:contact@careercraft.com" target="_blank">
        <button style='background-color:#ff7f00; color:white; padding:10px 24px; border:none; cursor:pointer; border-radius:5px; margin:3px;'>
            🌐 Email
        </button>
    </a>
    """
    phone_button_html = """
    <a href="tel:+1234567890" target="_blank">
        <button style='background-color:#ff7f00; color:white; padding:10px 24px; border:none; cursor:pointer; border-radius:5px; margin:3px;'>
            📞 Phone
        </button>
    </a>
    """
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(email_button_html, unsafe_allow_html=True)
    with col2:
        st.markdown(phone_button_html, unsafe_allow_html=True)


def welcome_page():
    st_lottie(lottie_animation, height=300, key="welcome")

    st.title("Welcome to CareerCraft")
    st.markdown("## Enhance Your Career Prospects with AI")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("AI Interviewer")
        st.markdown(
            """
            - **Practice Makes Perfect**: Engage with our AI interviewer.
            - **Personalized Feedback**: Receive constructive feedback.
            - **Confidence Building**: Enhance your interview skills.
        """
        )
    with col2:
        st.subheader("Resume Enhancer")
        st.markdown(
            """
            - **Tailored Suggestions**: Improve your resume.
            - **Highlight Your Strengths**: Ensure your skills stand out.
            - **Beat the ATS**: Optimize for Applicant Tracking Systems.
        """
        )

    st.markdown("---")
    st.markdown("## Get Started")

    selected = option_menu(
        menu_title=None,
        options=["AI Interviewer", "Resume Enhancer"],
        icons=["cast", "cloud-upload"],
        default_index=0,
        orientation="horizontal",
    )

    if selected == "AI Interviewer":
        st.info(
            """
            📚 In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4096 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start by introducing yourself and enjoy!
        """
        )
    if selected == "Resume Enhancer":
        st.info(
            """
            📚 In this session, you'll receive suggestions to improve your resume.
            Note: The maximum length of your answer is 4096 tokens!
            - Each session will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Start by uploading your resume and get instant feedback!
        """
        )


if page == "Welcome Page":
    welcome_page()
# elif page == "AI Interviewer":
#     ai_interviewer_page()
elif page == "Resume Enhancer":
    resume_enhancer_page()
