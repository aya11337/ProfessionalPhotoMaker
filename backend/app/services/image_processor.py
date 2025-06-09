import cv2
import numpy as np
from PIL import Image
import io
from rembg import remove

class ImageProcessor:
    @staticmethod
    def read_image(image_bytes: bytes) -> np.ndarray:
        """Convert image bytes to numpy array"""
        try:
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if image is None:
                raise ValueError("Failed to decode image")
            return image
        except Exception as e:
            raise ValueError(f"Error reading image: {str(e)}")

    @staticmethod
    def remove_background(image: np.ndarray) -> np.ndarray:
        """Remove background from image"""
        try:
            # Convert to PIL Image
            pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            
            # Remove background
            output = remove(pil_image)
            
            # Convert back to OpenCV format
            output_array = np.array(output)
            return cv2.cvtColor(output_array, cv2.COLOR_RGB2BGR)
        except Exception as e:
            raise ValueError(f"Error removing background: {str(e)}")

    @staticmethod
    def enhance_image(image: np.ndarray) -> np.ndarray:
        """Apply professional image enhancement"""
        try:
            # Remove background
            image = ImageProcessor.remove_background(image)
            
            # Convert to LAB color space
            lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
            
            # Apply CLAHE to L channel
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
            cl = clahe.apply(l)
            
            # Enhance contrast
            cl = cv2.convertScaleAbs(cl, alpha=1.2, beta=10)
            
            # Merge channels
            merged = cv2.merge((cl, a, b))
            
            # Convert back to BGR
            enhanced = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
            
            # Apply sharpening
            kernel = np.array([[-1,-1,-1],
                             [-1, 9,-1],
                             [-1,-1,-1]])
            enhanced = cv2.filter2D(enhanced, -1, kernel)
            
            # Adjust saturation
            hsv = cv2.cvtColor(enhanced, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)
            s = cv2.multiply(s, 1.2)  # Increase saturation by 20%
            hsv = cv2.merge([h, s, v])
            enhanced = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            
            return enhanced
        except Exception as e:
            raise ValueError(f"Error enhancing image: {str(e)}")

    @staticmethod
    def image_to_bytes(image: np.ndarray) -> bytes:
        """Convert numpy array to bytes"""
        try:
            success, buffer = cv2.imencode('.png', image)
            if not success:
                raise ValueError("Failed to encode image")
            return buffer.tobytes()
        except Exception as e:
            raise ValueError(f"Error converting image to bytes: {str(e)}") 