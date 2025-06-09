from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from ..services.image_processor import ImageProcessor
import os
from datetime import datetime

router = APIRouter()
image_processor = ImageProcessor()

@router.post("/enhance")
async def enhance_image(file: UploadFile = File(...)):
    """
    Enhance an uploaded image using OpenCV
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")

        # Read the uploaded file
        contents = await file.read()
        
        # Process the image
        image = image_processor.read_image(contents)
        enhanced = image_processor.enhance_image(image)
        
        # Convert back to bytes
        enhanced_bytes = image_processor.image_to_bytes(enhanced)
        
        # Generate a unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"enhanced_{timestamp}_{file.filename}"
        filepath = os.path.join("uploads", filename)
        
        # Save the enhanced image
        with open(filepath, "wb") as f:
            f.write(enhanced_bytes)
        
        return {
            "message": "Image enhanced successfully",
            "filename": filename,
            "filepath": filepath
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 