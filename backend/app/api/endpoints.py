from fastapi import APIRouter, UploadFile, File
from ..services.image_processor import ImageProcessor

router = APIRouter()
image_processor = ImageProcessor()

@router.post("/enhance")
async def enhance_image(file: UploadFile = File(...)):
    """
    Enhance an uploaded image using OpenCV
    """
    # Read the uploaded file
    contents = await file.read()
    
    # Process the image
    image = image_processor.read_image(contents)
    enhanced = image_processor.enhance_image(image)
    
    # Convert back to bytes
    enhanced_bytes = image_processor.image_to_bytes(enhanced)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "enhanced_image": enhanced_bytes
    } 