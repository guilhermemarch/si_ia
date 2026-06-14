import httpx

from app.configuracoes.config import Configuracoes

PROMPT_SISTEMA = (
    "Voce e um assistente de CRM imobiliario. "
    "Responda em portugues do Brasil, de forma curta e direta. "
    "Use somente os dados recebidos no contexto. "
    "Se faltar informacao, diga isso claramente."
)


class ProvedorNvidia:
    def __init__(self, config: Configuracoes):
        self.config = config

    def gerar_resposta(self, mensagem: str, contexto: str) -> str:
        if not self.config.nvidia_api_key:
            return (
                "A chave da NVIDIA nao foi configurada. "
                "Configure NVIDIA_API_KEY para usar o chatbot."
            )

        url = f"{self.config.nvidia_base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.config.nvidia_api_key}",
            "Accept": "application/json",
        }
        payload: dict = {
            "model": self.config.nvidia_model,
            "messages": [
                {"role": "system", "content": PROMPT_SISTEMA},
                {
                    "role": "user",
                    "content": f"Contexto do sistema:\n{contexto}\n\nPergunta: {mensagem}",
                },
            ],
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature,
            "top_p": self.config.top_p,
            "stream": False,
        }

        if self.config.enable_thinking:
            payload["chat_template_kwargs"] = {"enable_thinking": True}

        try:
            with httpx.Client(timeout=60.0) as cliente:
                resposta = cliente.post(url, headers=headers, json=payload)
                resposta.raise_for_status()
                dados = resposta.json()
        except httpx.HTTPStatusError as erro:
            status = erro.response.status_code
            if status == 413:
                return "O contexto enviado e muito grande. Tente uma pergunta mais especifica."
            if status == 429:
                return "Limite de requisicoes da API atingido. Tente novamente em instantes."
            if status in (401, 403):
                return "Chave da NVIDIA invalida ou sem permissao. Verifique NVIDIA_API_KEY."
            return f"Erro na API de IA (codigo {status}). Tente novamente."
        except httpx.TimeoutException:
            return "A API de IA demorou para responder. Tente novamente."
        except httpx.RequestError:
            return "Nao foi possivel conectar a API de IA. Tente novamente."

        try:
            conteudo = dados["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            return "Nao consegui gerar uma resposta agora."

        return conteudo or "Nao consegui gerar uma resposta agora."
