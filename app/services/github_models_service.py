
import os
from openai import OpenAI
from typing import List, Dict

class ModelsService:
    BASE_URL = "https://models.github.ai/inference"
    MODEL_NAME = "openai/gpt-4.1"
    TOKEN = os.getenv("GITHUB_TOKEN")

    @staticmethod
    def chat_completions(messages: List[Dict]) -> str:
        if not ModelsService.TOKEN:
            raise ValueError("GITHUB_TOKEN environment variable is not set.")

        client = OpenAI(
            base_url=ModelsService.BASE_URL,
            api_key=ModelsService.TOKEN,
        )

        response = client.chat.completions.create(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            model=ModelsService.MODEL_NAME,
        )

        return response.choices[0].message.content