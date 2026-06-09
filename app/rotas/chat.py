from fastapi import APIRouter

from app.esquemas.chat import MensagemChat, RespostaChat
from app.servicos.servico_chatbot import ServicoChatbot

router = APIRouter(prefix="/chat")
servico_chatbot = ServicoChatbot()


@router.post("/conversa", response_model=RespostaChat)
def conversar(dados: MensagemChat):
    return servico_chatbot.conversar(dados)
