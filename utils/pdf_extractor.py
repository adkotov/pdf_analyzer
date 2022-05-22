from utils.barcode_extractor import BarcodeExtractor
from utils.pdf_text_extractor import PdfTextExtractor
from utils.pdf_converter import convert_pdf_to_img


class PdfExtractor:
    """Class for getting info from pdf files"""
    
    def __init__(self, input_file_path, output_files_folder_path):
        self.input_file_path = input_file_path
        self.output_files_folder = output_files_folder_path
        self._text_extractor = PdfTextExtractor(self.input_file_path)
        self._barcode_extractor = BarcodeExtractor(f"{self.output_files_folder}test.png", self.output_files_folder)
        self.pdf_data = dict()

    def get_data_from_pdf_file(self) -> dict:
        self.pdf_data.update(self._text_extractor.get_text_from_pdf())
        convert_pdf_to_img(self.input_file_path, f"{self.output_files_folder}test.png")
        self._barcode_extractor.extract_barcode()
        self.pdf_data.update(self._barcode_extractor.barcodes)
        return self.pdf_data
    
    def get_num_of_pages(self) -> int:
        return self._text_extractor.get_num_of_pages()
    
def get_coordinates_data_from_dict(input_dict) -> dict:
    coordinate_dict = dict()
    for key, value in input_dict.items():
        if 'coordinates' not in value:
            return coordinate_dict
        else:
            coordinate_dict.update({key: value['coordinates']})
            coordinate_dict.update(get_coordinates_data_from_dict(value))
    return coordinate_dict
