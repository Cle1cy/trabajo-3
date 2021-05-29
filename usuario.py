import flask
import sys

app = flask.Flask(__name__)

@app.route('/')

def home():
    return “hola usuario ”+ sys.argv[1]

if __name__ == '__main__':

        app.run(debug=True,host='0.0.0.0',port=80)

