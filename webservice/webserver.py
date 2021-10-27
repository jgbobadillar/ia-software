from flask import Flask
import requests


app=Flask(__name__)

@app.route("/credit/predict")
def predict():
    response = requests.post("http://127.0.0.1:5000/servicioia", 
                        json={"age": 23, "housing": "rent","credit_amount": 1000})
    print("ia responde", response.json())
    return {"prediction": response.json()}


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)

