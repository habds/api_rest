import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector

class Tienda(): 
   def __init__(self,id = 0,nombre = '',direccion = '',email = '',telefono = '',idComuna = 0,idTipoTienda = 0): 
      self.id = id
      self.nombre = nombre
      self.direccion = direccion
      self.email = email
      self.telefono = telefono
      self.idComuna = idComuna
      self.idTipoTienda = idTipoTienda
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setDireccion(self, direccion):
      self.direccion = direccion
 
   def setEmail(self, email):
      self.email = email
 
   def setTelefono(self, telefono):
      self.telefono = telefono
 
   def setIdComuna(self, idComuna):
      self.idComuna = idComuna
 
   def setIdtipotienda(self, idTipoTienda):
      self.idTipoTienda = idTipoTienda
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getDireccion(self):
      return self.direccion
 
   def getEmail(self):
      return self.email
 
   def getTelefono(self):
      return self.telefono
 
   def getIdComuna(self):
      return self.idComuna
 
   def getIdtipotienda(self):
      return self.idTipoTienda

   def selectTienda(self):
      try:
         self.db.cursor.execute(f'select id, nombre, direccion, email, telefono, idcomuna, idtipotienda from tienda where nombre="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.setDireccion(f'{obj[2]}')
            self.setEmail(f'{obj[3]}')
            self.setTelefono(f'{obj[4]}')
            self.setIdComuna(f'{obj[5]}')
            self.setIdtipotienda(f'{obj[6]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getTiendaId(self):
      try:
         self.db.cursor.execute(f'select id, nombre, direccion, email, telefono, idcomuna, idtipotienda from tienda where id="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.setDireccion(f'{obj[2]}')
            self.setEmail(f'{obj[3]}')
            self.setTelefono(f'{obj[4]}')
            self.setIdComuna(f'{obj[5]}')
            self.setIdtipotienda(f'{obj[6]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectTiendas(self):
      self.db.cursor.execute('select id, nombre, direccion, email, telefono, idcomuna, idtipotienda from tienda')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1],"direccion":registro[2], "email":registro[3],"telefono":registro[4],"idComuna":registro[5],"idTipoTienda":registro[6]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando las tiendas', 'Tiendas': listaDatos}
      return result


   def createTienda(self):
      try:
         self.db.cursor.execute(f'insert into tienda(nombre,direccion,email,telefono,idcomuna,idtipotienda) values("{self.nombre}","{self.direccion}","{self.email}","{self.telefono}","{self.idComuna}","{self.idTipoTienda}")')
         self.db.cursor.execute("commit;")
         self.selectTienda()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return False

   def updateTiendaTipo(self):
      try:
         self.db.cursor.execute(f"update tienda set nombre='{self.nombre}', direccion='{self.direccion}', email='{self.email}', telefono='{self.telefono}', idcomuna={self.idComuna}, idtipotienda={self.idTipoTienda} where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteTienda(self):
      try:
         self.db.cursor.execute(f"delete from tienda where nombre='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre, 'direccion':self.direccion, 'email':self.direccion, 'telefono':self.telefono, 'idComuna':self.idComuna, 'idTipoTienda':self.idTipoTienda}
      return diccionario

 
   def __str__(self):
      return str(self.id), self.nombre, self.direccion, self.email, self.telefono, str(self.idComuna), str(self.idTipoTienda)
