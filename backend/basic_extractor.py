import cv2
import numpy as np
import pytesseract

class ImprovedMetalTextExtractor:
    def __init__(self):
        print("✅ ImprovedMetalTextExtractor initialized")

    def extract_text_from_bytes(self, img_bytes):
        print("🔹 Converting bytes to image...")
        nparr = np.frombuffer(img_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is None:
            print("❌ Failed to decode image!")
            return "Error: Could not decode image"

        return self.extract_text_from_image(image)

    def extract_text_from_image(self, image):
        print("🔹 Converting image to grayscale...")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("🔹 Performing OCR...")
        text = pytesseract.image_to_string(gray)
        print(f"🟢 Extracted text: {text.strip()}")
        return text.strip()
