from groq import Groq

from app.configuracoes.config import Configuracoes
from app.provedores.provedor_base import ProvedorBase


class ProvedorGroq(ProvedorBase):
    def __init__(self, config: Configuracoes):
        self.config = config
        self.cliente = Groq(api_key=config.groq_api_key) if config.groq_api_key else None

    def gerar_resposta(self, mensagem: str, contexto: str) -> str:
        if not self.cliente:
            return "A chave da Groq nao foi configurada. Configure GROQ_API_KEY para usar o chatbot."

        resposta = self.cliente.chat.completions.create(
            model=self.config.groq_model,
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Voce e um assistente de CRM imobiliario. "
                        "Responda em portugues do Brasil, de forma curta e direta. "
                        "Use somente os dados recebidos no contexto. "
                        "Se faltar informacao, diga isso claramente."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Contexto do sistema:\n{contexto}\n\nPergunta: {mensagem}",
                },
            ],
        )

        conteudo = resposta.choices[0].message.content
        return conteudo or "Nao consegui gerar uma resposta agora."
