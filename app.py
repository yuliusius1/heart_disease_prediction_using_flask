from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/diagnosa', methods=['GET', 'POST'])
def diagnosa():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
    
        data = [int(age), int(sex),int(cp),int(trestbps),int(chol),int(restecg),int(fbs),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]
        # convert data to numpy array
        data_as_array = np.asarray(data)
        data_reshape = data_as_array.reshape(1,-1)
        prediction = model.predict(data_reshape)

        if prediction[0] == 0:
            result = 'Negatif'
        else:
            result = 'Positif'
        return render_template('result.html', result = result, name = name)
    return render_template('index.html')
        
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)