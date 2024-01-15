import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.generate import generatePlan, generatePlanWithOpenAI
from src.predict import predictMarathonTime
from src.helpers import get_pace_time

# pylint: disable=C0103
app = Flask(__name__, template_folder='dist')
# TODO remove cors when app will be deployed with front-end
CORS(app) 

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/api')
def hello():

    message = 'Welcome to the Marathon Prediction App!'

    return render_template('index.html', message=message)

@app.route('/predict', methods=['GET'])
def predict():
    age = request.args.get('age', default = '18', type = int)
    gender = request.args.get('gender', default = 'male', type = str)

    if age is None:
        return jsonify({"error": "age parameter is required"}), 400
    if gender is None:
        return jsonify({"error": "gender parameter is required"}), 400

    if age < 18:
        return jsonify({"error": 'You are too young to run'}), 400
    elif age > 80:
        return jsonify({"error": "you are too old to run"}), 400

    if gender not in ["male", "female"]:
        return jsonify({"error": "gender must be \"male\" or \"female\""}), 400

    # prediction
    time = predictMarathonTime(int(age), gender)
    
    if (time):
        pace = get_pace_time(time)
        return jsonify({"time": time, "pace": pace})
    
    return jsonify({"error": "an error happen, we can not predict your time :("}), 400

@app.route('/plan', methods=['GET'])
def getPlan():
    months = request.args.get('months', default = '6', type = int)
    age = request.args.get('age', default = '18', type = int)
    gender = request.args.get('gender', default = 'male', type = str)
    assistant = request.args.get('assistant', default = 'open-ai', type = str)

    if months is None:
        return jsonify({"error": "months parameter is required"}), 400

    if months < 3:
        return jsonify({"error": "months must be greater than 3"}), 400
    elif months > 12:
        return jsonify({"error": "months must be greater less then 12"}), 400
    
    if age is None:
        return jsonify({"error": "age parameter is required"}), 400
    if gender is None:
        return jsonify({"error": "gender parameter is required"}), 400

    if age < 18:
        return jsonify({"error": 'You are too young to run'}), 400
    elif age > 80:
        return jsonify({"error": "you are too old to run"}), 400

    if gender not in ["male", "female"]:
        return jsonify({"error": "gender must be \"male\" or \"female\""}), 400
    
    if assistant not in ["vertex-ai", "open-ai"]:
        return jsonify({"error": "assistant must be \"vertex-ai\" or \"open-ai\""}), 400
    
    gender_translation = {"male": "чоловік", "female": "жінка"}

    userContent = (f"Я {gender_translation[gender]} {age} років, мені потрібний тренувальний план на {months} місяці, розписаний по місяцям в Markdown")
    systemContent = 'Ти професійний тренер з бігу,'
    
    if (assistant == 'vertex-ai') :
        prompt = systemContent + userContent
        result = generatePlan(prompt)
    elif (assistant == 'open-ai') :
        result = generatePlanWithOpenAI(systemContent, userContent)

    if (result):
        return result

    return jsonify({"error": "an error happen, we can not get your plan :("}), 400

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
