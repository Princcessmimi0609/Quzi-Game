import streamlit as st
from PIL import Image, ImageFilter
import time

# Load an image
image_path = "C:/Users/princ/Desktop/Python Projects/Quiz Game/images/moon.jpg"  # Replace with your image path
image = Image.open(image_path)

# Display the original image
st.image(image, caption="Original Image", use_column_width=True)

# Initialize the session state variables
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'timer_start' not in st.session_state:
    st.session_state.timer_start = time.time()
if 'remaining_time' not in st.session_state:
    st.session_state.remaining_time = 180  # 3 minutes (180 seconds)
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# Set the total time allowed per question (in seconds)
TOTAL_TIME = 180  # 3 minutes (180 seconds) per question

# Questions, options, and correct answers
questions = [
    {"type": "mcq", "question": "Which is the largest country in the world?", "options": ["India", "USA", "China", "Russia"], "answer": "Russia"},
    {"type": "tf", "question": "Is Python a programming language?", "options": ["True", "False"], "answer": "True"},
    {"type": "mcq", "question": "How many days are there in a leap year?", "options": ["354", "366", "365", "420"], "answer": "366"},
    {"type": "mcq", "question": "Finish the sequence: 9, 18, 27, _?", "options": ["36", "34", "30", "37"], "answer": "36"},
    {"type": "mcq", "question": "Which one is the first fully supported 64-bit operating system?", "options": ["Earth", "Linux", "Mac", "Windows XP"], "answer": "Linux"}
]

# Function to load the next question
def next_question():
    st.session_state.current_index += 1
    st.session_state.timer_start = time.time()  # Reset timer for the next question
    st.session_state.remaining_time = TOTAL_TIME  # Reset remaining time
    st.experimental_rerun()  # Force the interface to refresh and load the next question

# Function to check the answer
def check_answer(selected_option):
    if selected_option.strip().lower() == questions[st.session_state.current_index]['answer'].strip().lower():
        st.session_state.score += 1
    next_question()

# Countdown Timer Logic
def countdown_timer():
    elapsed_time = time.time() - st.session_state.timer_start
    st.session_state.remaining_time = TOTAL_TIME - elapsed_time

    if st.session_state.remaining_time <= 0:  # Time's up
        next_question()

    # Display the remaining time in minutes and seconds
    minutes, seconds = divmod(int(st.session_state.remaining_time), 60)
    st.markdown(f"**Time Remaining:** {minutes:02d}:{seconds:02d} minutes")

# Display the current question
if st.session_state.current_index < len(questions):
    countdown_timer()  # Display the countdown timer and check if time has expired

    question = questions[st.session_state.current_index]
    st.markdown(f"**Question {st.session_state.current_index + 1}:** {question['question']}")

    if question['type'] == 'mcq':
        selected_option = st.radio("", question['options'])
    elif question['type'] == 'tf':
        selected_option = st.radio("", question['options'])

    if st.button("Submit"):
        check_answer(selected_option)

    # Sleep for a short time to prevent too many reruns
    time.sleep(1)
    st.experimental_rerun()  # Refresh to update the timer

else:
    st.markdown(f"### Quiz Completed! Your score: {st.session_state.score} out of {len(questions)}")
    
    # Save score to leaderboard
    name = st.text_input("Enter your name for the leaderboard:")
    if st.button("Submit Score"):
        st.session_state.leaderboard.append({"name": name, "score": st.session_state.score})
        st.session_state.leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x['score'], reverse=True)
        st.experimental_rerun()  # Refresh to update leaderboard

    # Display leaderboard
    st.markdown("### Leaderboard:")
    for i, entry in enumerate(st.session_state.leaderboard):
        st.markdown(f"{i + 1}. **{entry['name']}**: {entry['score']}")

    if st.button("Restart Quiz"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.timer_start = time.time()
        st.session_state.remaining_time = TOTAL_TIME
        st.experimental_rerun()  # Refresh to restart quiz
