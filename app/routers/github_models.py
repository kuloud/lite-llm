import logging

from fastapi import APIRouter, HTTPException
from app.schemas.chat_request import ChatRequest
from app.services.github_models_service import ModelsService

from app.utils.logger import logger

router = APIRouter(prefix="/models", tags=["Models"])


@router.post("/chat", summary="Chat with GitHub Models")
async def chat_with_models(request: ChatRequest):
    """
    Handle chat requests with GitHub models.

    Args:
        request (ChatRequest): The chat request containing a list of messages.

    Returns:
        dict: A dictionary containing the response from the model.

    Raises:
        HTTPException: If a ValueError occurs, return a 400 status code.
                       If any other exception occurs, return a 500 status code.
    """
    try:
        logger.info("Received chat request with %d messages", len(request.messages))
        response = ModelsService.chat_completions(request.messages)
        logger.info("Successfully processed chat request")
        return {"response": response}
    except ValueError as e:
        logger.error("Value error occurred during chat processing: %s", str(e))
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("An unexpected error occurred during chat processing: %s", str(e))
        raise HTTPException(
            status_code=500, detail="An error occurred while processing the request."
        )
