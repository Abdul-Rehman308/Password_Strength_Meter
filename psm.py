import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# Custom CSS for Glassmorphism & Clean UI
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
            text-align: center;
        }
        .glass-container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
        }
        /* Input Field Styling */
        div[data-baseweb="input"] {
            width: 70% !important; /* Input field ka size thoda bara */
            height: 50px; /* Proper height */
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            border: 2px solid #00c9ff;
            background: rgba(255, 255, 255, 0.2);
            color: black !important;
        }
        /* Slightly Smaller Label */
        label[for="Enter your password"] {
            font-weight: bold;
            font-size: 16px;
        }
        /* Button Styling */
        .stButton>button {
            background: linear-gradient(90deg, #00c9ff, #92fe9d);
            color: white;
            padding: 12px; /* Proper padding */
            border-radius: 8px;
            font-size: 16px;
            width: 40%; /* Button ka size balanced */
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #92fe9d, #00c9ff);
        }
        .password-strength-bar {
            height: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title & Description
st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Password Strength Bar
    strength_levels = ["🔴 Weak", "🟠 Fair", "🟡 Moderate", "🟢 Strong"]
    strength_colors = ["#ff4d4d", "#ffa500", "#ffcc00", "#4caf50"]
    
    st.markdown(f'<div class="password-strength-bar" style="background: {strength_colors[score]}; width: {score * 25}%;"></div>', unsafe_allow_html=True)
    st.write(f"**Password Strength: {strength_levels[score]}**")

    # Display Password Strength Result
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password - Follow the suggestions below to strengthen it.**")

    # Show improvement suggestions
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# User Input Field
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

# Button to Check Password Strength (Perfect Center)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password first!")

st.markdown('</div>', unsafe_allow_html=True)
