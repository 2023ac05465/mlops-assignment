import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error  
import joblib
import mlflow

print("Loading dataset...")
data = pd.read_csv('Housing.csv')
data.head()
# pre processing of the data set
data = data.dropna()
data = data.drop(columns=['ocean_proximity'])
data.columns
x = data.drop(columns=['median_house_value'])
y = data['median_house_value']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)



# after the split, we need to perform the experiments

mlflow.set_experiment("Housing_Price_Prediction_Linear_Regression")
with mlflow.start_run():
    print("Training model...")
    model = LinearRegression()
    model.fit(x_train, y_train.values.ravel())  # Flatten y_train to 1D array
    #
    mlflow.log_params({"random_state": 42})
    y_pred =  model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    # track metrics through mlflow
    mlflow.log_metric("mse", mse)
    joblib.dump(model, 'linear_regression_model.joblib')
    #track model through mlflow
    mlflow.log_artifact('linear_regression_model.joblib')
