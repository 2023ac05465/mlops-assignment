"""
Predit using the trained model
"""
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/linear_regression_model.joblib')
model_decision_tree = joblib.load('model/decision_tree_model.joblib')

@app.route('/predict/linearregression', methods=['POST'])
def predict_linear_regression():
    data = request.json
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/predict/decisiontree', methods=['POST'])
def predict_decision_tree():
    data = request.json
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
