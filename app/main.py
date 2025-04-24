import os
from app.services.github_models_service import ModelsService


from fastapi import FastAPI
from app.routers.github_models import router as github_models_router
from app.routers.websocket_router import router as websocket_router


app = FastAPI(
    title="FastAPI Service",
    version="1.0",
    description="A FastAPI service for GitHub models.",
)

ModelsService.set_config(
    token=os.getenv("GITHUB_TOKEN"),
    base_url=os.getenv("BASE_URL"),
    model_name=os.getenv("MODEL_NAME"),
)


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "FastAPI Service is running"}


app.include_router(github_models_router, prefix="/api")
app.include_router(websocket_router)
