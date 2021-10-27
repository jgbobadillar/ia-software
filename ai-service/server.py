from flask import Flask
from flask import request
import joblib

app = Flask(__name__)

preprocess = joblib.load('models/preprocesamiento.joblib')
model = joblib.load('models/model.joblib')

@app.route('/servicioia', methods=['POST'])
def servicio_ia():
    global preprocess
    global model
    content = request.get_json()
    age = content['age']
    housing = content['housing']
    credit_amount = content['credit_amount']

    y = model.predict_proba(preprocess.transform([[age, housing, credit_amount]]))
    print(y)
    return {"prediction": {"bad_score_proba": y[0, 0], "good_score_proba": y[0, 1]}}




if __name__=='__main__':
    app.run('0.0.0.0')

