
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from tavily import TavilyClient
from langchain_community.document_loaders import WebBaseLoader
from googleapiclient.discovery import build
# Load environment variables from the .env file
from logger import logger
load_dotenv()
groq_api_key = os.environ['GROQ_API_KEY']
youtube_api_key = os.environ['YOUTUBE_API_KEY']
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    api_key=groq_api_key,
    temperature=0.5,
)
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

import tiktoken
from langchain_community.document_loaders import WebBaseLoader

# Initialize tokenizer for Groq-compatible models
tokenizer = tiktoken.get_encoding("cl100k_base")
MAX_TOKENS = 4000

def truncate_tokens(text: str, max_tokens: int = MAX_TOKENS) -> str:
    """Truncate text to max_tokens from the start (cut excess from end)."""
    tokens = tokenizer.encode(text)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
    return tokenizer.decode(tokens)

def load_blog_content(page_url):
    try:
        # Load blog content from URL
        loader = WebBaseLoader(web_paths=[page_url], bs_get_text_kwargs={"separator": " ", "strip": True})
        loaded_content = loader.load()

        # Extract full text
        blog_content = " ".join([doc.page_content for doc in loaded_content])

        # Truncate to 4000 tokens
        truncated_content = truncate_tokens(blog_content, max_tokens=MAX_TOKENS)

        return truncated_content

    except Exception as e:
        logger.info(f"Error loading content from {page_url}: {e}")
        return ""



youtube = build('youtube', 'v3', developerKey=youtube_api_key)
