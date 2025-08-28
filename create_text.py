import os
from dotenv import load_dotenv
load_dotenv()

from google import genai


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_text(content: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [content]
    )
    print(response)
    return response.text


if __name__ == "__main__":
    prompt = "Write an essay on the importance of AI in modern education."
    print(create_text(prompt))

