## Pre-requist 
1. Visual Studio as Editor
2. python and pip is installed

## Project Structure
* `train.py`: Train and save both models
* `app.py`: FastAPI app to serve predictions and route traffic
* `dockerfile`:  Container build instructions
* `monitoring-deployment.yaml`: Monitoring stack and deployment --Prometheus and Grafana Deployment for monitoring
* `requirements.txt`: Dependencies
* `Data.csv`: Dataset used to train the models

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
   
4. **Train and save the models:**

   ```bash
   python train.py
   ```
   This will save models and preprocessors under the `models/` folder.

4. **Run the FastAPI app: Locally**
   
   Deploy Flask app, Prometheus, and Grafana:
   ```bash
   kubectl apply -f monitoring-deployment.yaml
   kubectl apply -f k8s-deployment.yaml
   ```
6. **Kuberneetes Deployment**

   ```bash
   python app.py
   ```

7. **Test the API:**
   Send a POST request to:

   ```
   http://127.0.0.0:5000/predict
   ```

   With sample JSON:

   ```json
   {"input":[5.1,1.2,3.2,3.4]}
   ```

6. **Simulate 100+ requests:**

   ```bash
   python simulator.py
   ```

7. **Evaluate model performance:**

   ```bash
   python performance.py
   ```
   
8. mflow ui  --- this command will start the mflow ui locally and can be accessed through URL http://127.0.0.1:5000/

---
DOCKER SETUP -- Pre-requist Docker should be installed on your machine

1. Once your local APIS are working we can containarized the APIS.
2. execute the command to build the image ----  docker build -t iris
3. run the docker ---    docker run -p 5000:5000 iris
4. this will enable the rest API which can be executed from the postman
   4.1 URL -- http://127.0.0.0:5000/predict
   4.2  body data --  {"input":[5.1,1.2,3.2,3.4]}
