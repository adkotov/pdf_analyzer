from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal


class PdfTextExtractor:
    """Class for extracting text data from pdf files"""

    def __init__(self, file_path: str) -> None:
        self.file_path  = file_path
        self.pdf_dict = dict()
        
    def get_num_of_pages(self) -> int:        
        return sum(1 for page in extract_pages(self.file_path))
    
    def get_text_from_pdf(self) -> dict():
        for page in extract_pages(self.file_path):
            for element in page:
                if isinstance(element, LTTextBoxHorizontal):
                    element_text = element.get_text()
                    if element.index == 0:
                        self.pdf_dict.update({
                            "title": {
                                "value": element_text.strip(),
                                "coordinates": [element.x0, element.y0]
                            }
                        })
                    elif element.index == 19:
                        self.notes = element_text.strip().replace(":","")
                        self.pdf_dict.update({
                            self.notes: {
                                "coordinates": [element.x0, element.y0]
                            },
                        })
                    elif element.index>19:
                        self.pdf_dict[self.notes].update({
                            element_text.strip():{
                                "coordinates": [element.x0, element.y0]
                            }
                        })
                    else:
                        key, value = element_text.split(":")
                        self.pdf_dict.update({
                            key: {
                                "value": value.strip(),
                                "coordinates": [element.x0, element.y0]
                            }
                        })
        return self.pdf_dict
