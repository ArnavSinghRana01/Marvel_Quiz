import streamlit as st
import marvel_quiz_data

# Define Marvel-themed colors
marvel_red = "#E62429"
marvel_blue = "#005EB8"
marvel_yellow = "#F1AA30"
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Use markdown to set the title text color
st.markdown(f"<h1 style='color:{marvel_red};'>Marvel Quiz</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .title {
        color: marvel_red;
    }
    .question {
        color: marvel_blue;
        font-weight: bold;
    }
    .choice {
        color: marvel_yellow;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def show_question():
    question_number = st.session_state.current_question + 1
    question = marvel_quiz_data.marvel_quiz_data[st.session_state.current_question]
    st.markdown(f"<div class='question'>Question {question_number}: {question['question']}</div>", unsafe_allow_html=True)
    selected_choice = st.radio("Select your answer:", question['choices'], key=question_number)
    submit_button = st.button("Submit", key=f"submit_button_{question_number}")
    if submit_button:
        check_answer(selected_choice)


# Function to check the selected answer and provide feedback
def check_answer(selected_choice):
    question = marvel_quiz_data.marvel_quiz_data[st.session_state.current_question]
    if selected_choice == question["answer"]:
        st.success("✅ **Correct! Well done!**")
        st.session_state.score += 1
    else:
        st.error(f"❌ **Incorrect!** The correct answer is: {question['answer']}")
    next_question()

# Function to move onto the next question
def next_question():
    current_question = st.session_state.current_question + 1
    if current_question < len(marvel_quiz_data.marvel_quiz_data): 
        st.session_state.current_question = current_question 
        show_question()
    else:
        st.write("---")
        if st.session_state.score == len(marvel_quiz_data.marvel_quiz_data):  # Check if user scored 5/5
            st.success("🎉 **Congratulations! You are a true Marvel fan!**")
        else:
            st.success(f"🎉 **Quiz Complete! Your Score: {st.session_state.score}/{len(marvel_quiz_data.marvel_quiz_data)}**")
        st.session_state.current_question = 0
        st.session_state.score = 0

# Main function - initializing the session state variables
def main():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0 
    if 'score' not in st.session_state:
        st.session_state.score = 0

    show_question()

if __name__ == "__main__":
    main()
