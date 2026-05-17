from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "mensagem": "API funcionando com sucesso",
        "projeto": "Jornada IA e Agentes"
    }


@router.get("/health")
def health():
    return {
        "status": "ok"
    }


@router.get("/ask")
def ask(pergunta: str):
    return {
        "pergunta": pergunta,
        "resposta": "Em breve esta rota será conectada ao GPT."
    }