"""
This module it to train the model
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import joblib
import mlflow


# Load the dataset
print("Loading dataset...")
data = pd.read_csv('Housing.csv')
data.head()

# Clean the dataset
data = data.dropna()

# Encode categorical features
train_df_object = data.select_dtypes(include='object')
encoders = {}
for col in train_df_object.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le


# Features (X) and target (y)
data = data.drop(columns=['ocean_proximity'])
x = data.drop(columns=['median_house_value'])
y = data['median_house_value']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Before we start training the model, we will set up MLflow to track our experiments.
# Experiment : In MLflow an experiment acts as a container that holds all the runs
# RUN: A run represents a single execution of a machine learning model,
# including its parameters, metrics and results.

# By default MLflow will log the runs in the local file system under mlruns directory

def train_with_linear_regression():
    """
    Train a linear regression model and log the results using MLflow"""
    # Set the experiment name
    mlflow.set_experiment("Housing_Price_Prediction_Linear_Regression")
    mlflow.set_tracking_uri("http://localhost:5000")

    # Define model hyperparameters
    params = {
        "fit_intercept": True,
    }

    # After setting the  experiment, we can start tracking various aspects of our model
    # such as parameters, metrics, and model itself.
    with mlflow.start_run():

        # set expreiment tags
        mlflow.set_tags({"model": "Linear Regression", "dataset": "Housing Prices"})

        # Log model parameters
        for param, value in params.items():
            mlflow.log_param(param, value)

        print("Training model...")
        model = LinearRegression(fit_intercept=True)
        model.fit(x_train, y_train.values.ravel())  # Flatten y_train to 1D array
        y_pred =  model.predict(x_test)

        mse = mean_squared_error(y_test, y_pred)
       # Log evaluation metrics
        mlflow.log_metric("mean square error", mse)
        joblib.dump(model, 'model/linear_regression_model.joblib')
        #track model through mlflow
        mlflow.log_artifact('model/linear_regression_model.joblib')


def train_with_decision_tree():
    """
    Train a decision tree model and log the results using MLflow
    """
    mlflow.set_experiment("Housing_Price_Prediction_Decision_Tree")
    mlflow.set_tracking_uri("http://localhost:5000")
    # Define model hyperparameters
    params = {
        "random_state": 44,
        "max_depth": None,
        "min_samples_split": 2,
        "min_samples_leaf": 1
    }

    # After setting the  experiment, we can start tracking various aspects of our model
    # such as parameters, metrics, and model itself.
    with mlflow.start_run():

        # set expreiment tags
        mlflow.set_tags({"model": "Decision Tree", "dataset": "Housing Prices"})

        # Log model parameters
        for param, value in params.items():
            mlflow.log_param(param, value)

        print("Training model...")
        model = DecisionTreeRegressor(random_state=44, min_samples_split=2, min_samples_leaf=1)
        model.fit(x_train, y_train.values.ravel())  # Flatten y_train to 1D array
        y_pred =  model.predict(x_test)

        mse = mean_squared_error(y_test, y_pred)
        # Log evaluation metrics
        mlflow.log_metric("mean square error", mse)
        joblib.dump(model, 'model/decision_tree_model.joblib')
        #track model through mlflow
        mlflow.log_artifact('model/decision_tree_model.joblib')

if __name__ == "__main__":
    train_with_linear_regression()
    train_with_decision_tree()
    print("Training completed and models saved.")
