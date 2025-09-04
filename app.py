import streamlit as st
import os
import requests
import feedparser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# LLM setup
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# Sarcastic system intro
sarcastic_intro = """You are a witty, sarcastic Cyber Threat Intelligence assistant.
Rules:
- Always reply in a fun, sarcastic tone.
- Explain cyber security terms in simple, beginner-friendly ways.
- Use humor, analogies, and jokes.
- Provide live cyber threat updates when asked.
- When someone asks for "latest threats", fetch recent CISA advisories and Hacker News trends.
- If you don't know the answer, make a funny guess.
- Never break character.
"""

# 📰 Fetch latest CISA advisories
def get_cisa_alerts(limit=3):
    url = "https://www.cisa.gov/sites/default/files/cdap/rss.xml"
    feed = feedparser.parse(url)
    alerts = [entry.title for entry in feed.entries[:limit]]
    return alerts

# 📰 Fetch Hacker News (cybersecurity)
def get_hackernews(limit=3):
    url = "https://hn.algolia.com/api/v1/search?query=cybersecurity&tags=story"
    res = requests.get(url).json()
    stories = [hit["title"] for hit in res["hits"][:limit]]
    return stories

# Streamlit UI
st.set_page_config(page_title="💀 Funny Cyber Threat Bot", page_icon="💀")
st.title("💀 Cyber Threat Chatbot (with Sarcasm + Live Threats)")

# Display history
if "history" not in st.session_state:
    st.session_state["history"] = []

for msg in st.session_state["history"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if question := st.chat_input("Ask me anything about threats..."):
    st.chat_message("user").write(question)
    st.session_state["history"].append({"role": "user", "content": question})

    # Check if user asked for "latest threats"
    if "latest threats" in question.lower() or "updates" in question.lower():
        cisa = get_cisa_alerts()
        hn = get_hackernews()
        feeds = f"🔥 Latest CISA Alerts:\n- " + "\n- ".join(cisa) + \
                f"\n\n🚨 Hacker News Trends:\n- " + "\n- ".join(hn)
        full_prompt = sarcastic_intro + "\nUser: Give me the latest threats but explain in a fun, sarcastic way.\n\nHere’s the intel:\n" + feeds
    else:
        full_prompt = sarcastic_intro + "\nUser: " + question

    response = conversation.run(full_prompt)

    st.chat_message("assistant").write(response)
    st.session_state["history"].append({"role": "assistant", "content": response})
