import faiss
import numpy as np


def create_vector_store(embeddings):
    embeddings = np.asarray(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index


def search(index, query_embedding, top_k=3):
    query_embedding = np.asarray(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    return distances, indices