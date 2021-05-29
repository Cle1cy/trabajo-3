import flask
import sys
import os

app = flask.Flask(__name__)

@app.route('/')
def home():
        return flask.render_template('index.html')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if flask.request.method == 'POST' and 'username' in flask.request.form and 'password' in flask.request.form:
		nombre = flask.request.form['username']
		contraseña = flask.request.form['password']
		puerto(range(5570,6000)) 
		for i in range(1):
			os.system("sudo docker run -d -p" + str(puerto[i]) + ":80 server:app" + nombre)
			i +=1
	return flask.render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if flask.request.method == 'POST' and 'username' in flask.request.form and 'password' in flask.request.form and 'email' in flask.request.form :
		nombre = flask.request.form['username']
		contraseña = flask.request.form['password']
		correo = flask.request.form['email']
	elif flask.request.method == 'POST':
		msg = 'Please fill out the form !'
	return flask.render_template('register.html', msg = msg)
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80)
