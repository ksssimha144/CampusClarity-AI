# CampusClarity AI 🎓

**Turn college notices into clear, actionable next steps using Gemma.**

## 💡 Problem

Students receive college announcements, event posters, examination updates, and other notices. Important dates, required actions, and missing information can be easy to overlook.

## 🚀 Solution

CampusClarity AI analyzes uploaded college notice images and produces a concise action plan to help students identify what matters and what to do next.

## ✨ Features

- **Image-based notice analysis** using Gemma.
- **Action extraction** to identify concrete next steps.
- **Deadline awareness** to classify dates as past, urgent, upcoming, or unstated.
- **Uncertainty awareness** to highlight important missing information.
- **Concise responses** designed to avoid repeating the entire notice.

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gen AI SDK
- Gemma model via the Gemini API

## ⚙️ Run Locally

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   ```bash
   pip install streamlit google-genai
   ```

4. Create `.streamlit/secrets.toml` and add your API key:

   ```toml
   GEMINI_API_KEY = "YOUR_API_KEY"
   ```

5. Start the app:

   ```bash
   python -m streamlit run app.py
   ```

## 🔐 Security

Never commit API keys or secret configuration files. The `.streamlit/secrets.toml` file should be excluded through `.gitignore`.

## ⚠️ Disclaimer

AI-generated results may contain errors. Always verify important dates, eligibility requirements, and instructions against the original notice.

## 🎯 Goal

Help students move from reading college announcements to understanding their next steps with less effort.