**Linux Command RAG Assistant**

A Retrieval-Augmented Generation (RAG) based assistant for Linux commands, concepts, installation guides, and troubleshooting.
The system combines ChromaDB, Sentence Transformers, and a Groq-hosted LLM to deliver fast, accurate, and context-grounded answers strictly from provided documentation.

**🚀 Features**

1. Semantic search over Linux documentation
2. Context-aware answers using RAG
3. Persistent vector storage with ChromaDB
4. Ultra-low latency responses via Groq API
5. Modular, production-ready architecture
6. Conversational memory support
7. API-based interface (FastAPI)

**Tech Stack**

1. Python 3.10+
2. ChromaDB – Vector database
3. Sentence-Transformers – BAAI/bge-m3
4. Groq API – LLM inference
5. FastAPI – Backend API
6. LangChain – RAG orchestration

**Environment Variables**

Create a .env file: 
    GROQ_API_KEY=your_api_key_here

**Setup Instructions**

1️⃣ Clone the Repository

    git clone https://github.com/Irfan-Alaam/RAG_task_ODCRU.git
    cd your-repo-name

2️⃣ Create Virtual Environment

    python -m venv env
    env\Scripts\activate   # Windows
    # source env/bin/activate  # Linux/Mac

3️⃣ Install Dependencies

    pip install -r requirements.txt
    (MAKE SURE THE PIP IS OF LATEST VERSION ELSE IT WILL SHOW TIMEOUT ERROR)

4️⃣ Run the Application

    python main.py

**########First run will:**
 1. Download and save embedding model
 2. Build ChromaDB vector store
 3. Subsequent runs are fast ⚡

## 💡 Usage Examples

1. What does -r option of ls command do?
2. Explain vim modes
3. How to install Linux on a virtual machine

> If an answer is not present in the dataset, the assistant will respond:
> **"I don't know based on the provided documentation."****

**SAMPLE OUTPUT**
<img width="1920" height="1080" alt="Screenshot (540)" src="https://github.com/user-attachments/assets/c504d27c-be7c-4df0-85d5-d04357c529c8" />
<img width="1920" height="1080" alt="Screenshot (539)" src="https://github.com/user-attachments/assets/b0f60769-3ed9-4ffe-8c9e-af3b07651aef" />
