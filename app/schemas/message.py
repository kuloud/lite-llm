from pydantic import BaseModel

class Message(BaseModel):
    """
    A model representing a message in a chat.

    Attributes:
        role (str): The role of the message sender, e.g., 'user', 'assistant'.
        content (str): The content of the message.
    """
    role: str
    content: str