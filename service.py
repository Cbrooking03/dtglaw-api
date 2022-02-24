from http import client
import flask
from flask_cors import cross_origin
import models
from models.client import client

#--------------------Flask App---------------------
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/whatever', methods=['GET'])
@cross_origin()
def home():
    c = client(4)
    print(c.num)
    return '<h1>Hello</h1>'

app.run()
