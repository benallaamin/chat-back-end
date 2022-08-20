from threading import local
from urllib import response
from flask import Flask, render_template, jsonify, request
import numpy
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.get("/")
def index_get():
    return render_template("base.html")



@app.post('/predict')
def predict():
    print(request.get_json())
    text=request.get_json()["message"]
    print(text)
    response=get_response(text)
    print(get_response(text))
    message={"answer":response}
    print(message)
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)