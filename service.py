import flask
from flask_cors import cross_origin
from email.message import EmailMessage

#--------------------Flask App---------------------
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/whatever', methods=['GET'])
@cross_origin()
def home():
    return '<h1>Hello</h1>'

app.run()
