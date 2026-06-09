from fastapi import FastAPI
from app.rotas import chat, saude

app = FastAPI(title="SI IA")

app.include_router(saude.router)
app.include_router(chat.router)


@app.get("/")
def raiz():
    return {"mensagem": "Microsservico de IA do SI"}
