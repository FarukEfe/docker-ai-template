from flask import Flask
import numpy as np
import joblib, logging

# Server Environment
PORT = 8000
HOST = "0.0.0.0"

# Log any info if need-be for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load .joblib model
model = joblib.load('app/model.joblib')

# Labels
class_names = np.array(['setosa','versicolor','virginica'])

# Create Flask app
app = Flask(__name__)

# Basic response for API root
@app.route("/")
def main_():
    return { "message" : "This is the root directory!!!" }

# Predict label based on sent post request data
@app.route('/predict', methods=['POST'])
def predict_(data: dict):
    features = np.array(data['features'].reshape(1,-1))
    prediction = model.predict(features)
    class_name = class_names[prediction][0] # Get the string label for model prediction
    return { 'prediction': class_name }

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)