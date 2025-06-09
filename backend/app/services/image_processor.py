import cv2
import numpy as np
from PIL import Image
import io

class ImageProcessor:
    @staticmethod
    def read_image(image_bytes: bytes) -> np.ndarray:
        """Convert image bytes to numpy array"""
        nparr = np.frombuffer(image_bytes, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    @staticmethod
    def enhance_image(image: np.ndarray) -> np.ndarray:
        """Apply basic image enhancement"""
        # Convert to LAB color space
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Apply CLAHE to L channel
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        
        # Merge channels
        merged = cv2.merge((cl, a, b))
        
        # Convert back to BGR
        enhanced = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
        
        return enhanced

    @staticmethod
    def image_to_bytes(image: np.ndarray) -> bytes:
        """Convert numpy array to bytes"""
        success, buffer = cv2.imencode('.png', image)
        if not success:
            raise Exception("Failed to encode image")
        return buffer.tobytes() 