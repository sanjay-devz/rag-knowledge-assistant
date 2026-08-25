def build_prompt(query: str, results: list[dict]) -> str:
    context = "\n\n".join(
        f"Context {i}: {result['chunk']}"
        for i, result in enumerate(results, start=1)
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using only the provided context.

If the answer cannot be found in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt.strip()