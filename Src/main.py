from document_loader import load_pdf
from text_chunker import chunk_text


pdf_path = "50_Gen_AI_Product_Ideas_E2E.pdf"

text = load_pdf(pdf_path)

chunks = chunk_text(text)

print(f"Total characters: {len(text)}")
print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:5], start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)