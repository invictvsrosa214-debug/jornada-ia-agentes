from fastapi import FastAPI

app = FastAPI(
    title="API GPT - Jornada IA",
    description="Primeira API da jornada de IA e agentes",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "API funcionando com sucesso",
        "projeto": "Jornada IA e Agentes"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/ask")
def ask(pergunta: str):
    return {
        "pergunta": pergunta,
        "resposta": "Em breve esta rota será conectada ao GPT."
    }