import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_text(content: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents = [content],
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )
    return response


if __name__ == "__main__":
    generated_image_path = os.path.join(os.getcwd(), "./images/generated_image.png")
    prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
    res = create_text(prompt)

    for part in res.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            print("adasdasdas")
            image = Image.open(BytesIO(part.inline_data.data))
            image.save(generated_image_path)
            image.show()

