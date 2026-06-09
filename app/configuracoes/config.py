import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Configuracoes:
    groq_api_key: str
    groq_model: str
    port: int


def carregar_configuracoes() -> Configuracoes:
    return Configuracoes(
        groq_api_key=os.getenv("GROQ_API_KEY", ""),
        groq_model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        port=int(os.getenv("PORT", "8000")),
    )
