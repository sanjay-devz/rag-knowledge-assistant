from document_loader import load_pdf


text = load_pdf("rag-knowledge-assistant\Data\Documents\50 Gen AI Product Ideas E2E.pdf")

print(text[:3000])