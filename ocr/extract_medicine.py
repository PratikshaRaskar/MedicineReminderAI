import easyocr
import cv2

def extract_text(image_path):
    """
    Extract all text from a prescription image.
    """

    # Load EasyOCR only when needed
    reader = easyocr.Reader(['en'], gpu=False)

    image = cv2.imread(image_path)

    results = reader.readtext(image)

    extracted_text = ""

    for result in results:
        extracted_text += result[1] + "\n"

    return extracted_text
