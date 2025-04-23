from fastapi import FastAPI
from app.routers.github_models import router as github_models_router

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "FastAPI Service is running"}


app.include_router(github_models_router, prefix="/api", tags=["Models"])
