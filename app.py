"""
Predit using the trained model
"""
from flask import Flask, request, jsonify
import joblib
import numpy as np
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
model = joblib.load('model/linear_regression_model.joblib')
model_decision_tree = joblib.load('model/decision_tree_model.joblib')

# Store logs in memory
logs = []

# Prometheus Metrics
REQUEST_COUNT = Counter("predict_requests_total", "Total prediction requests")
LINEARREGRESSION_REQUEST_LATENCY = Histogram("predict_linearregression_request_latency_seconds", 
                                             "Latency for lineargregression model prediction requests")
DECISIONTREE_REQUEST_LATENCY = Histogram("predict_decisiontree_request_latency_seconds", 
                                         "Latency for decisiontree model prediction requests")

@LINEARREGRESSION_REQUEST_LATENCY.time()
@app.route('/predict/linearregression', methods=['POST'])
def predict_linear_regression():
    """ Predict using the linear regression model
    """
    REQUEST_COUNT.inc()
    data = request.json
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)

    # Log result
    log_entry = {
        "input": data['input'],
        "model": "Linear Regression",
        "prediction": prediction.tolist()
    }
    logs.append(log_entry)

    return jsonify({'prediction': prediction.tolist()})

@DECISIONTREE_REQUEST_LATENCY.time()
@app.route('/predict/decisiontree', methods=['POST'])
def predict_decision_tree():
    """ Predict using the decision tree model
    """
    REQUEST_COUNT.inc()
    data = request.json
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    # Log result
    log_entry = {
        "input": data['input'],
        "model": "Decision Tree",
        "prediction": prediction.tolist()
    }
    logs.append(log_entry)

    return jsonify({'prediction': prediction.tolist()})

@app.route("/logs")
def get_logs():
    """ 
    Get the logs of predictions
    
    """
    return logs

# Metrics endpoint for Prometheus
@app.route("/metrics")
def metrics():
    """
    Expose metrics for Prometheus
    """
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
