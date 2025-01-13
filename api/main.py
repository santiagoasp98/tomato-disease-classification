from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
import tensorflow as tf
from pathlib import Path
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils.utils import preprocess_image


# ------------------------------------------------- #
# Configuration and Constants
# ------------------------------------------------- #

# Get the absolute path to the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the model and define class names
MODEL_PATH = BASE_DIR / 'saved_models' / 'v3' / 'model.keras'
MODEL = tf.keras.models.load_model(str(MODEL_PATH))
CLASS_NAMES = [
    'Early blight',
    'Late blight',
    'Yellow Leaf Curl Virus',
    'Healthy'
]

# ------------------------------------------------- #
# FastAPI Application Setup
# ------------------------------------------------- #

app = FastAPI(
    title="Tomato Disease Classification API",
    description="An API for classifying tomato diseases using deep learning models.",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# ------------------------------------------------- #
# API Endpoints
# ------------------------------------------------- #

@app.get('/ping', summary="Health Check")
async def ping():
    """
    Health check endpoint to ensure the API is running.
    """
    return {"message": "Server is healthy!"}

@app.post('/predict', summary="Classify Plant Disease")
async def predict(file: UploadFile = File(...)):
    """
    Handles image classification requests by accepting an uploaded image file,
    preprocessing it, making a prediction using the loaded model, and returning
    the result.

    Args:
        file (UploadFile): The uploaded image file.
    Returns:
        dict: Predicted class and confidence score, or an error message.
    """
    try:
        # Read and preprocess the uploaded image
        image_bytes = await file.read()
        img_batch = preprocess_image(image_bytes)

        # Make predictions
        predictions = MODEL.predict(img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))

        return {
            "class": predicted_class,
            "confidence": confidence
        }
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

# ------------------------------------------------- #
# Application Entry Point
# ------------------------------------------------- #

# Mount static files for serving frontend
app.mount(
    '/',
    StaticFiles(directory=str(BASE_DIR / 'frontend'), html=True),
    name='frontend'
)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)