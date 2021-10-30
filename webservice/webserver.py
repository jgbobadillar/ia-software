from flask import Flask
from flask import request
import requests
import os

app=Flask(__name__)

ip_ai_server = os.getenv("IA_IP") or "127.0.0.1"

@app.route("/credit/predict", methods=['POST'])
def predict():
    content = request.get_json()
    age = content['age']
    housing = content['housing']
    credit_amount = content['credit_amount'] 

    response = requests.post(f"http://{ip_ai_server}:5000/servicioia", 
                        json={"age": age, "housing": housing,"credit_amount": credit_amount})
    print("ia responde", response.json())
    return {"prediction": response.json()}


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)

