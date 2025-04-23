from fastapi import FastAPI
from app.routers.github_models import router as github_models_router
from app.routers.dia_router import router as dia_router

app = FastAPI()

app.include_router(github_models_router)
app.include_router(dia_router)