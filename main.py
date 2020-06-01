import sys, os
sys.path.append(os.getcwd())
from flask import Flask, jsonify, request
from Clases.Comuna import Comuna
from Clases.Region import Region
# from bdfalsa import productos
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def inicio():
    return 'hola' #jsonify(productos)

#------------------------------------Comunas-------------------------------------------------------------
@app.route('/comuna/<string:nombre_comuna>', methods=['GET'])
def comuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        return jsonify({'message': 'Exitosamente', 'Comuna': com.dic()})
    else:
        return jsonify({"message":f'No existe ninguna comuna con el nombre {nombre_comuna}'})

@app.route('/comuna/', methods=['GET'])
def comunas():
    com = Comuna()
    print(request.args.get('pentakill'))
    return jsonify(com.getComunas())

@app.route('/comuna/', methods=['POST'])
def addComuna():
    com = Comuna(nombre=request.json['nombre'], idProvincia=request.json['idProvincia'])
    if com.setComuna():
        return jsonify({'message':'Comuna creada exitosamente', 'Comuna': com.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear la Comuna'})

@app.route('/comuna/<string:nombre_comuna>', methods=['PUT'])
def updateComuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        com.setNombre(request.json['nombre'])
        com.setIdProvincia(request.json['idProvincia'])
        if com.updateComuna():
            return jsonify({'message':'Comuna Actualizada Exitosamente', 'Comuna':com.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Comuna'})


@app.route('/comuna/<string:nombre_comuna>', methods=['DELETE'])
def deleteComuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        if com.deleteComuna():
            return jsonify({
                'message': 'La comuna fue eliminada exitosamente',
                'Comuna': com.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar la comuna'})
    else:
        return jsonify({'message':'No se encontro ninguna comuna para eliminar'})




#------------------------------------Fin Comunas-------------------------------------------------------------

#------------------------------------Region-------------------------------------------------------------

@app.route('/region/<string:nombre_region>', methods=['GET'])
def region(nombre_region):
    reg = Region(nombre=nombre_region)
    if reg.getRegion():
        return jsonify({'message': 'Exitosamente', 'Region': reg.dic()})
    else:
        return jsonify({"message":f'No existe ninguna region con el nombre {nombre_region}'})

@app.route('/region/', methods=['GET'])
def regiones():
    reg = Region()
    return jsonify(reg.getRegiones())

@app.route('/region/', methods=['POST'])
def addRegion():
    reg = Region(nombre=request.json['nombre'], codigo=request.json['codigo'])
    if reg.setRegion():
        return jsonify({'message':'Region creada exitosamente', 'Region': reg.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear la Region'})

@app.route('/region/<string:nombre_region>', methods=['PUT'])
def updateRegion(nombre_region):
    reg = Region(nombre=nombre_region)
    if reg.getRegion():
        reg.setNombre(request.json['nombre'])
        reg.setCodigo(request.json['codigo'])
        if reg.updateRegion():
            return jsonify({'message':'Region Actualizada Exitosamente', 'Region':reg.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Region'})


@app.route('/region/<string:nombre_region>', methods=['DELETE'])
def deleteRegion(nombre_region):
    reg = Region(nombre=nombre_region)
    if reg.getRegion():
        if reg.deleteRegion():
            return jsonify({
                'message': 'La region fue eliminada exitosamente',
                'Region': reg.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar la region'})
    else:
        return jsonify({'message':'No se encontro ninguna region para eliminar'})

if __name__ == '__main__':
 app.run(debug=True)