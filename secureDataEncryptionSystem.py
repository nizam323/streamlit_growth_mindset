import streamlit as st
import hashlib
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher = Fernet(KEY)

stored_data = {}  
failed_attempts = 0

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed_pass = hash_passkey(passkey)

    if encrypted_text in stored_data:
        saved_data = stored_data[encrypted_text]
        if saved_data["passkey"] == hashed_pass:
            failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    failed_attempts += 1
    return None

st.title("🔐 Secure Data Encryption App")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.write("This app lets you **encrypt and save text** with a secret passkey, then retrieve it securely.")

elif choice == "Store Data":
    st.subheader("📁 Store Data")
    user_text = st.text_area("Enter your secret data:")
    user_pass = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_text and user_pass:
            encrypted = encrypt_data(user_text)
            hashed = hash_passkey(user_pass)
            stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data encrypted and stored!")
            st.text(f"Encrypted Text (save this to retrieve):\n{encrypted}")
        else:
            st.warning("Please enter both data and passkey.")

elif choice == "Retrieve Data":
    st.subheader("🔓 Retrieve Data")
    encrypted_input = st.text_area("Enter your encrypted text:")
    passkey_input = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey_input:
            result = decrypt_data(encrypted_input, passkey_input)
            if result:
                st.success(f"✅ Decrypted Data:\n{result}")
            else:
                remaining = 3 - failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {remaining}")
                if failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts. Redirecting to Login...")
                    st.experimental_rerun()
        else:
            st.warning("Enter both fields to proceed.")

elif choice == "Login":
    st.subheader("🔐 Login to Reset Attempts")
    master_key = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if master_key == "admin123":
            failed_attempts = 0
            st.success("✅ Login successful! You can now try again.")
        else:
            st.error("❌ Wrong master password.")
