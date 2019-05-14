#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Tom Healy

#Import libraries and modules
import pickle
from flask import Flask, request
from flasgger import Swagger
import numpy as np
import pandas as pd
#load the model that is saved as a pickle file and add read privilege
with open('./rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
#initiate the Flask app and we are adding swagger ui wrapper
app = Flask(__name__)
swagger = Swagger(app)
#Using the flask mod we add two endpoint (API) one for a GET request and the other for a POST request
@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    responses:
        200:
          description: OK
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    responses:
          200:
            description: OK
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    