import fitz
from typing import Tuple


def convert_pdf_to_img(input_path: str, output_path: str, pages: Tuple = None):
    """Method for convert pdf file to image"""

    pdf_input = fitz.open(input_path)
    output_files = []
    for pg in range(pdf_input.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        page = pdf_input[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        pix.save(output_path)
    pdf_input.close()
