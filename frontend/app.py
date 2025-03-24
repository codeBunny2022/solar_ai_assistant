import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.title("Solar AI Assistant ☀️")

topics = [
    "Introduction to Solar Energy",
    "Types of Solar Panels",
    "Solar Energy Efficiency",
    "Solar Power Installation Process",
    "Cost and Financial Benefits",
    "Environmental Impact of Solar Energy",
    "Latest Trends in Solar Industry"
]

explanation_levels = ["Basic", "Intermediate", "Advanced"]

st.subheader("Select a topic or ask your own question")
selected_topic = st.selectbox("Choose a topic:", ["Custom Question"] + topics)
custom_question = st.text_input("Or enter your own question:")
explanation_level = st.selectbox("Select the level of explanation:", explanation_levels)

if st.button("Ask"):
    question = custom_question if selected_topic == "Custom Question" else selected_topic

    if not question:
        st.warning("Please enter a question or select a topic.")
        st.stop()

    params = {"question": question, "level": explanation_level.lower()}
    response = requests.get(API_URL, params=params)
    
    try:
        data = response.json()
        st.write(data.get("response", "No response received"))
    except requests.exceptions.JSONDecodeError:
        st.error("Error: Backend returned an invalid response.")
