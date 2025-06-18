import streamlit as st
import requests

# Load API key securely
api_key = st.secrets["GROQ_API_KEY"]

# Groq API endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Streamlit App UI
st.title("🌟 Daily Motivation (Powered by Groq + Llama 3)")

if st.button("Get Motivational Quote"):
    st.info("Generating your quote...")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",  # You can also try "llama3-70b-8192"
        "messages": [
            {"role": "user", "content": "Give me a short motivational quote"}
        ],
        "temperature": 0.7,
        "max_tokens": 60
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        quote = result["choices"][0]["message"]["content"]
        st.success("Here's your quote:")
        st.write(quote.strip())

    except Exception as e:
        st.error(f"Error: {e}")
