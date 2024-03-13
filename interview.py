# import streamlit as st
# import json
# from streamlit_lottie import st_lottie
# from streamlit_option_menu import option_menu
# from streamlit.components.v1 import html
# import streamlit as st
# import os
# import shutil
# import uuid
# from pydub import AudioSegment
# from st_audiorec import st_audiorec
# from utils import (
#     extract_resume_information,
#     get_system_prompt,
#     transcribe_audio,
#     get_chat_response,
#     convert_text_to_audio,
# )

# session_state = st.session_state

# def get_started():
#     session_id = str(uuid.uuid4())
#     return session_id


# def save_final_system_prompt():
#     application_role = ""
#     job_description = ""
#     resume_information = ""

#     user_data_folder = f"user_data/{session_state['session_id']}"
#     if os.path.exists(f"{user_data_folder}/role.txt"):
#         with open(f"{user_data_folder}/role.txt", "r") as file:
#             application_role = file.read()

#     if os.path.exists(f"{user_data_folder}/job_requirements.txt"):
#         with open(f"{user_data_folder}/job_requirements.txt", "r") as file:
#             job_description = file.read()

#     if os.path.exists(f"{user_data_folder}/resume.txt"):
#         with open(f"{user_data_folder}/resume.txt", "r") as file:
#             resume_information = file.read()

#     final_system_prompt = get_system_prompt(
#         application_role, job_description, resume_information
#     )
#     with open(f"{user_data_folder}/system_prompt.txt", "w") as f:
#         f.write(final_system_prompt)


# def conduct_interview():
#     user_data_folder = f"user_data/{session_state['session_id']}"

#     audio_path = f"{user_data_folder}/uploads/output_data.wav"
#     user_message = transcribe_audio(audio_path)

#     # Get chat response
#     system_prompt = ""
#     if os.path.exists(f"{user_data_folder}/system_prompt.txt"):
#         with open(f"{user_data_folder}/system_prompt.txt", "r") as file:
#             system_prompt = file.read()

#     database_path = f"{user_data_folder}/database.json"
#     chat_response = get_chat_response(user_message, database_path, system_prompt)
#     # chat_response = "Hey, how are you??"
#     gpt_audio_path = f"{user_data_folder}/uploads/gpt_audio.wav"
#     convert_text_to_audio(chat_response, gpt_audio_path)

#     audio_file = open(gpt_audio_path, "rb")
#     audio_bytes = audio_file.read()

#     st.audio(audio_bytes, format="audio/wav")


# def ai_interviewer_page():
#     if "interview_started" not in st.session_state:
#         st.session_state.interview_started = False

#     if "session_id" not in session_state:
#         st.title("AI Interviewer App")
#         st.write("Welcome to the AI-powered interview experience!")
#         if st.button("Get Started"):
#             session_id = get_started()  # Extract the session ID from the response
#             session_state[
#                 "session_id"
#             ] = session_id  # Store the session ID in session state
#             st.experimental_rerun()

#     # Entry page
#     elif not st.session_state.interview_started:
#         if not os.path.exists(f"user_data/{session_state['session_id']}"):
#             os.makedirs(f"user_data/{session_state['session_id']}")
#         user_data_folder = f"user_data/{session_state['session_id']}"

#         st.title("Enter Role and Skills")
#         role = st.selectbox(
#             "Select Role",
#             ["Software Engineer", "ML Engineer", "React Engineer", "Other"],
#         )
#         skills = st.multiselect(
#             "Select Skills", ["C++", "Java", "Python", "React", "TensorFlow"]
#         )
#         job_requirements = st.text_area("Job Requirements:")
#         resume = st.file_uploader("Resume (optional):")

#         user_data_folder = f"user_data/{session_state['session_id']}"
#         with open(f"{user_data_folder}/role.txt", "w") as f:
#             f.write(role)
#         with open(f"{user_data_folder}/skills.txt", "w") as f:
#             f.write("\n".join(skills))
#         with open(f"{user_data_folder}/job_requirements.txt", "w") as f:
#             f.write(job_requirements)
#         if resume is not None:
#             resume_text = extract_resume_information(resume)
#             print(resume_text)
#             with open(f"{user_data_folder}/resume.txt", "w", encoding="utf-8") as f:
#                 f.write(resume_text)

