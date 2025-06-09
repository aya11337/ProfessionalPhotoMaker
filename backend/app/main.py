from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from .api.endpoints import router as image_router

app = FastAPI(
    title="Professional Photo Maker API",
    description="API for professional photo enhancement using OpenCV",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory if it doesn't exist
os.makedirs("uploads", exist_ok=True)

# Include the image processing router
app.include_router(image_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Professional Photo Maker API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                }
                h1 {
                    color: #333;
                    border-bottom: 2px solid #eee;
                    padding-bottom: 10px;
                }
                .endpoint {
                    background: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 10px 0;
                }
                code {
                    background: #e0e0e0;
                    padding: 2px 5px;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <h1>Professional Photo Maker API</h1>
            <p>Welcome to the Professional Photo Maker API. This API provides endpoints for image enhancement using OpenCV.</p>
            
            <h2>Available Endpoints:</h2>
            <div class="endpoint">
                <h3>POST /api/enhance</h3>
                <p>Enhance an uploaded image using OpenCV.</p>
                <p>Send a POST request with an image file to enhance it.</p>
            </div>

            <h2>API Documentation:</h2>
            <p>For detailed API documentation, visit:</p>
            <ul>
                <li><a href="/docs">Swagger UI Documentation</a></li>
                <li><a href="/redoc">ReDoc Documentation</a></li>
            </ul>
        </body>
    </html>
    """

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": f"An error occurred: {str(exc)}"}
    ) 