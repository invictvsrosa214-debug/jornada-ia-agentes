from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="API GPT - Jornada IA",
    description="Primeira API da jornada de IA e agentes",
    version="0.2.0"
)

app.include_router(router)