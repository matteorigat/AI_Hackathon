from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from pdfminer.layout import LTChar  #for titles
import fitz
import re


def format_text(output_dict):
    formatted_output = ""
    for page_num, text in output_dict.items():
        text = text.replace('\n', ' ')
        formatted_output += f"Page {page_num}:\n{text}\n\n"
    return formatted_output


def extract_text_from_pdf(pdf_path):
    text_per_page = {}
    for page_layout in extract_pages(pdf_path):
        page_text = ""
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()
        text_per_page[page_layout.pageid] = page_text
    return format_text(text_per_page)

def extract_images_and_formulas(pdf_path):
    images = []
    formulas = []
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        images.extend(image_list)
        formula_matches = re.findall(r'\$\$(.*?)\$\$', page.get_text())
        formulas.extend(formula_matches)
    return images, formulas

# Example usage
pdf_path = 'pdf/P1-10-sequence-learning.pdf'
text = extract_text_from_pdf(pdf_path)
#images, formulas = extract_images_and_formulas(pdf_path)

# Print or process extracted text, images, and formulas as needed
print("Extracted text:")
print(text)

"""print("\nExtracted images:")
for image in images:
    print(image)

print("\nExtracted formulas:")
for formula in formulas:
    print(formula)"""