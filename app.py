import os
import numpy as np
from flask import Flask, request, render_template, url_for
import requests
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


app=Flask(__name__)#our flask app
model=load_model('ECG.h5')

@app.route("/") #default routC:\Users\hariharan\Documents\Projects\Untitled Foldere
def about():
    return render_template( "about.html")
@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/info") #default route
def information():
    return render_template("info.html")

@app.route("/upload")
def test():
    return render_template("index6.html")

@app.route("/predict",methods=["GET","POST"])
def upload():
    if request.method=='POST':
        
        f=request.files['file']
        basepath=os.path.dirname('__file__')
        filepath=os.path.join(basepath,"uploads",f.filename)
        f.save(filepath)

        img=image.load_img(filepath,target_size=(64,64))
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)

        pred=(model.predict(x) > 0.5).astype("int32")
        print("Prediction",pred)

        API_KEY = "[enter the api key]"
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
        API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        payload_scoring = {"input_data": [{"field":x}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b80cbc74-c8c2-48eb-bd8f-9b6e63cdc26e/predictions?version=2022-11-19', json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        predictions=response_scoring.json()
        print(predictions)
        index=['Left Bundle Branch Block','Normal','Premature Atrial Contraction','Premature Ventricular Contraction','Right Bundle Branch Block','Ventricular Fibrillation']
        result=str(index[pred[0].tolist().index(1.)])
        return render_template("base.html", name = result)  
        
    return None
    

if __name__=="__main__":
    app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)
