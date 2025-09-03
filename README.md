# 🛡️ AI-Powered Threat Intelligence Chatbot (LangChain + Streamlit)

Beginner-friendly project that fetches public cyber threat intel (CVE, CISA KEV, security news) and lets you ask natural-language questions like:
- *“What are the latest vulnerabilities in Windows?”*
- *“Summarize recent phishing trends.”*

It uses LangChain for retrieval + summarization and a **free LLM** via the Hugging Face Inference API by default (or **Ollama** locally).

## ✨ Features
- Ingest **CVE** (CIRCL), **CISA Known Exploited Vulnerabilities**, **security RSS feeds**, **Hacker News security stories**.
- Optional indicator enrichment: **OTX**, **AbuseIPDB**, **GreyNoise** (free keys).
- Local embeddings (**all-MiniLM-L6-v2**) + **Chroma** vector DB (no paid keys).
- Streamlit UI: one-click ingest, Q&A, and Daily Brief.

## 🧰 Prereqs
- Python 3.10+
- (Option A) Free **Hugging Face** token for hosted LLM
- (Option B) **Ollama** running locally with a chat model (e.g. `llama3.1:8b`)

## 🔑 Free API keys you can use
All optional except the LLM token unless you use Ollama.

- **Hugging Face Inference API** (free):
  1. Create account: https://huggingface.co/
  2. Go to **Settings → Access Tokens → New token** (type: *Read*). 
  3. Put it in `.env` as `HUGGINGFACEHUB_API_TOKEN`.

- **NVD CVE API** (free, increases rate limits):
  1. Request key: https://nvd.nist.gov/developers/request-an-api-key
  2. Put it in `.env` as `NVD_API_KEY`.

- **AlienVault OTX** (free registration):
  1. Sign up and get an API key from your profile.
  2. Put it in `.env` as `OTX_API_KEY`.

- **AbuseIPDB** (free tier 1,000 checks/day):
  1. Create account: https://www.abuseipdb.com/ (Dashboard → API).
  2. Put it in `.env` as `ABUSEIPDB_API_KEY`.

- **GreyNoise Community API** (free, limited lookups):
  1. Create free account and get key.
  2. Put it in `.env` as `GREYNOISE_API_KEY`.

> Public feeds that **require no key** and are already wired in:
> - CIRCL last CVEs, CISA KEV, RSS (BleepingComputer, The Hacker News), HN Algolia search.

## 🚀 Run it
```bash
git clone <this-zip-or-repo>
cd threat_intel_chatbot
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# EITHER set a HF token (default)
echo 'HUGGINGFACEHUB_API_TOKEN=your_token' >> .env
# OPTIONAL: choose a different HF model
echo 'HF_REPO_ID=HuggingFaceH4/zephyr-7b-beta' >> .env

# OR use Ollama locally (no hosted token needed)
# ollama run llama3.1:8b  # first-time pull
# echo 'OLLAMA_BASE_URL=http://localhost:11434' >> .env
# echo 'OLLAMA_MODEL=llama3.1:8b' >> .env

streamlit run app.py
```

## 🧱 Project structure
```
.
├── app.py                 # Streamlit UI
├── requirements.txt
├── .env.example
└── src
    ├── chains.py          # QA & summarization chains
    ├── config.py          # feed lists and constants
    ├── ingest.py          # feed/API fetchers -> LangChain Documents
    ├── llm.py             # LLM provider (HF or Ollama)
    └── storage.py         # Chroma vector store helpers
```

## 🧪 Try these prompts
- *“Summarize trending phishing lures this week and list sources.”*
- *“List high-severity CVEs affecting Linux published in the last 7 days.”*
- *“Compare KEV vs. NVD coverage for CVE-YYYY-XXXX.”*
- *“Is IP 1.2.3.4 noisy or malicious?”* (if you added indicator lookups)

## ⚠️ Notes
- Respect each API’s rate limits and Terms.
- Results from public feeds can be noisy; verify before acting.
- For larger data, consider a background scheduler (e.g., cron) and a real database for raw JSON.
