import random
from transformers import pipeline

mood_responses = {
    "good": [
        "Awesome! Let's power through these tasks! 💪",
        "I’m loving your energy today! Let’s get cracking! 🚀",
        "Your vibe is immaculate today 😎 — go conquer these!", 
        "Let's prepare to tackle these! 💪"
    ],
    "a bit low": [
        "It's totally okay to feel this way. These tasks are light enough to handle. ❤️",
        "Take your time, and maybe try tackling one of these at your pace. 💆‍♂️",
        "Don't worry, you’ve got this. One step at a time! 🌱",
        "I understand you are not feeling too well today, and it is alright. You can choose the light tasks."
    ],
    "neutral": [
        "Here’s a balanced set of tasks to maintain the flow 👌",
        "Let’s keep the day going with these tasks ⚖️",
        "A steady day calls for a steady plan — here you go! 📋"
    ]
}



project_plan = [
    {
        "task": "Fix critical bug causing system crash.",
        "priority": "High",
        "start_date": "2025-04-21",
        "end_date": "2025-04-25",
        "assigned_to": "Employee A"
    },
    {
        "task": "Respond to customer escalation on service outage.",
        "priority": "High",
        "start_date": "2025-04-21",
        "end_date": "2025-04-24",
        "assigned_to": "Employee B"
    },
    {
        "task": "Investigate issue in production server logs.",
        "priority": "High",
        "start_date": "2025-04-26",
        "end_date": "2025-04-30",
        "assigned_to": "Employee A"
    },
    {
        "task": "Write unit tests for login module.",
        "priority": "Medium",
        "start_date": "2025-04-24",
        "end_date": "2025-04-28",
        "assigned_to": "Employee C"
    },
    {
        "task": "Finish design for new dashboard layout.",
        "priority": "Medium",
        "start_date": "2025-04-29",
        "end_date": "2025-05-02",
        "assigned_to": "Employee B"
    },
    {
        "task": "Review pull request from intern.",
        "priority": "Medium",
        "start_date": "2025-05-01",
        "end_date": "2025-05-02",
        "assigned_to": "Employee C"
    },
    {
        "task": "Update documentation for onboarding guide.",
        "priority": "Medium",
        "start_date": "2025-05-05",
        "end_date": "2025-05-08",
        "assigned_to": "Employee C"
    },
    {
        "task": "Prepare final report for client presentation.",
        "priority": "High",
        "start_date": "2025-05-05",
        "end_date": "2025-05-09",
        "assigned_to": "Employee A"
    },
    {
        "task": "Schedule weekly sync meeting.",
        "priority": "Low",
        "start_date": "2025-05-06",
        "end_date": "2025-05-07",
        "assigned_to": "Employee B"
    },
    {
        "task": "Organize team-building activity next month.",
        "priority": "Low",
        "start_date": "2025-05-09",
        "end_date": "2025-05-12",
        "assigned_to": "Employee C"
    }
]


import re

response = """
project_plan = [
    {
        "task": "Fix critical bug causing system crash.",
        "priority": "High",
        "start_date": "2025-04-21",
        "end_date": "2025-04-25",
        "assigned_to": "Employee A"
    },
    {
        "task": "Respond to customer escalation on service outage.",
        "priority": "High",
        "start_date": "2025-04-21",
        "end_date": "2025-04-24",
        "assigned_to": "Employee B"
    },
    {
        "task": "Investigate issue in production server logs.",
        "priority": "High",
        "start_date": "2025-04-26",
        "end_date": "2025-04-30",
        "assigned_to": "Employee A"
    },
    {
        "task": "Write unit tests for login module.",
        "priority": "Medium",
        "start_date": "2025-04-24",
        "end_date": "2025-04-28",
        "assigned_to": "Employee C"
    },
    {
        "task": "Finish design for new dashboard layout.",
        "priority": "Medium",
        "start_date": "2025-04-29",
        "end_date": "2025-05-02",
        "assigned_to": "Employee B"
    },
    {
        "task": "Review pull request from intern.",
        "priority": "Medium",
        "start_date": "2025-05-01",
        "end_date": "2025-05-02",
        "assigned_to": "Employee C"
    },
    {
        "task": "Update documentation for onboarding guide.",
        "priority": "Medium",
        "start_date": "2025-05-05",
        "end_date": "2025-05-08",
        "assigned_to": "Employee C"
    },
    {
        "task": "Prepare final report for client presentation.",
        "priority": "High",
        "start_date": "2025-05-05",
        "end_date": "2025-05-09",
        "assigned_to": "Employee A"
    },
    {
        "task": "Schedule weekly sync meeting.",
        "priority": "Low",
        "start_date": "2025-05-06",
        "end_date": "2025-05-07",
        "assigned_to": "Employee B"
    },
    {
        "task": "Organize team-building activity next month.",
        "priority": "Low",
        "start_date": "2025-05-09",
        "end_date": "2025-05-12",
        "assigned_to": "Employee C"
    }
]
"""

# Extract everything from 'project_plan = [' to the last closing bracket of the list
# match = re.search(r"(project_plan\s*=\s*\[.*?\])", response, re.DOTALL)

# if match:
#     extracted_code = match.group(1)
#     print("Extracted Code:\n")
#     print(extracted_code)
# else:
#     print("No project_plan code block found.")




# nltk.download("vader_lexicon")
# analyzer = SentimentIntensityAnalyzer()

# def get_sentiment_label(text):
#     score = analyzer.polarity_scores(text)
#     compound = score['compound']
#     if compound > 0.05:
#         return "good"
#     elif compound < -0.05:
#         return "a bit low"
#     else:
#         return "neutral"




sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment_label(text):
    result = sentiment_pipeline(text)[0]
    label = result['label'].lower()
    confidence = result['score']

    if confidence < 0.75:
        return "neutral"
    elif label == "positive":
        return "good"
    elif label == "negative":
        return "a bit low"
    else:
        return "neutral"


def get_sentiment_response(sentiment):
    responses = mood_responses.get(sentiment, ["Let's get to work!"])
    return random.choice(responses)



def recommend_tasks(sentiment, plan):
    priority_order = {'High': 3, 'Medium': 2, 'Low': 1}

    if sentiment == "a bit low":
        filtered = [t for t in plan if t["priority"] in ["Low", "Medium"]]
    elif sentiment == "good":
        filtered = [t for t in plan if t["priority"] in ["High", "Medium"]]
    else:
        filtered = [t for t in plan if t["priority"] == "Medium"]
    
    sorted_tasks = sorted(filtered, key=lambda x: priority_order.get(x['priority'], 0), reverse=True)
    return sorted_tasks



def input_check(text):
    return bool(re.search(r'[a-zA-Z]', text)) and len(text.strip()) > 1