#         st.write("Role and skills saved successfully!")

#         if st.button("Start interview"):
#             st.session_state.interview_started = True
#             save_final_system_prompt()
#             with open(f"{user_data_folder}/database.json", "w") as json_file:
#                 pass
#             st.experimental_rerun()

#     else:
#         st.title("Welcome to your Interview")
#         wav_audio_data = st_audiorec()
#         user_data_folder = f"user_data/{session_state['session_id']}"

#         if wav_audio_data is not None:
#             # st.audio(wav_audio_data, format='audio/wav')
#             print(type(wav_audio_data))
#             audio_segment = AudioSegment(
#                 wav_audio_data,
#             )

#             ###
#             ### conduct interview

#             if not os.path.exists(f"{user_data_folder}/uploads"):
#                 os.makedirs(f"{user_data_folder}/uploads")
#             audio_segment.export(
#                 f"{user_data_folder}/uploads/output_data.wav", format="wav"
#             )

#             conduct_interview()
#             # st.audio(wav_audio_data, format='audio/wav')

#         if st.button("Exit Session"):
#             user_data_folder = f"user_data/{session_state['session_id']}"
#             if os.path.exists(user_data_folder):
#                 shutil.rmtree(user_data_folder)  # Delete the entire user data folder
#         # Proceed to the interview page (code not shown)


import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
import streamlit as st
import os
import shutil
import uuid
from pydub import AudioSegment
from st_audiorec import st_audiorec
from utils import (
    extract_resume_information,
    get_system_prompt,
    transcribe_audio,
    get_chat_response,
    convert_text_to_audio,
    generate_feedback,
)
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import mediapipe as mp
from audiorecorder import audiorecorder
import io

FRAME_SKIP = 30
frame_count = 0
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh

pose = mp_pose.Pose()
face_mesh = mp_face_mesh.FaceMesh()

facial_scores = []
session_state = st.session_state

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()


def calculate_average_score():
    if facial_scores:
        return sum(facial_scores[-1000:]) / len(facial_scores[-1000:])
    return 0


def provide_interview_review():
    average_score = calculate_average_score()
    threshold = 3.5
    if average_score > threshold:
        return "Positive facial expressions detected during the interview."
    else:
        return "Facial expressions could be more engaging."


SMILE_THRESHOLD = 0.03
OPEN_MOUTH_THRESHOLD = 0.02
SMILE_WEIGHT = 50
OPEN_MOUTH_PENALTY_WEIGHT = 70


def calculate_facial_expression_score(face_landmarks):
    try:
        NOSE_TIP_INDEX = 1
        MOUTH_LEFT_INDEX = 78
        MOUTH_RIGHT_INDEX = 308
        UPPER_LIP_TOP_INDEX = 13
        LOWER_LIP_BOTTOM_INDEX = 14

        nose_tip = face_landmarks.landmark[NOSE_TIP_INDEX]
        mouth_left = face_landmarks.landmark[MOUTH_LEFT_INDEX]
        mouth_right = face_landmarks.landmark[MOUTH_RIGHT_INDEX]
        upper_lip_top = face_landmarks.landmark[UPPER_LIP_TOP_INDEX]
        lower_lip_bottom = face_landmarks.landmark[LOWER_LIP_BOTTOM_INDEX]

        mouth_left_x = mouth_left.x - nose_tip.x
        mouth_right_x = mouth_right.x - nose_tip.x
        upper_lip_top_y = upper_lip_top.y - nose_tip.y
        lower_lip_bottom_y = lower_lip_bottom.y - nose_tip.y

        horizontal_mouth_stretch = abs(mouth_left_x - mouth_right_x)
        vertical_mouth_opening = abs(upper_lip_top_y - lower_lip_bottom_y)

        smile_score = (
            max(0, (horizontal_mouth_stretch - SMILE_THRESHOLD) * SMILE_WEIGHT)
            if horizontal_mouth_stretch > SMILE_THRESHOLD
            else 0
        )
        open_mouth_penalty = (
            max(
                0,
                (vertical_mouth_opening - OPEN_MOUTH_THRESHOLD)
                * OPEN_MOUTH_PENALTY_WEIGHT,
            )
            if vertical_mouth_opening > OPEN_MOUTH_THRESHOLD
            else 0
        )

        return max(0, smile_score - open_mouth_penalty)
    except Exception as e:
        print("Error in calculate_facial_expression_score:", e)
        return 0


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        global facial_scores
        try:
            img = frame.to_ndarray(format="bgr24")
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            face_results = face_mesh.process(img_rgb)

            if face_results.multi_face_landmarks:
                for face_landmarks in face_results.multi_face_landmarks:
                    facial_expression_score = calculate_facial_expression_score(
                        face_landmarks
                    )
                    facial_scores.append(facial_expression_score)
            print("Average score:", calculate_average_score())
            return img

        except Exception as e:
            print("Error in transform method:", e)
            return img


