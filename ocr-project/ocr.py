from pdf2image import covert_from_path
from PIL import Image
import pytesseract
import os

pdf_path = "prot.pdf"
output_txt = "endprot.txt"
tesseract_cmd = r"C:\"
idioma = "eng"
dpi = 300

pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

print("Convertando, aguarde um pouco")
pages = convert_from_path(pdf_path, dpi=dpi)

all_text = []
for i, page in enumerate(pages, start=1):
    print(f"Lendo página {i}...")
    text = pytesseract.image_to_string(pages, lang=idioma)
    all_text.append(f"---Page {i} --\n{text}\n")

with open(output_txt, "w" encoding="utf-8") as f: f.writelines(all_text)

print(f"Conversão concluida! Arquivo: '{output_txt}'")