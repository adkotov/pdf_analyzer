import json
import pytest
from utils.pdf_extractor import PdfExtractor


input_file_path = "test_data/test.pdf"
output_files_folder_path = "test_data/"

@pytest.fixture(scope="session")
def init_extractor():
    extractor = PdfExtractor(input_file_path, output_files_folder_path)
    return extractor

@pytest.fixture(scope="session")
def get_template_dictionary():
    with open('test_data/template.json') as template_json:
        expected_dict = json.load(template_json)
        return expected_dict

@pytest.fixture(scope="session")
def get_dictionary_from_pdf(init_extractor, get_template_dictionary):
    return {
        "expected_dict": get_template_dictionary,
        "actual_dict": init_extractor.get_data_from_pdf_file()
    }
