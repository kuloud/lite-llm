from pydantic import BaseModel
from typing import List
from .message import Message

class ChatRequest(BaseModel):
    """
    A model representing a chat request.

    Attributes:
        messages (List[Message]): A list of Message objects representing the chat history.
    """
    messages: List[Message]
