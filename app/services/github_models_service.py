import os
from openai import OpenAI
from typing import List, Dict
from app.utils.logger import logger


class ModelsService:
    BASE_URL = "https://models.github.ai/inference"
    MODEL_NAME = "openai/gpt-4.1"
    TOKEN = os.getenv("GITHUB_TOKEN")

    @classmethod
    def set_config(cls, token=None, base_url=None, model_name=None):
        if token is not None:
            cls.TOKEN = token
        if base_url is not None:
            cls.BASE_URL = base_url
        if model_name is not None:
            cls.MODEL_NAME = model_name

    @classmethod
    def chat_completions(cls, messages: List[Dict]) -> str:
        if not cls.TOKEN:
            raise ValueError("GITHUB_TOKEN environment variable is not set.")

        client = OpenAI(
            base_url=cls.BASE_URL,
            api_key=cls.TOKEN,
        )

        response = client.chat.completions.create(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            model=cls.MODEL_NAME,
        )

        return response.choices[0].message.content

    @classmethod
    async def chat_completions_stream(cls, messages: List[Dict]):
        if not cls.TOKEN:
            raise ValueError("GITHUB_TOKEN environment variable is not set.")

        client = OpenAI(
            base_url=cls.BASE_URL,
            api_key=cls.TOKEN,
        )

        try:
            stream = client.chat.completions.create(
                messages=messages,
                temperature=1.0,
                top_p=1.0,
                model=cls.MODEL_NAME,
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            logger.error(f"Error in chat_completions_stream: {str(e)}")
            raise
