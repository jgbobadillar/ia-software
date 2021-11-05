from flask import Flask
from flask import request
import requests
import os
from flask import render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

ip_ai_server = os.getenv("IA_IP") or "127.0.0.1"

@app.route("/credit/predict", methods=['POST'])
def predict():
    name = request.form.get('nombre')
    age = int(request.form.get('age'))
    housing = request.form.get('housing')
    credit_amount = int(request.form.get('credit_amount'))

    response = requests.post(f"http://{ip_ai_server}:5000/servicioia", 
                        json={"age": age, "housing": housing,"credit_amount": credit_amount})
    

    response = response.json()
    print(response)
    good_score_proba = response['prediction']['good_score_proba']
    bad_score_proba = response['prediction']['bad_score_proba']
    if good_score_proba >=0.5:
       good_client = True
       proba = good_score_proba
    else:
       good_client = False
       proba = bad_score_proba

    return render_template("response.html", nombre= name, credit_amount= credit_amount, proba= proba, good_client= good_client)

@app.route("/credit/predict/v2",methods=["POST"])
def predict2():
    content = request.get_json()
    name = content['nombre']
    age = int(content['age'])
    housing = content['housing']
    credit_amount = int(content['credit_amount'])

    response = requests.post(f"http://{ip_ai_server}:5000/servicioia", 
                        json={"age": age, "housing": housing,"credit_amount": credit_amount})
    

    response = response.json()
    print(response)
    good_score_proba = response['prediction']['good_score_proba']
    bad_score_proba = response['prediction']['bad_score_proba']
    if good_score_proba >=0.5:
       good_client = True
       proba = good_score_proba
    else:
       good_client = False
       proba = bad_score_proba

    return {"nombre": name, "credit_amount":credit_amount, "proba":proba, "good_client":good_client}



@app.route('/')
def form():
    return render_template("form.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)

