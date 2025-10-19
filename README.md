🌐 Website Summarizer using Groq LLM & Streamlit

This project is a Streamlit web application that allows users to summarize website content using Groq’s Llama 3.3 70B model. The user simply enters a website URL, and the app automatically fetches and summarizes the page content — no API key input required, as it securely uses your API key from the .env file.

🚀 Features

✅ Summarizes website content into a concise 300-word summary

✅ Powered by Groq LLM for fast and accurate summarization

✅ Clean and simple Streamlit UI

✅ Automatic API key loading using dotenv

✅ YouTube support removed as requested (website-only summarization)

📁 Project Structure
your_project/
│
├─ .env                  # Stores the Groq API key
├─ app.py                # Streamlit application (UI)
├─ model.py              # LLM logic and summarization functions
├─ requirements.txt      # List of Python dependencies
└─ README.md             # Project documentation

🔑 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-repo-url.git
cd your_project

2️⃣ Create and Add Your API Key in .env

Create a file named .env and add:

GROQ_API_KEY=your_actual_key_here

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py

🧠 How It Works

User enters a valid website URL

The app loads the page content using UnstructuredURLLoader

Content is sent to the Groq LLM for summarization

A clean 300-word summary is displayed in the UI

📌 Requirements

Python 3.9 or higher

Internet connection

Groq API key