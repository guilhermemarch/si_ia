from typing import Any

from pydantic import BaseModel, Field


class ContextoSistema(BaseModel):
    leads: list[dict[str, Any]] = Field(default_factory=list)
    imoveis: list[dict[str, Any]] = Field(default_factory=list)
    resumo: dict[str, Any] = Field(default_factory=dict)


class MensagemChat(BaseModel):
    mensagem: str
    contexto: ContextoSistema


class RespostaChat(BaseModel):
    resposta: str
