import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask,request,jsonify,render_template

# start flask
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

# render default webpage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    rd=request.form['rd']
    ad=request.form['administration']
    mar=request.form['marketing']
    st=request.form['state']
    a=[]
    if(st=='Florida' or st=='florida' or st=='FLORIDA'):
        a=[1,0]
    if(st=='California' or st=='california' or st=='CALIFORNIA'):
        a=[0,0]
    if(st=='New York' or st=='new york' or st=='New york' or st=='newyork' or st=='NEW YORK' or st=='NEWYORK'):
        a=[0,1]
    prediction=model.predict([[float(rd),float(ad),float(mar),a[0],a[1]]])
    
    output=round(prediction[0],2)
    
    return render_template('index.html',prediction_text='Profit is Rs. {}'.format(output))
    
if __name__ == '__main__':
    app.run(debug=True)