def get_started():
    session_id = str(uuid.uuid4())
    return session_id


def save_final_system_prompt():
    application_role = ""
    job_description = ""
    resume_information = ""

    user_data_folder = f"user_data/{session_state['session_id']}"
    if os.path.exists(f"{user_data_folder}/role.txt"):
        with open(f"{user_data_folder}/role.txt", "r") as file:
            application_role = file.read()

    if os.path.exists(f"{user_data_folder}/job_requirements.txt"):
        with open(f"{user_data_folder}/job_requirements.txt", "r") as file:
            job_description = file.read()

    if os.path.exists(f"{user_data_folder}/resume.txt"):
        with open(f"{user_data_folder}/resume.txt", "r") as file:
            resume_information = file.read()

    final_system_prompt = get_system_prompt(
        application_role, job_description, resume_information
    )
    with open(f"{user_data_folder}/system_prompt.txt", "w") as f:
        f.write(final_system_prompt)


def conduct_interview():
    user_data_folder = f"user_data/{session_state['session_id']}"

    audio_path = f"{user_data_folder}/uploads/output_data.wav"
    user_message = transcribe_audio(audio_path)

    # Get chat response
    system_prompt = ""
    if os.path.exists(f"{user_data_folder}/system_prompt.txt"):
        with open(f"{user_data_folder}/system_prompt.txt", "r") as file:
            system_prompt = file.read()

    database_path = f"{user_data_folder}/database.json"
    chat_response = get_chat_response(user_message, database_path, system_prompt)
    # chat_response = "Hey, how are you??"
    gpt_audio_path = f"{user_data_folder}/uploads/gpt_audio.wav"
    convert_text_to_audio(chat_response, gpt_audio_path)

    audio_file = open(gpt_audio_path, "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/wav")

def get_feedback():
    user_data_folder = f"user_data/{session_state['session_id']}"
    database_path = f"{user_data_folder}/database.json"

    feedback = generate_feedback(database_path)
    return feedback

