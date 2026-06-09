# SI IA

Microsservico FastAPI responsavel por gerar respostas do chatbot usando Groq e contexto enviado pelo backend.

## Tecnologias

- Python
- FastAPI
- Pydantic
- Groq
- python-dotenv
- Uvicorn

## Papel no sistema

Este servico nao acessa o banco de dados e nao deve receber chamadas diretas do frontend.

Fluxo correto:

```txt
Frontend -> Backend -> IA -> Groq
```

O backend envia a mensagem do usuario e um contexto com leads, imoveis e resumo do sistema.

## Configuracao

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Exemplo:

```env
GROQ_API_KEY=""
GROQ_MODEL="llama-3.1-8b-instant"
PORT=8000
```

Sem `GROQ_API_KEY`, o servico sobe normalmente, mas o chatbot retorna uma mensagem informando que a chave nao foi configurada.

## Instalacao local

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

## Execucao local

```bash
uvicorn app.main:app --reload --port 8000
```

## Docker

Build da imagem:

```bash
docker build -t case-imoveis-ia .
```

Execucao da imagem:

```bash
docker run --env-file .env -p 8000:8000 case-imoveis-ia
```

## Rotas

Health check:

```txt
GET /saude
```

Resposta:

```json
{
  "status": "ok"
}
```

Chat:

```txt
POST /chat/conversa
```

Payload:

```json
{
  "mensagem": "Quantos leads estao em negociacao?",
  "contexto": {
    "leads": [],
    "imoveis": [],
    "resumo": {}
  }
}
```

Resposta:

```json
{
  "resposta": "Atualmente existem leads em negociacao..."
}
```

## Decisoes tecnicas

- O servico recebe contexto pronto do backend.
- O prompt orienta respostas curtas, em portugues e baseadas apenas nos dados recebidos.
- A integracao com Groq fica isolada em `provedores/provedor_groq.py`.
- A regra de negocio do chatbot fica em `servicos/servico_chatbot.py`.

## Proximos passos

- Ajustar prompt conforme testes reais com dados do CRM.
- Adicionar logs simples para diagnostico.
- Adicionar testes automatizados em uma etapa futura.
