from typing import List
import fitz  # PyMuPDF


def add_header_and_crop(
    pdf_path: str,
    output_path: str,
    pages_with_headers: List[int],
    header_text: str,
    crop_top: float = 200.0,
    crop_bottom: float = 50.0,
    mask_top: float = 200.0,
    mask_bottom: float = 50.0
) -> None:
    """
    Reads a PDF, adds headers to specific pages, and crops the top/bottom of those pages.
    All other pages only have the bottom cropped.

    :param pdf_path: Path to the input PDF.
    :param output_path: Path to save the modified PDF.
    :param pages_with_headers: List of page indices (0-based) to add the header and crop top.
    :param header_text: Text to insert as header.
    :param crop_top: Points to crop from the top of selected pages.
    :param crop_bottom: Points to crop from the bottom of all pages.
    """
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        rect = page.rect

        new_rect = fitz.Rect(
            rect.x0,
            rect.y0,
            rect.x1,
            rect.y1 - crop_bottom
        )
        # Crop rectangle

        if page_num % 2 == 0:
            # Mask top area
            top_rect = fitz.Rect(rect.x0, rect.y0, rect.x1,
                                 rect.y0 + mask_top)
            page.draw_rect(top_rect, color=(1, 1, 1), fill=(1, 1, 1))
        page.set_cropbox(new_rect)

        # Add header if in selected pages
        if page_num % 2 == 0:
            header_rect = fitz.Rect(
                rect.x0, rect.y0, rect.x1,
                rect.y0 + mask_top)
            page.insert_textbox(
                header_rect,
                header_text,
                fontsize=12,
                fontname="helv",
                color=(0, 0, 0),
                align=1
            )

    doc.save(output_path)
    doc.close()


if __name__ == "__main__":
    add_header_and_crop(
        pdf_path="quiz.pdf",
        output_path="output1.pdf",
        pages_with_headers=[0, 2, 4],
        header_text="\nSaint Joseph Convent School - English Program\n Semester 1 | SY 2025-2026\n G10 Advanced Math Quiz\n"
        "Name: _____________________ Nickname: ___________ G10/____ Date: __________ Score: _______\n",
        crop_top=0,
        crop_bottom=50,
        mask_top=107.5,
        mask_bottom=50.0
    )
