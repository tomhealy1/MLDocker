#Flask

import pickle
from flask import Flask, request
import numpy as np 
from pathlib import Path

#base_path = Path(__file__).parent
#file_path = (base_path / "..").resolve()


with open('/Users/Teamwork/Desktop/rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict')
def predict_iris():
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str(prediction)

if __name__ == '__main__':
    app.run()
