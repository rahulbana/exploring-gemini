import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_image_description(prompt: str, image_path_1: str, image_path_2: str) -> str:
    uploaded_file = client.files.upload(file=image_path_1)

    with open(image_path_2, 'rb') as f:
        img2_bytes = f.read()


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [
            prompt,
            uploaded_file,
            types.Part.from_bytes(
                data=img2_bytes,
                mime_type='image/png',
            ),
        ]
    )
    return response.text


if __name__ == "__main__":
    prompt = "What is different between these two images?"
    image_path_1 = os.path.join(os.getcwd(), "./images/img-india.png")
    image_path_2 = os.path.join(os.getcwd(), "./images/img-eng.png")
    print(get_image_description(prompt, image_path_1, image_path_2))

