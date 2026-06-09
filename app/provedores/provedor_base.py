from abc import ABC, abstractmethod


class ProvedorBase(ABC):
    @abstractmethod
    def gerar_resposta(self, mensagem: str, contexto: str) -> str:
        pass
