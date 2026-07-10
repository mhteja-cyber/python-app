import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊")

st.title("✊ Rock Paper Scissors")
st.write("Play against the computer!")

# Initialize scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

choices = ["rock", "paper", "scissors"]

user = st.radio(
    "Choose your move:",
    choices,
    horizontal=True
)

if st.button("Play"):
    computer = random.choice(choices)

    st.write(f"**Computer chose:** {computer}")

    if user == computer:
        st.info("🤝 It's a Tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        st.success("🎉 You Win!")
        st.session_state.user_score += 1
    else:
        st.error("💻 Computer Wins!")
        st.session_state.computer_score += 1

st.divider()

st.subheader("🏆 Score")

col1, col2 = st.columns(2)

with col1:
    st.metric("Your Score", st.session_state.user_score)

with col2:
    st.metric("Computer Score", st.session_state.computer_score)

if st.button("Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Scores reset!")
