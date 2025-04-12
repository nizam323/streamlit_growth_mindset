# import streamlit as st

# st.set_page_config(page_title="Growth Mindset Web")
# st.title()
# st.header()
# st.write()

import streamlit as st

st.title("Growth Mindset Challenge")
st.subheader("Develop Your Skills and Overcome Challenges!")

st.write("""A growth mindset helps you embrace challenges, learn from mistakes, and persist through difficulties.""")

name = st.text_input("Enter your name:")
if st.button("Join the Challenge!"):
    st.success(f"Great, {name}! Keep growing!")