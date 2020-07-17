import sys, os
sys.path.append(os.getcwd())

from flask import Flask, jsonify, request


from Model.Comuna import Comuna
from Model.Region import Region
from Model.Producto import Producto
from Model.Categoria import Categoria
from Model.Provincia import Provincia
from Model.TiendaTipo import TiendaTipo
from Model.Tienda import Tienda
from Model.Rol import Rol
from Model.Sexo import Sexo
from Model.Persona import Persona
from Model.Login_detail import Login_detail
from Model.Login import Login
from Model.Metodo_pago import Metodo_pago
from Model.PagoTienda import PagoTienda
from Model.Ticket import Ticket
from Model.Support import Support
from Model.Publicidad import Publicidad
from Model.Report_type import Report_type
from Model.Report import Report
from Model.Usr_comment import Usr_comment
from Model.Usr_msg import USR_MSG

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
        return jsonify({"message":f'No existe ningun login con el id {pId}'})

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
    if log.searchLoginById():
        log.setUsername(request.json['username'])
        log.setPassword(request.json['password'])
        log.setIdpersona(request.json['idPersona'])
        log.setIdrol(request.json['idRol'])
        if log.updateLogin():
            return jsonify({'message':'Datos de login actualizados exitosamente', 'login':log.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar los datos de login'})
    else:
        return jsonify({'message':f'No se ha encontrado ningun Usuario con el Id {pId}'})


@app.route('/login/<int:pId>', methods=['DELETE'])
def deleteLogin(pId):
    log = Login(id=pId)
    if log.searchLoginbyId():
        if log.deleteLogin():
            return jsonify({
                'message': 'Los datos para logearse fueron eliminados exitosamente',
                'Login': log.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar los datos para logearse'})
    else:
        return jsonify({f'message':f'No se encontro ningun dato para eliminar con el id: {pId}'})


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
        try:
            token = request.json['token'] 
            tokenD = jwt.decode(token, app.config['SECRET_KEY'])
            print(tokenD)
            return ƒ(*args, **kwargs)
        except jwt.DecodeError:
            return jsonify({'message' : 'Token Invalido'})
        except Exception as e:
            return jsonify({'message' : 'No hay Token'})
    return decorated

@app.route('/loginn/<string:pId>', methods=['GET'])
def loginn(pId):
    log = Login(username=pId)
    if log.searchLoginByNombre():
        return jsonify(log.dic())
    else:
        return jsonify({"message":f'No existe ningun sexo con el nombre {pId}'})

#--------------------------------------- FIN login-------------------------------------------------




#------------------------------------Comuna-------------------------------------------------------------
@app.route('/comuna/<string:nombre_comuna>', methods=['GET'])

def comuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        return jsonify(com.dic())
        
    else:
        return jsonify({"Message":f'No existe ninguna comuna con el nombre {nombre_comuna}'})


@app.route('/comuna/', methods=['GET'])
#@token_required
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
    #tokenope = request.json['token']
    com = Comuna(nombre=request.json['nombre'], idProvincia=request.json['idProvincia'])
    if com.setComuna():
        return jsonify(com.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar crear la Comuna'})

@app.route('/comuna/<string:nombre_comuna>', methods=['PUT'])
def updateComuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        com.setNombre(request.json['nombre'])
        com.setIdProvincia(request.json['idProvincia'])
        if com.updateComuna():
            return jsonify(com.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar la Comuna'})


@app.route('/comuna/<string:nombre_comuna>', methods=['DELETE'])
def deleteComuna(nombre_comuna):
    com = Comuna(nombre=nombre_comuna)
    if com.getComuna():
        if com.deleteComuna():
            return jsonify(com.dic())
        else:
            return jsonify({'Message':f'No ha sido posible eliminar la comuna {nombre_comuna}'})
    else:
        return jsonify({'Message':'No se encontro ninguna comuna para eliminar'})




#------------------------------------Fin Comunas-------------------------------------------------------------

#------------------------------------Region-------------------------------------------------------------

@app.route('/region/<string:nombre_region>', methods=['GET'])
def region(nombre_region):
    reg = Region(nombre=nombre_region)
    if reg.getRegion():
        return jsonify(reg.dic())
    else:
        return jsonify({"Message":f'No existe ninguna region con el nombre {nombre_region}'})

@app.route('/region/', methods=['GET'])
# @token_required
def regiones():
    reg = Region()
    return jsonify(reg.getRegiones())

@app.route('/region/', methods=['POST'])
def addRegion():
    reg = Region(nombre=request.json['nombre'])
    if reg.setRegion():
        return jsonify(reg.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar crear la Region'})

@app.route('/region/<string:nombre_region>', methods=['PUT'])
def updateRegion(nombre_region):
    reg = Region(nombre=nombre_region)
    if reg.getRegion():
        reg.setNombre(request.json['nombre'])
        if reg.updateRegion():
            return jsonify(reg.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar la Region'})


@app.route('/region/<string:nombre_region>', methods=['DELETE'])
def deleteRegion(nombre_region):
    reg = Region(nombre=nombre_region)
    if reg.getRegion():
        if reg.deleteRegion():
            return jsonify(reg.dic())
        else:
            return jsonify({'Message':'No ha sido posible eliminar la region'})
    else:
        return jsonify({'Message':'No se encontro ninguna region para eliminar'})

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
    prod = Producto(nombre=request.json['nombre'], descripcion=request.json['descripcion'], precio=request.json['precio'], idcategoria=request.json['idCategoria'])
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
        prod.idcategoria = request.json['idCategoria']
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
        return jsonify(cat.dic())
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
        return jsonify(cat.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar crear la Categoria'})

@app.route('/categoria/<string:nombre_categoria>', methods=['PUT'])
def updateCategoria(nombre_categoria):
    cat = Categoria(nombre=nombre_categoria)
    if cat.getCategoria():
        cat.setNombre(request.json['nombre'])
        if cat.updateCategoria():
            return jsonify(cat.dic())
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Categoria'})


@app.route('/categoria/<string:nombre_categoria>', methods=['DELETE'])
def deleteCategoria(nombre_categoria):
    cat = Categoria(nombre=nombre_categoria)
    if cat.getCategoria():
        if cat.deleteCategoria():
            return jsonify(cat.dic())
        else:
            return jsonify({'Message':'No ha sido posible eliminar la categoria'})
    else:
        return jsonify({'Message':'No se encontro ninguna categoria para eliminar'})

#------------------------------------------------------------------
#----------------------provincia----------------------------------------
@app.route('/provincia/<string:nombre_provincia>', methods=['GET'])
def provincia(nombre_provincia):
    pro = Provincia(nombre=nombre_provincia)
    if pro.getProvincia():
        return jsonify(pro.dic())
    else:
        return jsonify({"Message":f'No existe ninguna provincia con el nombre {nombre_provincia}'})

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
        return jsonify(pro.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar crear la Provincia'})

@app.route('/provincia/<string:nombre_provincia>', methods=['PUT'])
def updateProvincia(nombre_provincia):
    pro = Provincia(nombre=nombre_provincia)
    if pro.getProvincia():
        pro.setNombre(request.json['nombre'])
        pro.setIdregion(request.json['idRegion'])
        if pro.updateProvincia():
            return jsonify(pro.dic())
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar la Provincia'})

@app.route('/provincia/<string:nombre_provincia>', methods=['DELETE'])
def deleteProvincia(nombre_provincia):
    pro = Provincia(nombre=nombre_provincia)
    if pro.getProvincia():
        if pro.deleteProvincia():
            return jsonify(pro.dic())
        else:
            return jsonify({'message':'No ha sido posible eliminar la region'})
    else:
        return jsonify({'message':'No se encontro ninguna region para eliminar'})
#-----------------fin provincia----------------------------------

#-----------------Tienda Tipo---------------------------------------
@app.route('/tiendatipo/<string:pDescr>', methods=['GET'])
def tiendaTipo(pDescr):
    tie = TiendaTipo(descripcion=pDescr)
    if tie.getTiendaTipo():
        return jsonify(tie.dic())
    else:
        return jsonify({"Message":f'No existe ningun tipo de tienda con ese nombre {pDescr}'})

@app.route('/tiendatipo/', methods=['GET'])
def tiendaTipos():
    tie = TiendaTipo()
    return jsonify(tie.selectTiendaTipos())

@app.route('/tiendatipo/', methods=['POST'])
def addTiendaTipo():
    tie = TiendaTipo(descripcion=request.json['descripcion'])
    if tie.createTiendaTipo():
        return jsonify(tie.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar crear el Tipo de tienda'})

@app.route('/tiendatipo/<string:pDesc>', methods=['PUT'])
def updateTiendaTipo(pDesc):
    tie = TiendaTipo(descripcion=pDesc)
    if tie.getTiendaTipo():
        tie.setDescripcion(request.json['descripcion'])
        if tie.updateTiendaTipo():
            return jsonify(tie.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar la Tienda tipo'})

@app.route('/tiendatipo/<string:pDesc>', methods=['DELETE'])
def deleteTiendaTipo(pDesc):
    tie = TiendaTipo(descripcion=pDesc)
    if tie.getTiendaTipo():
        if tie.deleteTiendaTipo():
            return jsonify(tie.dic())
        else:
            return jsonify({'Message':'No ha sido posible eliminar el tipo de tienda '})
    else:
        return jsonify({'Message':'No se encontro ninguna Tipo de tienda para eliminar'})


#---------------------fin Tienda Tipo-----------------

#-----------------------Tienda-------------------------------------------------------------
@app.route('/tienda/<string:pNombre>', methods=['GET'])
def tienda(pNombre):
    tie = Tienda(nombre=pNombre)
    if tie.selectTienda():
        return jsonify(tie.dic())
    else:
        return jsonify({"Message":f'No existe ninguna provincia con el nombre {pNombre}'})

@app.route('/tienda/', methods=['GET'])
def tiendas():
    tie = Tienda()
    return jsonify(tie.selectTiendas())

@app.route('/tienda/', methods=['POST'])
def addTienda():
    tie = Tienda(nombre=request.json['nombre'], direccion=request.json['direccion'], email=request.json['email'], telefono=request.json['telefono'],idComuna=request.json['idComuna'], idTipoTienda=request.json['idTipoTienda'])
    if tie.createTienda():
        return jsonify(tie.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar crear la Tienda'})

@app.route('/tienda/<string:pNombre>', methods=['PUT'])
def updateTienda(pNombre):
    tie = Tienda(nombre=pNombre)
    if tie.selectTienda():
        tie.setNombre(request.json['nombre'])
        tie.setDireccion(request.json['direccion'])
        tie.setEmail(request.json['email'])
        tie.setTelefono(int(request.json['telefono']))
        tie.setIdComuna(int(request.json['idComuna']))
        tie.setIdtipotienda(int(request.json['idTipoTienda']))
        if tie.updateTiendaTipo():
            return jsonify(tie.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar la Tienda'})

@app.route('/tienda/<string:pNombre>', methods=['DELETE'])
def deleteTienda(pNombre):
    tie = Tienda(nombre=pNombre)
    if tie.selectTienda():
        if tie.deleteTienda():
            return jsonify(tie.dic())
        else:
            return jsonify({'Message':'No ha sido posible eliminar la tienda '})
    else:
        return jsonify({'Message':'No se encontro ninguna tienda para eliminar'})

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
    rol = Rol(nombre=request.json['nombre'])
    if rol.insertRol():
        return jsonify({'message':'Rol creado exitosamente', 'Rol': rol.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Rol'})

@app.route('/rol/<string:pNombre>', methods=['PUT'])
def updateRol(pNombre):
    rol = Rol(nombre=pNombre)
    if rol.searchRol():
        rol.setNombre(request.json['nombre'])
        
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
                  correo=request.json['correo'],fono=request.json['fono'], fono2=request.json['fono2'], fono3=request.json['fono3'], idComuna=request.json['idComuna'],idGenero=request.json['idGenero'])
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
        per.setEmail(request.json['correo'])
        per.setFono(request.json['fono'])
        per.setFono2(request.json['fono2'])
        per.setFono3(request.json['fono3'])
        per.setIdcomuna(request.json['idComuna'])
        per.setIdgenero(request.json['idGenero'])
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

#--------------------------------------Metodo Pago------------------------------------------------
@app.route('/metodopago/<string:pNombre>', methods=['GET'])
def metodoPago(pNombre):
    met = Metodo_pago(nombre=pNombre)
    if met.searchMetodoPago():
        return jsonify(met.dic())
    else:
        return jsonify({"Message":f'No existe ninguna metodo de pago con el nombre {pNombre}'})

@app.route('/metodopago/', methods=['GET'])
def metodosPagos():
    met = Metodo_pago()
    return jsonify(met.selectMetodoPago())

@app.route('/metodopago/', methods=['POST'])
def addMetodoPago():
    met = Metodo_pago(nombre=request.json['nombre'])
    if met.insertMetodoPago():
        return jsonify(met.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar agregar el metodo de pago'})

@app.route('/metodopago/<string:pNombre>', methods=['PUT'])
def updateMetodooPago(pNombre):
    met = Metodo_pago(nombre=pNombre)
    if met.searchMetodoPago():
        met.setNombre(request.json['nombre'])
        if met.updateMetodoPago():
            return jsonify(met.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar el metodo de pago'})
    else:
        return jsonify({'Message':'No encontro nada...'})

@app.route('/metodopago/<string:pNombre>', methods=['DELETE'])
def deleteMetodoPago(pNombre):
    met = Metodo_pago(nombre=pNombre)
    if met.searchMetodoPago():
        if met.deleteMetodoPago():
            return jsonify(met.dic())
        else:
            return jsonify({'Message':'No ha sido posible eliminar los datos del metodo de pago'})
    else:
        return jsonify({'Message':'No se encontraron datos del metodo de pago'})
#---------------------------------------fin metodo pago---------------------------------------------
#-------------------------------------PAGO TIENDA-----------------------------------------------------
@app.route('/pagotienda/<int:pId>', methods=['GET'])
def pagotienda(pId):
    pag = PagoTienda(id=pId)
    if pag.searchPagoTienda():
        return jsonify(pag.dic())
    else:
        return jsonify({"Message":f'No existe ningun pago de tienda con el id {pId}'})

@app.route('/pagotienda/', methods=['GET'])
def pagostienda():
    pag = PagoTienda()
    return jsonify(pag.selectPagoTienda())

@app.route('/pagotienda/', methods=['POST'])
def addPagoTienda():
    pag = PagoTienda(idTienda=request.json['idtienda'], idMetodoPago = request.json['idmetodopago'])
    if pag.insertPagoTienda():
        return jsonify(pag.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar agregar el pago tienda'})

@app.route('/pagotienda/<int:pId>', methods=['PUT'])
def updatePagoTienda(pId):
    pag = PagoTienda(id=pId)
    if pag.searchPagoTienda():
        pag.setIdtienda(request.json['idtienda'])
        pag.setIdmetodopago(request.json['idmetodopago'])
        if pag.updatePagoTienda():
            return jsonify(pag.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar el pago tienda'})
    else:
        return jsonify({'Message':'No encontro nada...'})

@app.route('/pagotienda/<int:pId>', methods=['DELETE'])
def deletePagoTienda(pId):
    pag = PagoTienda(id=pId)
    if pag.searchPagoTienda():
        if pag.deletePagoTienda():
            return jsonify(pag.dic())
        else:
            return jsonify({'Message':f'No ha sido posible eliminar los pago de tienda con id : {pId}'})
    else:
        return jsonify({'Message':'No se encontraron datos del pago tienda'})

#-----------------------------------------FIN PAGO TIENDA----------------------------------------------------

#-------------------------------------------------TICKET------------------------------------------------------------
@app.route('/ticket/<int:pId>', methods=['GET'])
def ticket(pId):
    tic = Ticket(id=pId)
    if tic.searchTicket():
        return jsonify(tic.dic())
    else:
        return jsonify({"Message":f'No existe ningun ticket con el id {pId}'})

@app.route('/ticket/', methods=['GET'])
def tickes():
    tic = Ticket()
    return jsonify(tic.selectTicket())

@app.route('/ticket/', methods=['POST'])
def addTicket():
    tic = Ticket(ticket_abierto=request.json['ticket_abierto'], estado = request.json['estado'])
    if tic.insertTicket():
        return jsonify(tic.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar agregar el ticket'})

@app.route('/ticket/<int:pId>', methods=['PUT'])
def updateTicket(pId):
    tic = Ticket(id=pId)
    if tic.searchTicket():
        tic.setTicket_abierto(request.json['ticket_abierto'])
        tic.setEstado(request.json['estado'])
        if tic.updateTicket():
            return jsonify(tic.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar el ticket'})
    else:
        return jsonify({'Message':'No encontro nada...'})

@app.route('/ticket/<int:pId>', methods=['DELETE'])
def deleteTicket(pId):
    tic = Ticket(id=pId)
    if tic.searchTicket():
        if tic.deleteTicket():
            return jsonify(tic.dic())
        else:
            return jsonify({'Message':f'No ha sido posible eliminar el ticket con id : {pId}'})
    else:
        return jsonify({'Message':'No se encontraron datos del ticket'})


#------------------------------------------------FIN TICKET-----------------------------------------------------------
#--------------------------------------------------SUPPORT ----------------------------------------------------------------
@app.route('/soporte/<int:pId>', methods=['GET'])
def support(pId):
    sup = Support(id=pId)
    if sup.searchSup():
        return jsonify(sup.dic())
    else:
        return jsonify({"Message":f'No existe ningun ticket con el id {pId}'})

@app.route('/soporte/', methods=['GET'])
def supports():
    sup = Support()
    return jsonify(sup.selectSup())

@app.route('/soporte/', methods=['POST'])
def addSupport():
    sup = Support(estatus=request.json['estatus'], codigo = request.json['codigo'], idTicket = request.json['idticket'])
    if sup.insertSup():
        return jsonify(sup.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar agregar el ticket'})

@app.route('/soporte/<int:pId>', methods=['PUT'])
def updateSupport(pId):
    sup = Support(id=pId)
    if sup.searchSup():
        sup.setEstatus(request.json['estatus'])
        sup.setCodigo(request.json['codigo'])
        sup.setIdTicket(request.json['idticket'])
        if sup.updateSup():
            return jsonify(sup.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar el support'})
    else:
        return jsonify({'Message':'No encontro nada...'})

@app.route('/soporte/<int:pId>', methods=['DELETE'])
def deleteSupport(pId):
    sup = Support(id=pId)
    if sup.searchSup():
        if sup.deleteSup():
            return jsonify(sup.dic())
        else:
            return jsonify({'Message':f'No ha sido posible eliminar el ticket con id : {pId}'})
    else:
        return jsonify({'Message':'No se encontraron datos del support'})
#-----------------------------------------------FIN SUPPORT ------------------------------------------------------------------

#-------------------------------------------------PUBLICIDAD------------------------------------------------------------------
@app.route('/publicidad/<int:pId>', methods=['GET'])
def publicidad(pId):
    pub = Publicidad(id=pId)
    if pub.search():
        return jsonify(pub.dic())
    else:
        return jsonify({"Message":f'No existe ninguna publicidad con el id: {pId}'})

@app.route('/publicidad/', methods=['GET'])
def publicidades():
    pub = Publicidad()
    return jsonify(pub.select())

@app.route('/publicidad/', methods=['POST'])
def addPublicidad():
    pub = Publicidad(f_inicio=request.json['inicio'], f_termino = request.json['termino'], compania = request.json['nombre'])
    if pub.insert():
        return jsonify(pub.dic())
    else:
        return jsonify({'Message':'Ha ocurrido un error al intentar agregar la publicidad'})

@app.route('/publicidad/<int:pId>', methods=['PUT'])
def updatePublicidad(pId):
    pub = Publicidad(id=pId)
    if pub.search():
        pub.setF_inicio(request.json['inicio'])
        pub.setF_termino(request.json['termino'])
        pub.setCompania(request.json['nombre'])
        if pub.update():
            return jsonify(pub.dic())
        else:
            return jsonify({'Message':'Ha ocurrido un error al intentar actualizar la publicidad'})
    else:
        return jsonify({'Message':'No encontro nada...'})

@app.route('/publicidad/<int:pId>', methods=['DELETE'])
def deletePublicidad(pId):
    pub = Publicidad(id=pId)
    if pub.search():
        if pub.delete():
            return jsonify(pub.dic())
        else:
            return jsonify({'Message':f'No ha sido posible eliminar la publicidad con id : {pId}'})
    else:
        return jsonify({'Message':'No se encontraron datos de la publicidad'})


#-----------------------------------------------FIN PUBLICIDAD------------------------------------------------------------------


#------------------------------------Report_Type-------------------------------------------------------------
@app.route('/reportetipo/<int:idreporttype>', methods=['GET'])

def report_type(idreporttype):
    rep = Report_type(id=idreporttype)
    if rep.getReportType():
        return jsonify({'message': 'Exitosamente', 'Report_Type': rep.dic()})
    else:
        return jsonify({"message":f'No existe ningun Report_Type con el id {idreporttype}'})


@app.route('/reportetipo/', methods=['GET'])
# @token_required
def report_types():
    rep = Report_type()
    return jsonify(rep.getReportTypes())

@app.route('/reportetipo/', methods=['POST'])
#@token_required
def addReport_Type():
    rep = Report_type(descripcion=request.json['descripcion'], area=request.json['area'], area_code=request.json['area_code'])
    if rep.setReportType():
        return jsonify({'message':'Report Type creado exitosamente', 'Report Type': rep.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Report Type'})

@app.route('/reportetipo/<int:idreport_type>', methods=['PUT'])
def updateReportType(idreport_type):
    rep = Report_type(id=idreport_type)
    if rep.getReportType():
        rep.setDescripcion(request.json['descripcion'])
        rep.setArea(request.json['area'])
        rep.setArea_code(request.json['area_code'])
        if rep.updateReportType():
            return jsonify({'message':'Report Type Actualizado Exitosamente', 'Report Type':rep.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el Report Type'})


@app.route('/reportetipo/<int:idreport_type>', methods=['DELETE'])
def deleteReporteType(idreport_type):
    rep = Report_type(id=idreport_type)
    if rep.getReportType():
        if rep.deleteReportType():
            return jsonify({
                'message': 'El Report Type fue eliminado exitosamente',
                'Report Type': rep.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el Report Type'})
    else:
        return jsonify({'message':'No se encontro ningun Report Type para eliminar'})




#------------------------------------Fin Report Type-------------------------------------------------------------

#------------------------------------Report-------------------------------------------------------------

@app.route('/reporte/<int:idreport>', methods=['GET'])

def reporte(idreport):
    rep = Report(id=idreport)
    if rep.getReport():
        return jsonify({'message': 'Exitosamente', 'Report': rep.dic()})
    else:
        return jsonify({"message":f'No existe ningun Report con el id {idreport}'})


@app.route('/reporte/', methods=['GET'])
# @token_required
def reportes():
    rep = Report()
    return jsonify(rep.getReports())

@app.route('/reporte/', methods=['POST'])
#@token_required
def addReporte():
    rep = Report(descripcion=request.json['descripcion'], codigo=request.json['codigo'], idReport_Type=request.json['idReport_Type'])
    if rep.setReport():
        return jsonify({'message':'Reportcreado exitosamente', 'Report': rep.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el Report'})

@app.route('/reporte/<int:idreport>', methods=['PUT'])
def updateReporte(idreport):
    rep = Report(id=idreport)
    if rep.getReport():
        rep.setDescripcion(request.json['descripcion'])
        rep.setCodigo(request.json['codigo'])
        rep.idreport_type = request.json['idReport_Type']
        if rep.updateReport:
            return jsonify({'message':'Report Actualizado Exitosamente', 'Report':rep.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el Report'})


@app.route('/reporte/<int:idreport>', methods=['DELETE'])
def deleteReporte(idreport):
    rep = Report(id=idreport)
    if rep.getReport():
        if rep.deleteReport():
            return jsonify({
                'message': 'El Report fue eliminado exitosamente',
                'Report': rep.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el Report'})
    else:
        return jsonify({'message':'No se encontro ningun Report para eliminar'})




#------------------------------------Fin Report-------------------------------------------------------------

#------------------------------------USR_Comentario-------------------------------------------------------------

@app.route('/comentario/<int:idcomentario>', methods=['GET'])

def comentario(idcomentario):
    comentario = Usr_comment(id=idcomentario)
    if comentario.getUSR_Comentario():
        return jsonify({'message': 'Exitosamente', 'Comentario': comentario.dic()})
    else:
        return jsonify({"message":f'No existe ningun Comentario con el id {idcomentario}'})


@app.route('/comentario/', methods=['GET'])
# @token_required
def comentarios():
    comentario = Usr_comment()
    return jsonify(comentario.getUSR_Comentarios())

@app.route('/comentario/', methods=['POST'])
#@token_required
def addComentario():
    comentario = Usr_comment(descripcion=request.json['descripcion'], estatus=request.json['estatus'], idUSR_MSG=request.json['idUsr_msg'])
    if comentario.setUSR_Comentario():
        return jsonify({'message':'Comentario creado exitosamente', 'Comentario': comentario.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el comentario'})

@app.route('/comentario/<int:idcomentario>', methods=['PUT'])
def updateComentario(idcomentario):
    comentario = Usr_comment(id=idcomentario)
    if comentario.getUSR_Comentario():
        comentario.setDescripcion(request.json['descripcion'])
        comentario.setEstatus(request.json['estatus'])
        comentario.idUSR_MSG = request.json['idUsr_msg']
        if comentario.updateUSR_Comentario():
            return jsonify({'message':'Comentario Actualizado Exitosamente', 'Comentario':comentario.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el comentario'})


@app.route('/comentario/<int:idcomentario>', methods=['DELETE'])
def deleteComentario(idcomentario):
    comentario = Usr_comment(id=idcomentario)
    if comentario.getUSR_Comentario():
        if comentario.deleteUSR_Comentario():
            return jsonify({
                'message': 'El Comentario fue eliminado exitosamente',
                'Comentario': comentario.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el comentario'})
    else:
        return jsonify({'message':'No se encontro ningun comentario para eliminar'})




#------------------------------------Fin USR_Comentario-------------------------------------------------------------

#------------------------------------Usr_msg-Anuncio-------------------------------------------------------------

@app.route('/anuncio/<int:idanuncio>', methods=['GET'])

def anuncio(idanuncio):
    anuncio = USR_MSG(idUSR_MSG=idanuncio)
    if anuncio.getUsr_msg():
        return jsonify({'message': 'Exitosamente', 'Anuncio': anuncio.dic()})
    else:
        return jsonify({"message":f'No existe ningun Anuncio con el id {idanuncio}'})


@app.route('/anuncio/', methods=['GET'])
# @token_required
def anuncios():
    anuncio = USR_MSG()
    return jsonify(anuncio.getUsr_msgs())

@app.route('/anuncio/', methods=['POST'])
#@token_required
def addAnuncio():
    anuncio = USR_MSG(nombre=request.json['nombre'],descripcion=request.json['descripcion'], precio_anuncio=request.json['precio'], estatus=request.json['estatus'], Rate_Container=request.json['Rate_Container'], idRate_MSG=request.json['idRate_MSG'], idProducto=request.json['idProducto'])
    if anuncio.setUsr_msg():
        return jsonify({'message':'Anuncio creado exitosamente', 'Anuncio': anuncio.dic()})
    else:
        return jsonify({'message':'Ha ocurrido un error al intentar crear el anuncio'})

@app.route('/anuncio/<int:idanuncio>', methods=['PUT'])
def updateAnuncio(idanuncio):
    anuncio = USR_MSG(id=idanuncio)
    if anuncio.getUsr_msg():
        anuncio.setNombre
        anuncio.setDescripcion(request.json['descripcion'])
        anuncio.setPrecio_anuncio(request.json['precio'])
        anuncio.setEstatus(request.json['estatus'])
        anuncio.setRate_container('Rate_Container')
        anuncio.setIdrate_msg(request.json['idRate_MSG'])
        anuncio.setIdproducto(request.json['idProducto'])
        if anuncio.updateUsr_msg():
            return jsonify({'message':'Anuncio Actualizado Exitosamente', 'Anuncio':anuncio.dic()})
        else:
            return jsonify({'message':'Ha ocurrido un error al intentar actualizar el anuncio'})


@app.route('/anuncio/<int:idanuncio>', methods=['DELETE'])
def deleteAnuncio(idanuncio):
    anuncio = USR_MSG(idUSR_MSG=idanuncio)
    if anuncio.getUsr_msg():
        if anuncio.deleteUsr_msg():
            return jsonify({
                'message': 'El Anuncio fue eliminado exitosamente',
                'Anuncio': anuncio.dic()
            })
        else:
            return jsonify({'message':'No ha sido posible eliminar el anuncio'})
    else:
        return jsonify({'message':'No se encontro ningun anuncio para eliminar'})




#------------------------------------Fin Anuncio-------------------------------------------------------------


if __name__ == '__main__':
 app.run(debug=True)