from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
from app.schemas.chat_request import ChatRequest
from app.services.github_models_service import ModelsService
from app.utils.logger import logger

router = APIRouter(tags=["WebSocket"])


@router.websocket("/ws")
async def websocket_github_model_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for interacting with GitHub models.

    This endpoint accepts WebSocket connections and handles different event types:
    - 'chat': Processes chat requests and streams responses from the GitHub model.
    - 'ping': Responds with a 'pong' message to check the connection status.

    Args:
        websocket (WebSocket): The WebSocket connection object.

    Returns:
        None: This function manages the WebSocket connection and sends messages back to the client.
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            try:
                request = json.loads(data)
                event_type = request.get("type")

                if event_type == "chat":
                    await handle_chat_event(websocket, request)
                elif event_type == "ping":
                    await handle_ping_event(websocket)
                else:
                    await handle_unsupported_event(websocket, event_type)
            except json.JSONDecodeError:
                await handle_json_error(websocket)
    except WebSocketDisconnect:
        logger.info("Client disconnected")


async def handle_chat_event(websocket: WebSocket, request: dict):
    try:
        chat_request = ChatRequest(**request.get("data", {}))
        logger.info(
            "Received chat request with %d messages", len(chat_request.messages)
        )

        async for chunk in ModelsService.chat_completions_stream(chat_request.messages):
            await websocket.send_text(
                json.dumps({"type": "chat_stream", "data": chunk})
            )

        await websocket.send_text(
            json.dumps({"type": "chat_end", "data": "Chat stream ended"})
        )
        logger.info("Successfully processed chat request")
    except ValueError as e:
        logger.error("Value error occurred during chat processing: %s", str(e))
        await websocket.send_text(
            json.dumps({"type": "error", "data": str(e), "status_code": 400})
        )
    except Exception as e:
        logger.error("An unexpected error occurred during chat processing: %s", str(e))
        await websocket.send_text(
            json.dumps(
                {
                    "type": "error",
                    "data": "An error occurred while processing the request.",
                    "status_code": 500,
                }
            )
        )


async def handle_ping_event(websocket: WebSocket):
    await websocket.send_text(json.dumps({"type": "pong", "data": "Pong response"}))


async def handle_unsupported_event(websocket: WebSocket, event_type: str):
    await websocket.send_text(
        json.dumps(
            {
                "type": "error",
                "data": f"Unsupported event type: {event_type}",
                "status_code": 400,
            }
        )
    )


async def handle_json_error(websocket: WebSocket):
    await websocket.send_text(
        json.dumps({"type": "error", "data": "Invalid JSON format", "status_code": 400})
    )
