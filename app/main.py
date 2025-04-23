from fastapi import FastAPI

from app.routers import github_models

app = FastAPI(title="FastAPI Service", version="1.0")


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "FastAPI Service is running"}


app.include_router(github_models.router, prefix="/api", tags=["Models"])
