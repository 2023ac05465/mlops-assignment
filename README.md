Pre-requist 
1. Visual Studio Code
2. python and pip is installed
---

1. Data is made part of the GIT HUB only .. this is done just to share the data with all team memebers.. other wise data should be part of some external storage like S3 or google driver
2. Onces we checkout the repo we will have the data also present
3. rename the data.cvs file to Housing.csv
4. pip install -r requirements
5. dvc add Housing.csv
6. mflow ui  --- this command will start the mflow ui locally and can be accessed through URL http://127.0.0.1:5000/
7. python train.py --- this will create the model
8. python app.py  -- this will enable the rest API which can be executed from the postman
   8.1- URL -- http://127.0.0.0:5000/predict
   8.2  body data --  {"input":[5.1,1.2,3.2,3.4]} 
