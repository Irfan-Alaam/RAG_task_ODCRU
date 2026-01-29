from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="UI/static"), name="static")

rag = None
def set_rag(rag_instance):
    global rag
    rag = rag_instance
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("UI/template/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.post("/ask")
async def ask(payload: dict):
    question = payload.get("question")
    answer = rag.ask(question)
    return JSONResponse({"answer": answer})