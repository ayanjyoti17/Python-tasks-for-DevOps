from flask import Flask

#creating a flask app instance
app = Flask(__name__)

#decorator
@app.route("/")
def hello_world():
    return 'hello, world!'

app.run('0.0.0.0')