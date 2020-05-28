import sys, os
sys.path.append(os.getcwd())
from flask import Flask, jsonify, request
from Clases.Comuna import Comuna
# from bdfalsa import productos
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def inicio():
    return 'hola' #jsonify(productos)

@app.route('/comuna/<string:nombre_comuna>', methods=['GET'])
def comuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        return jsonify({'message': 'Exitosamente', 'Comuna': com.dic()})
    else:
        return jsonify({"message":'Error'})

@app.route('/comuna/', methods=['GET'])
def comunas():
    com = Comuna()
    return jsonify(com.getComunas())

@app.route('/comuna/', methods=['POST'])
def addComuna():
    com = Comuna(nombre=request.json['nombre'], idProvincia=request.json['idProvincia'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)