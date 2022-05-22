import json
import pytest
from utils.pdf_extractor import PdfExtractor
from utils.pdf_extractor import get_coordinates_data_from_dict


def test_pdf_consists_of_one_page(init_extractor):
    assert init_extractor.get_num_of_pages() == 1, "Num of page isn't 1"

def test_pdf_contains_all_fields(get_dictionary_from_pdf):
    assert get_dictionary_from_pdf['expected_dict'].keys() == get_dictionary_from_pdf['actual_dict'].keys(), "Pdf file isn't contains all expected fields"

def test_pdf_fields_has_correct_positions(get_dictionary_from_pdf):
    expected_coordinates = get_coordinates_data_from_dict(get_dictionary_from_pdf['expected_dict'])
    actual_coordinates = get_coordinates_data_from_dict(get_dictionary_from_pdf['actual_dict'])
    assert expected_coordinates == actual_coordinates, "Fields in Pdf file has incorrect position"
