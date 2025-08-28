import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_image_description(prompt: str, image_full_path: str) -> str:
    with open(image_full_path, 'rb') as f:
      image_bytes = f.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [
            types.Part.from_bytes(
                data=image_bytes,
                mime_type='image/jpeg',
            ),
            prompt
        ]
    )
    return response.text


if __name__ == "__main__":
    prompt = "What is in the image. Explain in brief"
    image_full_path = os.path.join(os.getcwd(), "./images/human_organs.jpg")
    print(get_image_description(prompt, image_full_path))

