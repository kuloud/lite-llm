from fastapi import FastAPI

app = FastAPI(title="FastAPI Service", version="1.0")

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "FastAPI Service is running"}