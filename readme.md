# 🛒 shop_recommendation_agent :Intelligent AI Shopping Recommendation Agent

**shop_recommendation_agent** is an open-source agentic AI shopping assistant built using **LangGraph**, powered by **Tavily** for real-time web search and **DeepSeek LLM via Groq** for intelligent decision-making. It redefines the online shopping experience by performing product comparison, analysis, and personalized recommendations  all delivered straight to your inbox along with relevant **YouTube video reviews fetched automatically**.

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

# Smart Query Agent

This project demonstrates a simple yet powerful query-handling agent that utilizes Tavily, Groq, and YouTube APIs. It also integrates email functionality using SMTP with Google 2-Step Verification enabled.

---

## 📦 Installation

Install all required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🔑 API & Email Setup

### 1. Tavily, Groq, and YouTube API Keys

Make sure to set the following API keys in your `.env` or directly in your Python code:

- `TAVILY_API_KEY`
- `GROQ_API_KEY`
- `YOUTUBE_API_KEY`

### 2. Email Configuration (SMTP)

To send emails from the agent, configure the sender's email and password in the script.

> ✅ **Note**: You must enable **Google 2-Step Verification** and create an **App Password** to use SMTP services.

Set:

- **Sender Email Address** (e.g., `youremail@gmail.com`)
- **App Password** (generated from Google)

Example:
```python
sender_email = "youremail@gmail.com"
sender_password = "your_app_specific_password"
```

---

## 📨 Usage

### Set the Receiver Email Address

In `main.py`, assign the email address of the person you want to send the response to:

```python
receiver_email = "receiver@example.com"
```

### Invoke the Query and email to  Agent

Once everything is set up, simply run the following:

```bash
python main.py
```

---

## ✅ Summary

- Install dependencies: `pip install -r requirements.txt`
- Add Tavily, Groq, and YouTube API keys
- Configure Google email with App Password
- Set receiver email in `main.py`
- Run the app: `python main.py`

---

## 💡 Tips

- Ensure internet connection is active
- Use environment variables or a `.env` file to secure sensitive credentials
- Log API responses or errors to debug issues

---


