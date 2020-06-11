import sys, os
sys.path.append(os.getcwd())
from flask import Flask, jsonify, request
from Clases.Comuna import Comuna
from Clases.Region import Region
from Clases.Producto import Producto
from Clases.Categoria import Categoria
from Clases.Provincia import Provincia
from Clases.TiendaTipo import TiendaTipo
from Clases.Tienda import Tienda
from Clases.Rol import Rol
from Clases.Sexo import Sexo
from Clases.Persona import Persona
from Clases.Login_detail import Login_detail
from Clases.Login import Login

import jwt
import datetime
from functools import wraps



usuario="matias"
contraseña ="password"
# from bdfalsa import productos
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'palabrasecretabb:v'


#------------------------------------------LOGIN-----------------------------------------------
@app.route('/login/<int:pId>', methods=['GET'])
def login(pId):
    log = Login(id=pId)
    if log.searchLoginById():
        return jsonify({'message': 'Exitosamente', 'Login': log.dic()})
    else:
        return jsonify({"message":f'No existe ningun sexo con el nombre {pId}'})

@app.route('/login/', methods=['GET'])
def logins():
    log = Login()
    return jsonify(log.selectLogin())

@app.route('/login/', methods=['POST'])
def addLogin():
    log = Login(username=request.json['username'],password=request.json['password']
                ,idPersona=request.json['idPersona'],idRol=request.json['idRol'])
    if log.insertLogin():
        return jsonify({'message':'Datos paraa logearse creado exitosamente', 'Login': log.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear los datos para logearse'})

@app.route('/login/<int:pId>', methods=['PUT'])
def updateLogin(pId):
    log = Login(id=pId)
    if log.searchLogin():
        log.setUsername(request.json['username'])
        log.setPassword(request.json['password'])
        log.setIdpersona(request.json['idPersona'])
        log.setIdrol(request.json['idRol'])
        if log.updateLogin():
            return jsonify({'message':'Datos de login actualizados exitosamente', 'login':log.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar los datos de login'})


@app.route('/login/<int:pId>', methods=['DELETE'])
def deleteLogin(pId):
    log = Login(id=pId)
    if log.searchLogin():
        if log.deleteLogin():
            return jsonify({
                'message': 'Los datos para logearse fueron eliminados exitosamente',
                'Login': log.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar los datos para logearse'})
    else:
        return jsonify({'message':'No se encontro ningun dato para eliminar con el id:'+id})


@app.route('/token' , methods=['POST'])
def obtenerToken():
    log = Login()
    #auth = request.authorization
    log.username = request.json['username']
    log.password = request.json['password']

    credenciales = log.searchLogin()
    if credenciales:
        token = jwt.encode({'user' : log.username, 'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})
    else:
        return jsonify({'messege' : 'Error con la validación'})

def token_required(ƒ):
    @wraps(ƒ)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'messege' : 'Falta el token'})
        else:
            try:
                tokenD = jwt.decode(token, app.config['SECRET_KEY'])
                return ƒ(*args, **kwargs)
            except:
                return jsonify({'messege' : 'EL token es invalido'})
    return decorated

#--------------------------------------- FIN login-------------------------------------------------




#------------------------------------Comunas-------------------------------------------------------------
@app.route('/comuna/<string:nombre_comuna>', methods=['GET'])

def comuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        return jsonify({'message': 'Exitosamente', 'Comuna': com.dic()})
    else:
        return jsonify({"message":f'No existe ninguna comuna con el nombre {nombre_comuna}'})


@app.route('/comuna/', methods=['GET'])
@token_required
def comunas():
    com = Comuna()
    nombre_p = request.args.get('provincia')
    if nombre_p:
        diccionarioope = com.filtrarProvincia(nombre_p)
        return jsonify(diccionarioope)
    else:
        return jsonify(com.getComunas())

@app.route('/comuna/', methods=['POST'])
#@token_required
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

@app.route('/producto/<string:nombre_producto>', methods=['PUT'])
def updateProducto(nombre_producto):
    prod = Producto(nombre=nombre_producto)
    if prod.getProducto():
        prod.setNombre(request.json['nombre'])
        prod.setDescripcion(request.json['descripcion'])
        prod.setPrecio(request.json['precio'])
        prod.idcategoria = request.json['idcategoria']
        if prod.updateProducto():
            return jsonify({'message':'Producto Actualizado Exitosamente', 'Producto':prod.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el Producto'})


@app.route('/producto/<string:nombre_producto>', methods=['DELETE'])
def deleteProducto(nombre_producto):
    prod = Producto(nombre=nombre_producto)
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
    regionid = request.args.get('region')
    if regionid:
        return jsonify(pro.filtroRegion(regionid))
    else:
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
#-----------------fin provincia----------------------------------

#-----------------Tienda Tipo---------------------------------------
@app.route('/tiendatipo/<string:pCodigo>', methods=['GET'])
def tiendaTipo(pCodigo):
    tie = TiendaTipo(codigo=pCodigo)
    if tie.getTiendaTipo():
        return jsonify({'message': 'Exitosamente', 'Tienda Tipo': tie.dic()})
    else:
        return jsonify({"message":f'No existe ninguna provincia con el nombre {pCodigo}'})

@app.route('/tiendatipo/', methods=['GET'])
def tiendaTipos():
    tie = TiendaTipo()
    return jsonify(tie.selectTiendaTipos())

@app.route('/tiendatipo/', methods=['POST'])
def addTiendaTipo():
    tie = TiendaTipo(codigo=request.json['codigo'], descripcion=request.json['descripcion'])
    if tie.createTiendaTipo():
        return jsonify({'message':'Tipo de tienda creada exitosamente', 'TiendaTipo': tie.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Tipo de tienda'})

@app.route('/tiendatipo/<string:pCodigo>', methods=['PUT'])
def updateTiendaTipo(pCodigo):
    tie = TiendaTipo(codigo=pCodigo)
    if tie.getTiendaTipo():
        tie.setCodigo(request.json['codigo'])
        tie.setDescripcion(request.json['descripcion'])
        if tie.updateTiendaTipo():
            return jsonify({'message':'Tienda tipo Actualizada Exitosamente', 'Tienda Tipo':tie.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Tienda tipo'})

@app.route('/tiendatipo/<string:pCodigo>', methods=['DELETE'])
def deleteTiendaTipo(pCodigo):
    tie = TiendaTipo(codigo=pCodigo)
    if tie.getTiendaTipo():
        if tie.deleteTiendaTipo():
            return jsonify({
                'message': 'El Tipo de tienda fue eliminada exitosamente','Tienda Tipo': tie.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el tipo de tienda '})
    else:
        return jsonify({'message':'No se encontro ninguna Tipo de tienda para eliminar'})


#---------------------fin Tienda Tipo-----------------

#-----------------------Tienda-------------------------------------------------------------
@app.route('/tienda/<string:pNombre>', methods=['GET'])
def tienda(pNombre):
    tie = Tienda(nombre=pNombre)
    if tie.selectTienda():
        return jsonify({'message': 'Exitosamente', 'Tienda': tie.dic()})
    else:
        return jsonify({"message":f'No existe ninguna provincia con el nombre {pNombre}'})

@app.route('/tienda/', methods=['GET'])
def tiendas():
    tie = Tienda()
    return jsonify(tie.selectTiendas())

@app.route('/tienda/', methods=['POST'])
def addTienda():
    tie = Tienda(nombre=request.json['nombre'], direccion=request.json['direccion'], email=request.json['email'], telefono=request.json['telefono'],idComuna=request.json['idComuna'], idTipoTienda=request.json['idTipoTienda'])
    if tie.createTienda():
        return jsonify({'message':'Tipo de tienda creada exitosamente', 'Tienda': tie.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Tipo de tienda'})

@app.route('/tienda/<string:pNombre>', methods=['PUT'])
def updateTienda(pNombre):
    tie = Tienda(nombre=pNombre)
    if tie.selectTienda():
        tie.setNombre(request.json['nombre'])
        tie.setDireccion(request.json['direccion'])
        tie.setEmail(request.json['email'])
        tie.setTelefono(request.json['telefono'])
        tie.setIdComuna(request.json['idComuna'])
        tie.setIdtipotienda(request.json['idTipoTienda'])
        if tie.updateTiendaTipo():
            return jsonify({'message':'Tienda actualizada Exitosamente', 'Tienda':tie.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Tienda'})

@app.route('/tienda/<string:pNombre>', methods=['DELETE'])
def deleteTienda(pNombre):
    tie = Tienda(nombre=pNombre)
    if tie.selectTienda():
        if tie.deleteTienda():
            return jsonify({
                'message': 'El Tipo de tienda fue eliminada exitosamente','Tienda': tie.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar la tienda '})
    else:
        return jsonify({'message':'No se encontro ninguna tienda para eliminar'})

#-------------------------fin tienda---------------------------------------------------------

#-------------------------------------rol-------------------------------------------------------
@app.route('/rol/<string:pNombre>', methods=['GET'])
def rol(pNombre):
    rol = Rol(nombre=pNombre)
    if rol.searchRol():
        return jsonify({'message': 'Exitosamente', 'Tienda': rol.dic()})
    else:
        return jsonify({"message":f'No existe ningun Rol con el nombre {pNombre}'})

@app.route('/rol/', methods=['GET'])
def roles():
    rol = Rol()
    return jsonify(rol.selectRoles())

@app.route('/rol/', methods=['POST'])
def addRol():
    rol = Rol(nombre=request.json['nombre'], codigo=request.json['codigo'])
    if rol.insertRol():
        return jsonify({'message':'Rol creado exitosamente', 'Rol': rol.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Rol'})

@app.route('/rol/<string:pNombre>', methods=['PUT'])
def updateRol(pNombre):
    rol = Rol(nombre=pNombre)
    if rol.searchRol():
        rol.setNombre(request.json['nombre'])
        rol.setCodigo(request.json['codigo'])
        
        if rol.updateRol():
            return jsonify({'message':'Rol actualizado Exitosamente', 'Rol':rol.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar Rol'})
    else:
        return jsonify({'message':'No encontro nada...'})

@app.route('/rol/<string:pNombre>', methods=['DELETE'])
def deleteRol(pNombre):
    rol = Rol(nombre=pNombre)
    if rol.searchRol():
        if rol.deleteRol():
            return jsonify({
                'message': 'El Rol fue eliminado exitosamente','rol': rol.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el Rol'})
    else:
        return jsonify({'message':'No se encontro el rol'})
#---------------------------------------fin rol -------------------------------------------------
#------------------------------------Sexo-------------------------------------------------------------

@app.route('/sexo/<string:nombre_sexo>', methods=['GET'])
def sexo(nombre_sexo):
    sex = Sexo(nombre=nombre_sexo)
    if sex.getSexo():
        return jsonify({'message': 'Exitosamente', 'Sexo': sex.dic()})
    else:
        return jsonify({"message":f'No existe ningun sexo con el nombre {nombre_sexo}'})

@app.route('/sexo/', methods=['GET'])
def sexos():
    sex = Sexo()
    return jsonify(sex.getSexos())

@app.route('/sexo/', methods=['POST'])
def addSexo():
    sex = Sexo(nombre=request.json['nombre'])
    if sex.setSexo():
        return jsonify({'message':'Sexo creado exitosamente', 'Sexo': sex.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Sexo'})

@app.route('/sexo/<string:nombre_sexo>', methods=['PUT'])
def updateSexo(nombre_sexo):
    sex = Sexo(nombre=nombre_sexo)
    if sex.getSexo():
        sex.setNombre(request.json['nombre'])
        if sex.updateSexo():
            return jsonify({'message':'Sexo Actualizado Exitosamente', 'Sexo':sex.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el Sexo'})


@app.route('/sexo/<string:nombre_sexo>', methods=['DELETE'])
def deleteSexo(nombre_sexo):
    sex = Sexo(nombre=nombre_sexo)
    if sex.getSexo():
        if sex.deleteSexo():
            return jsonify({
                'message': 'El sexo fue eliminado exitosamente',
                'Sexo': sex.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el Sexo'})
    else:
        return jsonify({'message':'No se encontro ningun Sexo para eliminar'})

#--------------------------------------- FIN SEXO-------------------------------------------------

#------------------------------------------------LOGIN_DETAIL-------------------------------------
@app.route('/login_detalle/<int:pId_logged>', methods=['GET'])
def login_detail(pId_logged):
    log_d = Login_detail(id_logged=pId_logged)
    if log_d.searchLogin_detail():
        return jsonify({'message': 'Exitosamente', 'Detalle de login': log_d.dic()})
    else:
        return jsonify({"message":f'No existe ningun detalle de login con el id_logged {pId_logged}'})

@app.route('/login_detalle/', methods=['GET'])
def login_details():
    log_d = Login_detail()
    return jsonify(log_d.selectLogin_detail())

@app.route('/login_detalle/', methods=['POST'])
def addLogin_detail():
    log_d = Login_detail(id_logged=request.json['id_logged'], f_ultimo_login=request.json['f_ultimo_login'], tiempo_log=request.json['tiempo_log'])
    if log_d.insertLogin_detail():
        return jsonify({'message':'Detalle de login creado exitosamente', 'Login_detail': log_d.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el detalle de login'})

@app.route('/login_detalle/<int:pId>', methods=['PUT'])
def updateLogin_detail(pId):
    log_d = Login_detail(id=pId)
    if log_d.searchLogin_detail():
        log_d.setId(request.json['id'])
        if log_d.updateLogin_detail():
            return jsonify({'message':'Detalle de login Actualizado Exitosamente', 'Login_detail':log_d.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el detalle de login'})


@app.route('/login_detalle/<int:pId>', methods=['DELETE'])
def deleteLogin_detail(pId):
    log_d = Login_detail(id=pId)
    if log_d.searchLogin_detail():
        if log_d.deleteLogin_detail():
            return jsonify({
                'message': 'El detalle de login fue eliminado exitosamente',
                'Login_detail': log_d.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el detalle de login'})
    else:
        return jsonify({'message':'No se encontro ningun detalle de login para eliminar'})

#-------------------------------------------------FIN LOGIN_DETAIL---------------------------------

#-------------------------------------   PERSONA --------------------------------------------------

@app.route('/persona/<string:pRun>', methods=['GET'])
def persona(pRun):
    per = Persona(run=pRun)
    if per.searchPersona():
        return jsonify({'message': 'Persona encontrada exitosamente', 'Persona': per.dic()})
    else:
        return jsonify({"message":f'No existe ninguna persona con el nombre {pRun}'})

@app.route('/persona/', methods=['GET'])
def personas():
    per = Persona()
    return jsonify(per.selectPersonas())

@app.route('/persona/', methods=['POST'])
def addPersona():
    per = Persona(run=request.json['run'], dv=request.json['dv'],nombres=request.json['nombre'], a_paterno=request.json['a_paterno'],a_materno=request.json['a_materno'],
                  idGenero=request.json['idgenero'],fono=request.json['n_contacto'], fecha_n=request.json['fecha_n'],email=request.json['email'], idComuna=request.json['idcomuna'])
    if per.insertPersona():
        return jsonify({'message':'Persona agregada exitosamente', 'Persona': per.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar agregar la persona'})

@app.route('/persona/<string:pRun>', methods=['PUT'])
def updatePersona(pRun):
    per = Persona(run=pRun)
    if per.searchPersona():
        per.setRun(request.json['run'])
        per.setDv(request.json['dv'])
        per.setNombres(request.json['nombre'])
        per.setA_paterno(request.json['a_paterno'])
        per.setA_materno(request.json['a_materno'])
        per.setIdgenero(request.json['idgenero'])
        per.setFono(request.json['n_contacto'])
        per.setFecha_n(request.json['fecha_n'])
        per.setEmail(request.json['email'])
        per.setIdcomuna(request.json['idcomuna'])
        if per.updatePersona():
            return jsonify({'message':'Datos de la persona actualizados Exitosamente', 'Persona':per.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar los datos de la persona'})
    else:
        return jsonify({'message':'No encontro nada...'})

@app.route('/persona/<string:pRun>', methods=['DELETE'])
def deletePersona(pRun):
    per = Persona(run=pRun)
    if per.searchPersona():
        if per.deletePersona():
            return jsonify({
                'message': 'Los datos de la persona fueron eliminados exitosamente','Persona': per.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar los datos de la persona'})
    else:
        return jsonify({'message':'No se encontraron datos de la persona'})


#---------------------------------------FIN PERSONA ---------------------------------------------------



if __name__ == '__main__':
 app.run(debug=True)