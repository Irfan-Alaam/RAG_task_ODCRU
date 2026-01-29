import os
from langchain_groq import ChatGroq
def load_groq_llm():
    if not os.environ.get("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY not set")

    llm = ChatGroq(
        groq_api_key=os.environ["GROQ_API_KEY"],
        model_name="llama-3.3-70b-versatile",
        temperature=0.2,
        max_retries=2,
        timeout=20,
    )
    return llm
