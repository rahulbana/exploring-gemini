import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_text(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [prompt],
        config= types.GenerateContentConfig(
            system_instruction="You are a helpful assistant. Consider I am class 5th student. Write in simple language.",
            temperature=0.7
        )
    )
    return response.text


if __name__ == "__main__":
    prompt = "Write an essay on the importance of AI in modern education."
    print(create_text(prompt))

