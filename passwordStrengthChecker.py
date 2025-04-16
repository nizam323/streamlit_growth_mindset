import re
import streamlit as st

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

score = 0

if password:
    st.subheader("🔍 Checking your password...")

    if len(password) >= 8:
        score += 1
        st.success("✅ Password length is good.")
    else:
        st.error("❌ Your password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        st.success("✅ Contains both uppercase and lowercase letters.")
    else:
        st.error("❌ Add both UPPERCASE and lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
        st.success("✅ Contains numbers.")
    else:
        st.error("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
        st.success("✅ Contains special characters (!@#$%^&*).")
    else:
        st.error("❌ Add at least one special character (!@#$%^&*).")

    if password.lower() in ["password123", "123456"]:
        score = 0
        st.error("❌ This is a common and unsafe password. Please use something more unique.")

    st.write("---")
    if score == 4:
        st.success("✅ Your password is Strong!")
    elif score == 3:
        st.warning("⚠️ Your password is Moderate. Try to make it stronger.")
    else:
        st.error("❌ Your password is Weak. Please improve it.")
