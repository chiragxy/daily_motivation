import streamlit as st
import requests
import random
import time

# ----- Config -----
st.set_page_config(page_title="Daily Motivation", page_icon="🌟", layout="centered")

# ----- Groq API Key -----
api_key = st.secrets["GROQ_API_KEY"]
url = "https://api.groq.com/openai/v1/chat/completions"

# ----- Encouragement messages -----
loading_messages = [
    "Brewing positivity... ☕",
    "Tuning into greatness... 🎧",
    "Polishing your mindset... ✨",
    "Sharpening your focus... 🎯",
    "Feeding your soul... 💫",
]

# ----- Page Title -----
st.markdown("""
# 🌈 **Daily Dose of Motivation**
Welcome! Click the button below to spark your day with an inspiring quote.  
""")

# ----- Button -----
if st.button("💡 Inspire Me!"):
    # Random fun loading message
    with st.spinner(random.choice(loading_messages)):
        time.sleep(1)  # short wait to enhance feel

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "user", "content": "Give me a short motivational quote"}
            ],
            "temperature": 0.8,
            "max_tokens": 60
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            quote = result["choices"][0]["message"]["content"].strip()

            st.success("🌟 Here's your quote:")
            st.markdown(f"> *{quote}*")

            st.caption("🤖 Powered by LLaMA3-8B via Groq API")

        except Exception as e:
            st.error(f"⚠️ Failed to fetch quote: {e}")
else:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzM2OHVvYmxyZDA4bzZ5NDBhcHZyc3NvZ3h6dTdkMnR2ZmU3enN1YyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Cmr1OMJ2FN0B2/giphy.gif",
             use_column_width=True, caption="Click above to get inspired!")

