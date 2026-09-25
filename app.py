import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PocketSmart AI", page_icon="💡", layout="centered")

st.title("💡 PocketSmart AI")
st.subheader("Your Smart Budget & Recommendation Assistant")
st.write("Manage your expenses, set savings goals, and get instant AI-driven financial advice!")

# Sidebar API Key Input
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Inputs
    st.header("📊 Input Your Financial Details")
    income = st.number_input("Monthly Income (₹):", min_value=0.0, step=1000.0)
    expenses = st.number_input("Monthly Expenses (₹):", min_value=0.0, step=1000.0)
    savings_goal = st.text_input("Financial Goal (e.g., Save ₹10,000 in 3 months for a phone):")

    if st.button("Generate Budget & AI Advice"):
        balance = income - expenses
        st.write(f"### 💰 Remaining Monthly Balance: ₹{balance:.2f}")

        if balance < 0:
            st.error("⚠️ You are spending more than you earn! Here is how to fix it:")
        else:
            st.success("✅ You have a positive balance! Here is your personalized plan:")

        # AI Recommendation Prompt
        prompt = f"""
        Act as an expert financial advisor for a student/individual with the following profile:
        - Monthly Income: ₹{income}
        - Monthly Expenses: ₹{expenses}
        - Remaining Balance: ₹{balance}
        - Financial Goal: {savings_goal}

        Provide a structured breakdown:
        1. 50/30/20 Budgeting Rule Analysis based on their income.
        2. 3 Actionable Tips to cut down unnecessary expenses.
        3. A step-by-step roadmap to achieve their financial goal.
        Keep the advice encouraging, realistic, and easy to read with bullet points.
        """

        with st.spinner("PocketSmart AI is analyzing your budget..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to start!")
