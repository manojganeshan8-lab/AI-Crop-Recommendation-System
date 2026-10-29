# AI-Based Crop Recommendation System

A machine learning web application developed using Python, Flask, and Random Forest to recommend suitable crops and associated places based on soil nutrients and environmental conditions.

## Technologies
- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSV

## Features
- Crop prediction using a Random Forest Classifier
- Prediction based on N, P, K, temperature, humidity, pH, and rainfall
- Crop and place recommendation using a Tamil Nadu agricultural dataset
- Prediction history stored locally in CSV format
- Web interface for entering agricultural parameters

## Project Structure
- app.py - Flask application and prediction logic
- templates/index.html - Crop prediction form
- templates/history.html - Prediction history page
- tamilnadu_crop_dataset_1000.csv - Training dataset
- requirements.txt - Python dependencies

## How to Run

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Start the application:

   python app.py

5. Open http://127.0.0.1:5000 in your browser.

## Machine Learning
The application trains a Random Forest Classifier using seven agricultural features and predicts a crop-place combination.

Model accuracy has not yet been independently evaluated.

## Notes
- Prediction history is stored locally and excluded from Git.
- This is an academic machine learning project.
- Recommendations are experimental and should not replace professional agricultural advice.
