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
