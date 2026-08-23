from document_loader import load_pdf
from text_chunker import chunk_text
from embedder import create_embeddings
from vector_store import create_vector_store
from retriever import retrieve
from numpy import py

pdf_path = "50_Gen_AI_Product_Ideas_E2E.pdf"

# 1. Load PDF
text = load_pdf(pdf_path)

# 2. Chunk text
chunks = chunk_text(text)

# 3. Create embeddings
embeddings = create_embeddings(chunks)

# 4. Create FAISS vector store
index = create_vector_store(embeddings)

# 5. Ask a question
query = input("Ask a question: ")

# 6. Retrieve relevant chunks
results = retrieve(query, chunks, index, top_k=3)

# 7. Display results
for i, result in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(f"Distance: {result['distance']:.4f}")
    print(result["chunk"])