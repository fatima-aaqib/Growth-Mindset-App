import streamlit as st # type: ignore
import datetime

# Predefined daily growth mindset challenges
PREDEFINED_CHALLENGES = [
    "Learn something new for 15 minutes.",
    "Reflect on a recent failure and identify one lesson learned.",
    "Write down three things you're grateful for.",
    "Step out of your comfort zone and try something new.",
    "Praise someone else's effort or progress.",
    "Set a small, achievable goal for the day.",
    "Read an article or watch a video about growth mindset.",
    "Practice positive self-talk for 5 minutes.",
    "Ask for feedback on something you're working on.",
    "Celebrate a small win or progress you've made."
]

# Define motivational quotes
QUOTES = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Whether you think you can or you think you can't, you're right. – Henry Ford",
    "It's not that I'm so smart, it's just that I stay with problems longer. – Albert Einstein",
    "The harder you work for something, the greater you'll feel when you achieve it. – Unknown"
]

# Custom CSS for gradient background and styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #FF9A9E 0%, #FAD0C4 100%);
        color: #2E86C1;
        font-family: 'Arial', sans-serif;
    }
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        padding: 10px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        margin: 10px 0;
    }
    .subheader {
        font-size:[44px];
        font-weight: bold;
        color: #2E86C1;
        padding: 5px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
    }
    .quote {
        font-size: 18px;
        font-style: italic;
        color: #E74C3C;
        padding: 10px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
    }
    .challenge-box {
        padding: 15px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        margin: 10px 0;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and description
st.markdown('<p class="header">🌱 Growth Mindset Tracker 🚀</p>', unsafe_allow_html=True)
st.write("Welcome to the Growth Mindset Tracker! Use this app to develop a growth mindset by completing daily challenges, reflecting on your progress, and celebrating your efforts.")

# Initialize session state for user-added challenges and progress
if "user_challenges" not in st.session_state:
    st.session_state.user_challenges = []
if "completed_challenges" not in st.session_state:
    st.session_state.completed_challenges = 0

# User input for name
user_name = st.text_input("Enter your name to get started:")

if user_name:
    st.success(f"Hello, {user_name}! Let's grow together.")

    # Layout in columns
    col1, col2 = st.columns(2)

    with col1:
        # Allow users to add their own challenges
        st.markdown('<p class="subheader">➕ Add Your Own Challenge</p>', unsafe_allow_html=True)
        new_challenge = st.text_input("Enter a new challenge:")
        if st.button("Add Challenge") and new_challenge:
            st.session_state.user_challenges.append(new_challenge)
            st.success("Challenge added successfully!")

    with col2:
        # Display progress bar
        st.markdown('<p class="subheader">📊 Progress Tracker</p>', unsafe_allow_html=True)
        total_challenges = len(PREDEFINED_CHALLENGES) + len(st.session_state.user_challenges)
        progress = st.session_state.completed_challenges / total_challenges if total_challenges > 0 else 0
        st.progress(progress)
        st.write(f"Completed: {st.session_state.completed_challenges} / {total_challenges} challenges")

    # Combine predefined and user-added challenges
    all_challenges = PREDEFINED_CHALLENGES + st.session_state.user_challenges

    # Display today's challenge in a styled box
    st.markdown('<p class="subheader">🎯 Today\'s Challenge</p>', unsafe_allow_html=True)
    today = datetime.datetime.now().day % len(all_challenges)  # Cycle through challenges
    st.markdown(f'<div class="challenge-box">{all_challenges[today]}</div>', unsafe_allow_html=True)

    # Track completion
    if st.button("✅ I completed today's challenge!"):
        st.session_state.completed_challenges += 1
        st.balloons()
        st.success("🎉 Great job! Keep up the good work.")

    # Reflection Journal
    with st.expander("📔 Reflection Journal"):
        reflection = st.text_area("Take a moment to reflect on your experience today. What did you learn? How did you grow?")
        if reflection:
            st.write("Thank you for reflecting! Here's what you wrote:")
            st.write(reflection)

    # Motivational Quote
    st.markdown('<p class="subheader">💬 Motivational Quote</p>', unsafe_allow_html=True)
    quote_index = datetime.datetime.now().day % len(QUOTES)  # Cycle through quotes
    st.markdown(f'<div class="quote">{QUOTES[quote_index]}</div>', unsafe_allow_html=True)

    # Display all challenges in an expandable section
    with st.expander("📜 View All Challenges"):
        for i, challenge in enumerate(all_challenges, 1):
            st.write(f"{i}. {challenge}")