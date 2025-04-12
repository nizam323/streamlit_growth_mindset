import streamlit as st
import random

advice_list = [
    "Every challenge is an opportunity to grow. Keep pushing forward!",
    "Mistakes are proof that you're trying. Learn and move ahead!",
    "You're capable of amazing things—don’t let doubt hold you back.",
    "Growth comes from struggle. You're on the right path!",
    "Believe in yourself. You're stronger than you think!"
]

st.title("🌱 Growth Mindset Challenge")
st.subheader("Develop Your Skills and Overcome Challenges!")

st.write("""
A growth mindset helps you embrace challenges, learn from mistakes, and persist through difficulties.
Share what you're struggling with, and get a boost of motivation!
""")

name = st.text_input("Enter your name:")
challenge = st.text_area("What challenge are you facing right now?", placeholder="Describe your challenge here...")

if st.button("Join the Challenge!"):
    if name and challenge:
        st.success(f"Great, {name}! You're not alone in this journey.")
        st.info(f"Your challenge: {challenge}")
        motivation = random.choice(advice_list)
        st.markdown(f"💡 **Advice:** {motivation}")
    else:
        st.warning("Please enter both your name and your challenge to continue.")
