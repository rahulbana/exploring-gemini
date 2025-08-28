import os
from dotenv import load_dotenv
load_dotenv()

from google import genai


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_text(content: str) -> str:
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents = [content]
    )
    return response


if __name__ == "__main__":
    prompt = "Write an essay on the importance of AI in modern education."
    for chunk in create_text(prompt):
        print(chunk.text, end="", flush=True)
    
