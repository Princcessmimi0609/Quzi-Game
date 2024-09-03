import streamlit as st
from PIL import Image
import base64
import time

# Load and encode the image in Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Use your local image path
image_base64 = get_base64_of_bin_file("3482192.jpg")

# Corrected CSS for Background Image using Base64
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{image_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
'''

# Encode the local audio file in Base64
audio_base64 = get_base64_of_bin_file("月亮代表我的心 The Moon Represents My Heart Piano.mp3")

# Embed Background Music using Base64
audio_html = f'''
<audio autoplay loop>
    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    Your browser does not support the audio element.
</audio>
'''
# Use Streamlit's built-in audio function to play the local audio file
audio_file_path = "C:/Users/princ/Desktop/Python Projects/Quiz Game/audio/月亮代表我的心 The Moon Represents My Heart Piano.mp3"

# Play audio using Streamlit's built-in function
st.audio(audio_file_path, format="audio/mp3", start_time=0,)

# Embed background music
st.markdown(audio_html, unsafe_allow_html=True)


# Display an example image
image_path = ("moon.jpg")
image = Image.open(image_path)
st.image(image, use_column_width=True)

# Apply CSS for background image
st.markdown(page_bg_img, unsafe_allow_html=True)


# Initialize session state variables
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'timer_start' not in st.session_state:
    st.session_state.timer_start = time.time()
if 'remaining_time' not in st.session_state:
    st.session_state.remaining_time = 180  # 3 minutes (180 seconds)
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# List of questions with optional GIFs
questions = [
    {
        "type": "short_answer",
        "question": "稀奇真稀奇，天天脫層皮；到了大年夜，有骨卻沒皮?",
        ##"options": ["India", "USA", "China", "Russia"],
        "answer": "日曆",
        ##"gif": "https://media.giphy.com/media/3o7abB06u9bNzA8lu8/giphy.gif",  # Example GIF URL for the question
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG10NmQ4ajBtbDhlbWpndTYzbHhoYmg4bTE4MWI4ODB1dG9vcmozYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J6Ukx0azkxCBGUn846/giphy.gif"  # Example GIF URL for the answer
    },
    {
        "type": "short_answer",
        "question": "老婆婆電頭髮?",
        "answer": "銀絲捲",
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExemNzZWR5N3Q4MXM0bzV2Mm5nYjJycThzcW4wcTVidzNwOHh6YjFoZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R26ERFVcOuANi3EWfT/giphy.gif"  # Example GIF URL for the answer
    },
    {
        "type": "short_answer",
        "question": "麻屋子紅帳子，裡面一個白胖子。?",
        "answer": "花生",
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGEyNG1kaDN3MGE4anI0ZWttaWtmdGV0NmJyMnJnZHBmbjd2dTRwYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPCY9mCqND5gJ0s/giphy.gif"  # Example GIF URL for the answer
    },
    {
        "type": "short_answer",
        "question": "湖入面原本有魚蝦蟹，有一日只發現剩下魚及蟹。（猜一中國地區名）?",
        "answer": "哈爾濱（蝦已奔）",
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmIxNWZjeHJrYmk2dHN6eWZmeXM0b294aGx5czV2Nm16ZnZwdWZoayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4FGjjpumEDXgnVXG/giphy.gif"  # GIF URL for the answer
    },
    {
        "type": "short_answer",
        "question": "不是點心不是糖，軟軟涼涼肚裏藏，不能吃來不能喝，每天也要嘗一嘗。?",
        "answer": "牙膏",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHoweDNzbmk5bXc4aWVtMDBwaXQ3cnc0Zmh5Nmg3OG93cjZxMHZveCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/j1ovgbiiNs784/giphy.gif"
    },
     {
        "type": "short_answer",
        "question": "比貓大隻，比熊可愛，愛吃竹子，兼做外賣。?",
        "answer": "熊貓",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmo2d245OGxyd2lsOGxxdHI4cmJubG9leXBqaG1vNTV0am1xMHJ3OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/snpENu20kUrTESS3ko/giphy.gif"
    },
     {
        "type": "short_answer",
        "question": "24小時午餐 ..不停食 (猜天文現象)?",
        "answer": "日全蝕",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmhtYmM0bXBkYm5jcm90eDRneGVnaWhyZHV0dDI1eXBhd2gxczJ5bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hy9L8KcJp4Td6sXKt3/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "左手五個，右手五個，拿去十個，還剩十個。?",
        "answer": "手套",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExazJhejRmcmo5YnM3ZWVpcWFzdHVjZ2RpemdsZ3NqcjhqZmtyYXg2NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JpdvqUB2xeydKPZA0I/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "摘下是綠的，切下是紅的，吐出是黑的，剩下是白的?",
        "answer": "西瓜",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3RwcHBxbnY0bndjNTZybnBkb2J5OWt0eW12cXozcmVvazlqeWxncCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2JJuGNzLVmLDcD0Q/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "將軍無棋。（猜HK地區名）?",
        "answer": "竹園（捉完）",
        "gif": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGYzMzI2eXd5bml6YTEzNmdhd3J6cHB1cGh5a25zc2p0eDA2c2xmciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QW9gued0UndbeUrr8S/giphy.gif",
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXZpZThqNjBjemg3NWIxM2ZqeW96OWJoanVxZXFlZnl3N3ltdHByMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sWEUITjh864uZyaiIs/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "狼來了。?",
        "answer": "楊桃（羊逃）",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGVkc29kb3ZmYWN2MThqY3FvejljcDB0MWlxODJ1dTltcjZ5dmJhbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DburSAs9ZdBdCqEPhX/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "兩姐妹，一樣長，酸甜苦辣，她先嘗。?",
        "answer": "筷子",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXF6ZWdodXg4ZXJwenFqMnhueXNkNmtmZDdwNng0Nm01dmlnanF0OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cPJU9vzIM6l6oYR7VI/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "身穿紅袍，頭戴綠帽。?",
        "answer": "紅蘿蔔",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem05dWRsMDc3bjc4YjEybXplMzU5NHk1aHE3ZXZlYmtybnVndWo3YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xwkewgvaFB75Nm/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "頭上亮光光，出門就成雙，背上縛繩子，載人走四方。?",
        "answer": "皮鞋",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExenA0cThhdGN5eDJ4YWUyaWlwNHNkN2Vjd3k2M3R3ZGMzZ2Q5Z2Q2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JRzfAFk75qgI95Q8WW/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "一間屋，三個門，裡面只住半個人。?",
        "answer": "褲",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExb25nc2owNGxlYzh1aGpsd3RwMGEyaWxqdjVkYmp4amYwM2RqMGpwaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IhCYLb0ZitQe7V7xj1/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "兄弟七八個，圍著柱子坐，大家一分手，衣服全扯破。?",
        "answer": "蒜",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3kzMGUzMnowZDFseHFvYm44ZWNmNXZwdnZsaGdxZGRwNGt6bWx2aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2FazbV7tdNqYMe47K/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "消防員放假。（猜HK 地區名）?",
        "answer": "油麻地（休孖day，消防員常常返一日放兩日假）",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2t2cDdmOXI1M2ZhbGFtZW55emdnd2toa3RnMHpvd285MG5xNDJrOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5sagBQGSIgeX6QsxKl/giphy.gif"
    },
    {
        "type": "short_answer",
        "question": "青布包白布，白布包梳子，梳子包米。）?",
        "answer": "柚子",
        "gif": None,
        "gif_answer": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTZycG1zcmU2Zzd2ZWFrYm5wNmZlNWQ1ZDJmN28wM2l3YWllOW5hbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LP7a5Asc8TD8I/giphy.gif"
    },
]


# Function to display questions in the desired format
def display_question(question):
    st.markdown(f"**{question['question']}?**")
    
    # Display the GIF for the question if available
    if question.get('gif'):
        st.image(question['gif'], use_column_width=True)
    
    user_answer = st.text_input("Enter your answer:", key=f"answer_{st.session_state.current_index}")

    # When the "Submit" button is clicked, show the correct answer
    if st.button("Submit", key=f"submit_{st.session_state.current_index}"):
        st.session_state.show_answer = True  # Set flag to show the correct answer

    # Display the correct answer if the flag is set
    if st.session_state.show_answer:
        st.write(f"Correct Answer 正確答案 : **{question['answer']}**")
        
        # Display the GIF for the correct answer if available
        if question.get('gif_answer'):
            st.image(question['gif_answer'], use_column_width=True)

        st.write("-" * 50)  # Separator for clarity

        # Provide a "Next Question" button
        if st.button("Next Question"):
            next_question()

# Function to load the next question
def next_question():
    st.session_state.current_index += 1
    st.session_state.show_answer = False  # Reset the flag to hide the answer for the next question
    st.session_state.timer_start = time.time()  # Reset timer for the next question
    st.session_state.remaining_time = 180  # Reset remaining time
    st.experimental_rerun()  # Force the interface to refresh and load the next question

# Main display logic
if st.session_state.current_index < len(questions):
    display_question(questions[st.session_state.current_index])
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
        st.session_state.remaining_time = 180
        st.experimental_rerun()  # Refresh to restart quiz
