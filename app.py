import pickle
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application

# import ridge and standard scaler pickle
Ridge=pickle.load(open('models/Ridge.pkl','rb'))
scaler=pickle.load(open('models/scaler1.pkl','rb'))

#Route for home page
# @cross_origin()
@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')

# @cross_origin()
@app.route("/predictdata",methods=["GET","POST"])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        new_data_scaled=scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=Ridge.predict(new_data_scaled)

        return render_template('home.html',result=result[0])

    else:
        return render_template('home.html')



    
if __name__=="__main__":
    app.run(host="0.0.0.0" )