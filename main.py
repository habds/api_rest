import sys, os
sys.path.append(os.getcwd())
from flask import Flask, jsonify
from conexion import coneccion,select
from Clases.Ciudad import Ciudad
# from bdfalsa import productos
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def inicio():
    return 'hola' #jsonify(productos)

@app.route('/ciudad/<string:nombre_ciudad>', methods=['GET'])
def ciudad(nombre_ciudad):
    ciu = Ciudad(nombre=nombre_ciudad)
    if ciu.getCiudad():
        return jsonify({'message': 'Exitosamente', 'Ciudad': ciu.dic()})
    else:
        return jsonify({"message":'Error'})

@app.route('/ciudad/', methods=['GET'])
def ciudades():
    ciu = Ciudad()
    return jsonify(ciu.getCiudades())

if __name__ == '__main__':
    app.run(debug=True, port=5000)