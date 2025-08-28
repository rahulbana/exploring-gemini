import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_embedding(texts: list, dim=768) -> list[float]:
    ''' Creates an embedding for the given content using the specified model and dimensionality. 
    Args:
        content (str): The content to be embedded.
        dim (int, optional): The dimensionality of the embedding. Two sizes are 768, 1536. Defaults to 768.
    Returns:
        list[float]: The generated embedding as a list of floats.
    '''
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents = texts,
        config=types.EmbedContentConfig(output_dimensionality=dim)
    )
    return response.embeddings


if __name__ == "__main__":
    texts = [
        "This is an apple."
    ]
    print(create_embedding(texts))

