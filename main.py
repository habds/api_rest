from flask import Flask, jsonify
from conexion import coneccion,select
# from bdfalsa import productos
app = Flask(__name__)

@app.route('/')
def inicio():
    return 'hola' #jsonify(productos)

@app.route('/metodo_pago')
def metodoPago():
    respuesta=select()
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True, port=5000)