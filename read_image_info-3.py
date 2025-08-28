import os
import requests
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_image_description(prompt: str, image_path: str) -> str:
    image_bytes = requests.get(image_path).content
    image = types.Part.from_bytes(
        data=image_bytes, mime_type="image/jpeg"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [
            prompt, image
        ]
    )
    return response.text


if __name__ == "__main__":
    prompt = "What is this image?"
    image_path = "https://goo.gle/instrument-img"
    print(get_image_description(prompt, image_path))

