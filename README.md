# Tomato Disease Classification Project

This project implements a **Tomato Disease Classifier** using a **Convolutional Neural Network (CNN)** built with **TensorFlow** and **Keras**. The classifier is capable of identifying common tomato diseases from leaf images with **quite high accuracy**.

## Snapshot
![web snapshot](snapshots/snapshot1.png "Web Application Snapshot")

## Features
- **Deep Learning Model**: A CNN trained on a labeled dataset of tomato leaf images to detect diseases with **almost 100% accuracy on the test set**.
- **Interactive Web Interface**: A clean, user-friendly frontend built with **HTML**, **CSS**, and **JavaScript**, allowing users to upload images and view predictions.
- **FastAPI Backend**: A lightweight, high-performance API backend for serving predictions.
- **Real-Time Predictions**: Users can upload an image of a tomato leaf and get instant classification results, including a confidence score.

## Technologies Used
- **Frontend**:
  - HTML, CSS, JavaScript
  - Responsive design with a clean layout
- **Backend**:
  - **FastAPI** for handling API requests
  - TensorFlow/Keras for the machine learning model
- **Deployment**:
  - Easily deployable on any platform that supports Python and FastAPI
  - Model inference optimized for fast responses

## Highlights
- **High Accuracy**: Achieved **nearly 100% accuracy** on the test dataset, making the model highly reliable for real-world applications.
- **Image Preview**: Users can preview uploaded images before making predictions.
- **Confidence Visualization**: The interface displays a confidence score for the predicted disease class.

## Future Work
- Preprocess the input, since the model was trained with 256x256 pixel images.
- Improve web application.
- Make a mobile app that allows users to take photos with their phone.