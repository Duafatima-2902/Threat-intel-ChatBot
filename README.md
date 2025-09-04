🛡️ AI-Powered Threat Intelligence Chatbot (LangChain + Streamlit)
🎭 CyberSass 🤡🛡️

Your sarcastic AI Threat Intel Sidekick

“Hackers never sleep… but hey, at least I can roast them while keeping you informed.”

🚀 What is CyberJester?

CyberJester is an AI-powered cybersecurity chatbot that fetches the latest threats, CVEs, and security news and explains them in a funny, sarcastic, beginner-friendly way.

Instead of boring reports, CyberJester makes cybersecurity updates feel like talking to a witty friend.

✨ Features

✅ Fetches latest cybersecurity news & CVE updates
✅ Sarcastic & fun responses (never a dull moment 🥱👉😂)
✅ Explains complex security terms in simple words for beginners
✅ Memory-enabled conversations – it remembers your past questions
✅ Powered by Gemini API + LangChain
✅ Runs on a simple Streamlit web app

🛠️ Tech Stack

Python 3.10+

Streamlit
 – simple web UI

LangChain
 – memory & chaining

Gemini API
 – the brain of CyberSass

Requests
 – fetching feeds

Feedparser
 – for RSS news

📦 Installation

Clone this repo

git clone https://github.com/yourusername/cyberjester.git
cd cyberjester


Set up a virtual environment

python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Add your API keys in .env

GEMINI_API_KEY=your_gemini_api_key_here

▶️ Run the App
streamlit run app.py


Now open your browser at 👉 http://localhost:8501

<img width="1353" height="825" alt="image" src="https://github.com/user-attachments/assets/b5a84380-5f5f-459c-a29d-33ea6bea82bb" />

🤡 Example Chat

You: “What’s the latest phishing trend?”
CyberJester: “Oh, you mean besides Nigerian princes and fake Netflix logins? Well, apparently hackers now send fake invoice scams. Because who doesn’t love a good surprise bill? 💸”

🌍 Roadmap

 Add dark mode UI 🌑

 Integrate more threat feeds (AbuseIPDB, OTX)

 Export daily brief as PDF

 Deploy on HuggingFace Spaces

🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

📜 License

MIT License – free to use, modify, and sass around 😎

💡 Credits

Built with ❤️ by Dua Fatima
Powered by Gemini + LangChain + Streamlit

