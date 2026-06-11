# SI - Soluções Imobiliárias (IA)

Microsserviço de chatbot. FastAPI + Groq. Recebe contexto do backend e devolve a resposta.

Não acessa banco de dados. O frontend não chama este serviço direto.

## Configuração

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=
GROQ_MODEL=llama-3.1-8b-instant
PORT=8000
```

Sem `GROQ_API_KEY`, o serviço sobe mas o chat retorna aviso de chave ausente.

## Rodar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Rotas

- `GET /saude` — health check
- `POST /chat/conversa` — mensagem + contexto (leads, imóveis, resumo)

## Docker

```bash
docker build -t si-ia .
docker run --env-file .env -p 8000:8000 si-ia
```
