import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from utils.pdf_analyzer import PdfAnalyser


pdf_analyzer = PdfAnalyser('../test_data/test.pdf')
# print(pdf_analyzer.get_num_of_pages())
# print(pdf_analyzer.get_text_from_pdf())

pdf_analyzer.get_element()