def ai_interviewer_page():
    if st.button("Show Last 10 Facial Expression Scores"):
        if "facial_scores" in globals() and facial_scores:
            st.write(facial_scores[-10:])
        else:
            st.write("No facial scores available.")

    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    if 'end_interview' not in st.session_state:
        st.session_state.end_interview = False

    if "session_id" not in session_state:
        st.title("AI Interviewer App")
        st.write("Welcome to the AI-powered interview experience!")
        if st.button("Get Started"):
            session_id = get_started()  # Extract the session ID from the response
            session_state[
                "session_id"
            ] = session_id  # Store the session ID in session state
            st.experimental_rerun()

    # Entry page
    elif not st.session_state.interview_started:
        if not os.path.exists(f"user_data/{session_state['session_id']}"):
            os.makedirs(f"user_data/{session_state['session_id']}")
        user_data_folder = f"user_data/{session_state['session_id']}"

        st.title("Enter Role and Skills")
        role = st.selectbox(
            "Select Role",
            ["Software Engineer", "ML Engineer", "React Engineer", "Other"],
        )
        skills = st.multiselect(
            "Select Skills", ["C++", "Java", "Python", "React", "TensorFlow"]
        )
        job_requirements = st.text_area("Job Requirements:")
        resume = st.file_uploader("Resume (optional):")

        user_data_folder = f"user_data/{session_state['session_id']}"
        with open(f"{user_data_folder}/role.txt", "w") as f:
            f.write(role)
        with open(f"{user_data_folder}/skills.txt", "w") as f:
            f.write("\n".join(skills))
        with open(f"{user_data_folder}/job_requirements.txt", "w") as f:
            f.write(job_requirements)
        if resume is not None:
            resume_text = extract_resume_information(resume)
            print(resume_text)
            with open(f"{user_data_folder}/resume.txt", "w", encoding="utf-8") as f:
                f.write(resume_text)

        st.write("Role and skills saved successfully!")

        if st.button("Start interview"):
            st.session_state.interview_started = True
            save_final_system_prompt()
            with open(f"{user_data_folder}/database.json", "w") as json_file:
                pass
            st.experimental_rerun()

    elif not st.session_state.end_interview:

        if st.session_state.end_interview:
            st.experimental_rerun()
        else:
            st.title("Welcome to your Interview")

            st.subheader("Video Stream")
            webrtc_streamer(key="camera_score", video_processor_factory=VideoTransformer)

            # wav_audio_data = st_audiorec()
            # user_data_folder = f"user_data/{session_state['session_id']}"

            # if wav_audio_data is not None:
            #     audio_segment = AudioSegment(wav_audio_data)
            #     if not os.path.exists(f"{user_data_folder}/uploads"):
            #         os.makedirs(f"{user_data_folder}/uploads")
            #     audio_segment.export(
            #         f"{user_data_folder}/uploads/output_data.wav", format="wav"
            #     )
            #     conduct_interview()
            wav_audio_data = audiorecorder(
                "Muted. Click to Start", "Unmuted. Click to Stop"
            )

            user_data_folder = f"user_data/{session_state['session_id']}"

            if wav_audio_data is not None and wav_audio_data.duration_seconds > 0.1:
                # audio_segment = AudioSegment(wav_audio_data)
                if not os.path.exists(f"{user_data_folder}/uploads"):
                    os.makedirs(f"{user_data_folder}/uploads")
                wav_audio_data.export(
                    f"{user_data_folder}/uploads/output_data.wav", format="wav"
                )
                conduct_interview()
                wav_audio_data = None

            if st.button("End Interview"):
                wav_audio_data = None
                st.session_state.end_interview = True
                st.experimental_rerun()
    else:
        feedback = get_feedback()
        facial_review = provide_interview_review()
        feedback_values = feedback.split("\n")

        # Remove empty elements from the split result
        feedback_values = [value.strip() for value in feedback_values if value.strip()]

        #### displaying ##########################
        st.title("Feedback Metrics")
        st.subheader("Score")
        st.write(feedback_values[3])
        cols = st.columns(3)

        print(feedback_values)
        
        with cols[0]:
            st.subheader("Summarization")
            st.write(feedback_values[0])
        with cols[1]:
            st.subheader("Pros")
            st.write(feedback_values[1])
        with cols[2]:
            st.subheader("Cons")
            st.write(feedback_values[2])

        st.subheader("Sample Answers")
        st.write(feedback_values[4] if len(feedback_values) == 5 else "N/A")

        st.subheader("Facial Expression Feedback")
        st.write(facial_review)

        #### displaying end ######################

        if st.button("Exit Session"):
            st.session_state.interview_started = False
            st.session_state.end_interview = False
            # wav_audio_data = None

            user_data_folder = f"user_data/{session_state['session_id']}"
            if os.path.exists(user_data_folder):
                shutil.rmtree(user_data_folder)  # Delete the entire user data folder


            del session_state['session_id']
            st.experimental_rerun()

            # if st.button("Exit Session"):
            #     user_data_folder = f"user_data/{session_state['session_id']}"
            #     if os.path.exists(user_data_folder):
            #         shutil.rmtree(user_data_folder)
