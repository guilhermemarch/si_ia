from app.configuracoes.config import carregar_configuracoes
from app.esquemas.chat import MensagemChat, RespostaChat
from app.provedores.provedor_groq import ProvedorGroq


class ServicoChatbot:
    def __init__(self):
        self.provedor = ProvedorGroq(carregar_configuracoes())

    def conversar(self, dados: MensagemChat) -> RespostaChat:
        contexto = dados.contexto.model_dump_json()
        resposta = self.provedor.gerar_resposta(dados.mensagem, contexto)
        return RespostaChat(resposta=resposta)
