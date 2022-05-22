from pyzbar import pyzbar
import cv2


class BarcodeExtractor:
    """Class for extracting barcodes from image and save received 
       barcodes as png files 
    """
    
    def __init__(self, file_path: str, output_folder: str):
        self.file_path = file_path
        self.output_folder = output_folder
        self.barcodes = dict()

    def extract_barcode(self):
        self.image = cv2.imread(self.file_path)
        self.decode_barcode_from_image()
    
    def decode_barcode_from_image(self):
        decoded_objects = pyzbar.decode(self.image)
        count = 1
        for object in decoded_objects:
            barcode_coordinates = self.get_barcode_coordinates(object)
            self.save_barcode(barcode_coordinates, count, object.data)
            count += 1
   
    def get_barcode_coordinates(self, object):
        return min(object.polygon) + max(object.polygon)
    
    def save_barcode(self, coordinates, count, barcode_data):
        crop_image = self.image[coordinates[1]: coordinates[3], coordinates[0]: coordinates[2]]
        barcode_path = f"{self.output_folder}barcode_{count}.png"
        cv2.imwrite(barcode_path, crop_image)
        self.barcodes.update({
            f"barcode_{count}": {
                "barcode_path": barcode_path,
                "data": barcode_data.decode("UTF-8"),
                "coordinates": [
                    coordinates[0],
                    coordinates[1]
                ]
            }
        })
