import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html',prediction_text="")


@app.route('/predict',methods=['POST'])
def predict():

    if request.form["experience"].isnumeric():
        prediction = model.predict([[request.form["experience"]]])
        output = 'Your predicted salary: ${:,.2f}'.format(float(prediction))
    else:
        output = "Please Enter a Numeric value"

    return render_template('index.html', prediction_text=output)



@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    print(data["experience"])
    prediction = model.predict([[data["experience"]]])
    
    return jsonify(prediction[0][0])


if __name__ == "__main__":
    app.run(debug=True)