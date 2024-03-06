import os
from app import app

def get_uploaded_images():
    """
    Retrieve the list of image filenames in the upload folder.
    """
    upload_folder = 'uploads'  # Assuming this is the name of your upload folder
    images = []
    for filename in os.listdir(upload_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images.append(filename)
    return images