# 🛒 shop_recommendation_agent – Intelligent AI Shopping Recommendation Agent

**shop_recommendation_agent** is an open-source agentic AI shopping assistant built using **LangGraph**, powered by **Tavily** for real-time web search and **DeepSeek LLM via Groq** for intelligent decision-making. It redefines the online shopping experience by performing product comparison, analysis, and personalized recommendations — all delivered straight to your inbox along with relevant **YouTube video reviews fetched automatically**.

---

## 🚀 Features

- 🔎 **Real-Time Web Search**: Uses Tavily to fetch up-to-date product data and comparisons.
- 🤖 **Agentic Workflow**: Built on LangGraph to create a robust multi-agent pipeline.
- 📊 **Smart Product Analysis**: Compares specifications, reviews, and prices using DeepSeek via Groq.
- 📺 **YouTube Review Fetching**: Automatically finds relevant YouTube review links for the recommended product.
- 📬 **Structured Email Output**: Sends a neatly formatted email with the best product recommendation and YouTube review links.
- 🧠 **Domain-Agnostic**: Even if the user lacks product expertise, the agent ensures tailored recommendations.

---

## 🧠 Use Case Example

**Prompt**: *"Best smartphones under ₹20,000"*  
**Output**:
- The agent fetches current market options using Tavily.
- Performs detailed comparison using LLM.
- Chooses the most value-for-money product.
- Automatically finds relevant YouTube video reviews.
- Sends an email summarizing:
  - Product name
  - Key features
  - Price
  - YouTube review links

---

## 🔧 Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangGraph** | Multi-agent orchestration and workflow management |
| **Tavily** | Real-time web search for product data |
| **DeepSeek LLM (via Groq)** | Product analysis and decision-making |
| **YouTube Search (API or scraping)** | Fetching video review links |
| **Python** | Core programming language |
| **SMTP / Email API** | For sending structured recommendations to the user |

---

🧪 Installation & Running Instructions
1. 📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
2. 🔐 Set Up API Keys and Email Config
Create a .env file in your project root directory and add the following environment variables:

env
Copy
Edit
# Tavily API key (for web search)
TAVILY_API_KEY=your_tavily_api_key

# Groq API key (for DeepSeek LLM)
GROQ_API_KEY=your_groq_api_key

# YouTube Data API key (for fetching review videos)
YOUTUBE_API_KEY=your_youtube_api_key

# Email SMTP Configuration (Gmail recommended)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=youremail@gmail.com           # Sender's Gmail address
EMAIL_PASS=your_app_specific_password    # App-specific password
3. ✉️ Enable Gmail SMTP (for Email Sending)
To send emails via Gmail SMTP:

Go to Google Account Security.

Enable 2-Step Verification for your account.

Under "Signing in to Google", click on App passwords.

Generate an App Password for "Mail".

Use this password as EMAIL_PASS in the .env file.

4. 🧠 Set the Input Query and Receiver Email
In main.py, update the query and the recipient’s email:

python
Copy
Edit
# main.py

query = "best smartphones under ₹20000"              # Change this to your shopping query
receiver_email = "receiver@example.com"              # The email address to send results to
5. ▶️ Run the Agent
Once everything is set:

bash
Copy
Edit
python main.py


