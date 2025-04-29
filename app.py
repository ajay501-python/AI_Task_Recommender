import streamlit as st
import time
from task_recommender import get_sentiment_response, get_sentiment_label, recommend_tasks, project_plan, input_check

st.set_page_config(page_title="AI Task Recommender", layout="centered")

st.title("Sentiment-Based Task Manager 🧠")
st.write("Get personalized task suggestions based on how you feel.")

# Mood Input
user_mood = st.text_area("**How are you feeling today?**")

if st.button("Get Task Recommendations"):
    if user_mood.strip() and input_check(user_mood):
        
        sentiment = get_sentiment_label(user_mood)
        recommended = recommend_tasks(sentiment, project_plan)
        response_message = get_sentiment_response(sentiment)
        if sentiment == "good":
            st.success(response_message)
            #st.success(f"I am happy that you are feeling **{sentiment.upper()}** today!😊")
        elif sentiment == "a bit low":
            st.warning(response_message)
            #st.warning(f"I understand that you might be feeling **{sentiment}** 🙁 ...")
        else:
            st.info(response_message)
            #st.info(f"Detected mood: **{sentiment.capitalize()}**")
        

        if recommended:
            with st.spinner("Getting curated tasks for your mood...", show_time=True):
                time.sleep(2)
            if sentiment == "good":
                st.markdown("""<p style="font-size: 26px; font-weight: bold;"> You can surely tackle these today! </p>""", unsafe_allow_html=True)
            elif sentiment == "a bit low":
                st.markdown("""<p style="font-size: 26px; font-weight: bold;">No worries, you can work on these tasks for today...</p>""", unsafe_allow_html=True)
            st.markdown("""<p style="font-size: 24px; font-weight: bold;"> 📋 Suggested Tasks :</p>""", unsafe_allow_html=True)
            for task in recommended:
                if task['priority'] == "High":
                    st.markdown(f"- **{task['task']}**   _(Priority: :red-badge[{task['priority']}])_")
                if task['priority'] == "Medium":
                    st.markdown(f"- **{task['task']}**   _(Priority: :orange-badge[{task['priority']}])_")
                if task['priority'] == "Low":
                    st.markdown(f"- **{task['task']}**   _(Priority: :green-badge[{task['priority']}])_")
                
        else:
            st.warning("No suitable tasks found for your mood.")
    else:
        st.info("This doesn't seem right 🤔...")








# OLD ---------------------------------------------------------------------


# from sentiment_model import analyze_sentiment

# # Page setup
# st.set_page_config(page_title="Sentiment Analyzer", page_icon="🙂")

# st.title("Task Sentiment Analyzer 🙂")
# st.write("This task analyzes the task modality 🧑🏻‍🦱")

# # User input
# task_description = st.text_area("Enter task here:")
# #text = "This task is really frustrating and overdue."
# label, score = analyze_sentiment(task_description)

# st.write(f"User text: {task_description}")
# st.write(f"Sentiment: {label}")
# st.write(f"Confidence score: {score}")