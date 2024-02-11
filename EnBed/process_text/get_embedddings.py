from openai import OpenAI
client = OpenAI()


def get_embeddings(text: str) -> str:
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )
    return response.data[0].embedding
