## Pre-requist 
1. Visual Studio as Editor
2. python and pip is installed

## Project Structure
* `train.py`: Train and save both models
* `app.py`: FastAPI app to serve predictions and route traffic
* `dockerfile`:  Container build instructions
* `monitoring-deployment.yaml`: Monitoring stack and deployment --Prometheus and Grafana Deployment for monitoring
* `app-k8-deployment.yaml`: K8s based deployment of docker file which contains the app.py code
* `requirements.txt`: Dependencies
* `data.csv`: Dataset used to train the models
* `Housing.csv.dvc`: data verison file, which holds the information of from where the data need to be downloaded of the given version
## NOTE
Data is made part of the GIT HUB only .. this is done just to share the data with all team memebers.. other wise data should be part of some external storage like S3 or google driver


## How to use

1. **Clone the repo:**

   ```bash
   git clone https://github.com/2023ac05465/mlops-assignment.git
   cd mlops-assignment
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Get the Data Set**
   ```bash
   mv data.csv Housing.csv
   dvc add Housing.csv
   ```

4. **start the MFLOW**
   ```bash
   mlflow ui  # this command will start the mflow ui locally and can be accessed through URL http://127.0.0.1:5000/
   ```

   
5. **Train and save the models:**

   ```bash
   python train.py
   ```
   This will save models and preprocessors under the `models/` folder.

6. **Run the FastAPI app: Locally**
   ```bash
   python app.py
   ```
  
7. **Test the API:**
   Send a POST request to:

   ```
   http://127.0.0.0:8000/predict/linearregression
   ```

   ```
   http://127.0.0.0:8000/predict/decisiontreecd
   ```

   With sample JSON:

   ```json
   {"input":[-122.23,37.88,29.0,880.0,129.0,322.0,126.0,4.3252]}
   ```

  ```

 8. **Kuberneetes Deployment**

    Deploy Flask app, Prometheus, and Grafana:
    ```bash
    kubectl apply -f monitoring-deployment.yaml
    kubectl apply -f k8s-deployment.yaml
    ```

