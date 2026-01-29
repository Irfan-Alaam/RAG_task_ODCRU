import os
from langchain_groq import ChatGroq
from src.config import GROQ_MODEL
def load_groq_llm():
    if not os.environ.get("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY not set")

    llm = ChatGroq(
        groq_api_key=os.environ["GROQ_API_KEY"],
        model_name=GROQ_MODEL,
        temperature=0.2,
        max_retries=2,
        timeout=20,
    )
    return llm
