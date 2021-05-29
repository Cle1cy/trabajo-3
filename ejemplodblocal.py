
import flask
import sqlite3
import mysql.connector
#https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html

#coneccion a la base de datos
referenciabasedatos = (user = 'admin',
                                password = '12345678',
                                host = 'database-1.cczsxrehw43j.us-east-1.rds.amazonaws.com',
                                database = 'cont'
                                )


app = flask.Flask(__name__)

@app.route('/data', methods=['POST'])
def data():
   valores = flask.request.values
   nombre=flask.request.values.get("username")
   contraseña=flask.request.values.get("password")
   correo=flask.request.values.get("email")
 

   con = mysql.connect(referenciabasedatos)

   cur = con.cursor()
   cur.execute("INSERT INTO datos VALUES("+nombre+","+contraseña+","+correo");")

   con.commit()
   con.close()

   print(str(nombre)+str(contraseña)+str(correo))
   listajugadores.modificardata(nombre,contraseña,correo)
   return "ok"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80)
