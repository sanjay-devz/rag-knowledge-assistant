from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks: list[str]):
    return model.encode(chunks)