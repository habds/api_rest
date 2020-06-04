import sys, os
sys.path.append(os.getcwd())
from flask import Flask, jsonify, request
from Clases.Comuna import Comuna
from Clases.Region import Region
from Clases.Producto import Producto
from Clases.Categoria import Categoria
from Clases.Provincia import Provincia
# from bdfalsa import productos
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

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
    nombre_p = request.args.get('provincia')
    if nombre_p:
        diccionarioope = com.filtrarProvincia(nombre_p)
        return jsonify(diccionarioope)
    else:
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

#------------------------------------Producto-------------------------------------------------------------

@app.route('/producto/<int:id_producto>', methods=['GET'])
def producto(id_producto):
    prod = Producto(id=id_producto)
    if prod.getProducto():
        return jsonify({'message': 'Exitosamente', 'Producto': prod.dic()})
    else:
        return jsonify({"message":f'No existe ningun producto con el nombre {prod.nombre}'})

@app.route('/producto/', methods=['GET'])
def productos():
    prod = Producto()
    return jsonify(prod.getProductos())

@app.route('/producto/', methods=['POST'])
def addProducto():
    prod = Producto(nombre=request.json['nombre'], descripcion=request.json['descripcion'], precio=request.json['precio'], idcategoria=request.json['idcategoria'])
    if prod.setProducto():
        return jsonify({'message':'Producto creado exitosamente', 'Producto': prod.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Producto'})

@app.route('/producto/<int:id_producto>', methods=['PUT'])
def updateProducto(id_producto):
    prod = Producto(id=id_producto)
    if prod.getProducto():
        prod.setNombre(request.json['nombre'])
        prod.setDescripcion(request.json['descripcion'])
        prod.setPrecio(request.json['precio'])
        prod.idcategoria = request.json['idcategoria']
        if prod.updateProducto():
            return jsonify({'message':'Producto Actualizado Exitosamente', 'Producto':prod.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el Producto'})


@app.route('/producto/<int:id_producto>', methods=['DELETE'])
def deleteProducto(id_producto):
    prod = Producto(id=id_producto)
    if prod.getProducto():
        if prod.deleteProducto():
            return jsonify({
                'message': 'El producto fue eliminado exitosamente',
                'Producto': prod.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el producto'})
    else:
        return jsonify({'message':'No se encontro ningun producto para eliminar'})

#------------------------------------Fin Producto-------------------------------------------------------------

#------------------------------------Categoria-------------------------------------------------------------

@app.route('/categoria/<string:nombre_categoria>', methods=['GET'])
def categoria(nombre_categoria):
    cat = Categoria(nombre=nombre_categoria)
    if cat.getCategoria():
        return jsonify({'message': 'Exitosamente', 'Region': cat.dic()})
    else:
        return jsonify({"message":f'No existe ninguna region con el nombre {nombre_categoria}'})

@app.route('/categoria/', methods=['GET'])
def categorias():
    cat = Categoria()
    return jsonify(cat.getCategorias())

@app.route('/categoria/', methods=['POST'])
def addCategoria():
    cat = Categoria(nombre=request.json['nombre'])
    if cat.setCategoria():
        return jsonify({'message':'Categoria creada exitosamente', 'Categoria': cat.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear la Categoria'})

@app.route('/categoria/<string:nombre_categoria>', methods=['PUT'])
def updateCategoria(nombre_categoria):
    cat = Categoria(nombre=nombre_categoria)
    if cat.getCategoria():
        cat.setNombre(request.json['nombre'])
        if cat.updateCategoria():
            return jsonify({'message':'Categoria Actualizada Exitosamente', 'Categoria':cat.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Region'})


@app.route('/categoria/<string:nombre_categoria>', methods=['DELETE'])
def deleteCategoria(nombre_categoria):
    cat = Categoria(nombre=nombre_categoria)
    if cat.getCategoria():
        if cat.deleteCategoria():
            return jsonify({
                'message': 'La categoria fue eliminada exitosamente',
                'Categoria': cat.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar la categoria'})
    else:
        return jsonify({'message':'No se encontro ninguna categoria para eliminar'})

#------------------------------------------------------------------
#----------------------provincia----------------------------------------
@app.route('/provincia/<string:nombre_provincia>', methods=['GET'])
def provincia(nombre_provincia):
    pro = Provincia(nombre=nombre_provincia)
    if pro.getProvincia():
        return jsonify({'message': 'Exitosamente', 'Provincia': pro.dic()})
    else:
        return jsonify({"message":f'No existe ninguna provincia con el nombre {nombre_provincia}'})

@app.route('/provincia/', methods=['GET'])
def provincias():
    pro = Provincia()
    return jsonify(pro.getProvincias())

@app.route('/provincia/', methods=['POST'])
def addProvincia():
    pro = Provincia(nombre=request.json['nombre'], idRegion=request.json['idRegion'])
    if pro.setProvincia():
        return jsonify({'message':'Provincia creada exitosamente', 'Provincia': pro.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear la Provincia'})

@app.route('/provincia/<string:nombre_provincia>', methods=['PUT'])
def updateProvincia(nombre_provincia):
    pro = Provincia(nombre=nombre_provincia)
    if pro.getProvincia():
        pro.setNombre(request.json['nombre'])
        pro.setIdregion(request.json['idRegion'])
        if pro.updateProvincia():
            return jsonify({'message':'Provincia Actualizada Exitosamente', 'Provincia':pro.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Provincia'})

@app.route('/provincia/<string:nombre_provincia>', methods=['DELETE'])
def deleteProvincia(nombre_provincia):
    pro = Provincia(nombre=nombre_provincia)
    if pro.getProvincia():
        if pro.deleteProvincia():
            return jsonify({
                'message': 'La region fue eliminada exitosamente',
                'Region': pro.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar la region'})
    else:
        return jsonify({'message':'No se encontro ninguna region para eliminar'})

if __name__ == '__main__':
 app.run(debug=True)