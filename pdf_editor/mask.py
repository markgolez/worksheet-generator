import fitz  # PyMuPDF
from typing import Callable


def remove_pages_by_condition(
    pdf_path: str,
    output_path: str,
    condition: Callable[[int], bool]
) -> None:
    doc = fitz.open(pdf_path)
    pages_to_keep = [i for i in range(len(doc)) if not condition(i)]

    new_doc = fitz.open()
    for i in pages_to_keep:
        new_doc.insert_pdf(doc, from_page=i, to_page=i)

    new_doc.save(output_path)
    new_doc.close()
    doc.close()


if __name__ == "__main__":
    # Remove pages 3rd, 4th, 7th, 8th, 11th, 12th, ...
    remove_pages_by_condition(
        pdf_path="output1.pdf",
        output_path="output_filtered.pdf",
        condition=lambda i: (i - 2) % 4 in [0, 1]
    )
