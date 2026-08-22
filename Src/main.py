from document_loader import load_pdf


text = load_pdf("Src\Documents\50 Gen AI Product Ideas E2E.pdf")

print(text[:3000])