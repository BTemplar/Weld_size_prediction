from flask import Flask, request, render_template
import pickle
import pandas as pd

def weld_size_prediction(iw, if_, vw, fp):
    with open('ML/weld_size_prediction.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('ML/weld_size_scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)

    numerical_features = ['IW', 'IF', 'VW', 'FP']
    df = pd.DataFrame({
        'IW': [iw],
        'IF': [if_],
        'VW': [vw],
        'FP': [fp]})

    df[numerical_features] = scaler.transform(df[numerical_features])
    predictions = model.predict(df)

    depth = round(predictions[:, 0][0], 2)
    width = round(predictions[:, 1][0], 2)

    return depth, width
app = Flask(__name__)

html_form = '/templates/index.html'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        iw = int(request.form['IW'])
        if_ = int(request.form['IF'])
        vw = float(request.form['VW'])
        fp = int(request.form['FP'])
        result = weld_size_prediction(iw, if_, vw, fp)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
