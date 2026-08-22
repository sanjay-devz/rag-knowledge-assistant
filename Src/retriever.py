from embedder import model


def retrieve(query: str, chunks: list[str], index, top_k: int = 3):
    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for distance, index_number in zip(distances[0], indices[0]):
        results.append({
            "chunk": chunks[index_number],
            "distance": float(distance)
        })

    return results