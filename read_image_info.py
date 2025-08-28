import os
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

from google import genai


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_image_description(prompt: str, image_full_path: str) -> str:
    image = Image.open(image_full_path)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [image, prompt]
    )
    return response.text


if __name__ == "__main__":
    prompt = "What is in the image. Explain in brief"
    image_full_path = os.path.join(os.getcwd(), "./images/human_organs.jpg")
    print(get_image_description(prompt, image_full_path))

