from io import BytesIO
from PIL import Image
import numpy as np

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """
    Preprocess the uploaded image for the model.

    Args:
        image_bytes (bytes): The raw image bytes.
    Returns:
        np.ndarray: Preprocessed image ready for prediction.
    """
    # image = read_file_as_image(image_bytes)
    image = Image.open(BytesIO(image_bytes))
    image = image.resize((256, 256))
    image = np.array(image)
    return np.expand_dims(image, 0)  # Model expects a batch dimension