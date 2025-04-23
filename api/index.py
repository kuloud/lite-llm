from fastapi import FastAPI
from app.routers.github_models import router as github_models_router

app = FastAPI()

app.include_router(github_models_router)