import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.generate import generatePlan
from src.predict import predictMarathonTime

# pylint: disable=C0103
app = Flask(__name__)
# TODO remove cors when app will be deployed with front-end
CORS(app) 

@app.route('/')
def hello():

    message = 'Welcome to the Marathon Prediction App!'

    return render_template('index.html', message=message)

@app.route('/predict', methods=['GET'])
def predict():
    age = request.args.get('age', default = '18', type = int)
    gender = request.args.get('gender', default = 'male', type = str)

    # prediction = model.predict(age, gender)
    time = predictMarathonTime(int(age), gender)
    result = {
        "time": time
    }
    
    return jsonify(result)

@app.route('/plan')
def getPlan():
    mounts = request.args.get('mounts', default = '6', type = int)
    prompt = (f"Ти тренер з бігу, мені потрібний тренувальний план на {mounts} місяці, розписаний по місяцям")
    result = generatePlan(prompt)

    return result

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
