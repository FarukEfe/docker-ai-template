from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('model.joblib')

class_names = np.array(['setosa','versicolor','virginica'])

app = FastAPI()

# Basic response for API root
@app.get('/')
def read_root():
    return {'message': 'Iris model API'}

# Predict label based on sent post request data
@app.post('/predict')
def predict(data: dict):
    features = np.array(data['features'].reshape(1,-1))
    prediction = model.predict(features)
    class_name = class_names[prediction][0] # Get the string label for model prediction
    return {'prediction': class_name}
