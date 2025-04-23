from fastapi import APIRouter, HTTPException
from app.services.dia_service import DiaService
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["Dia"])

class DiaRequest(BaseModel):
    text: str
    output_path: str = "simple.mp3"

@router.post("/dia/generate", summary="Generate audio using Dia model")
async def generate_audio(request: DiaRequest):
    """
    Generate audio from the given text using the Dia model.

    Args:
        request (DiaRequest): The request containing the input text and output path.

    Returns:
        dict: A dictionary containing the path of the generated audio file.
    """
    try:
        audio_path = DiaService.generate_audio(request.text, request.output_path)
        return {"audio_path": audio_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
