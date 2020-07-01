import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector


class Rol(): 
   def __init__(self,id = 0,nombre = '',codigo = ''): 
      self.id = id
      self.nombre = nombre
      self.codigo = codigo
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setCodigo(self, codigo):
      self.codigo = codigo
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getCodigo(self):
      return self.codigo

   def searchRol(self):
      try:
         self.db.cursor.execute(f'select idRoles, nombre_rol from Roles where nombre_rol="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def searchRolById(self):
      try:
         self.db.cursor.execute(f'select idRoles, nombre_rol from Roles where idRoles="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def selectRoles(self):
      self.db.cursor.execute('select idRoles, nombre_rol from Roles')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []
      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Roles', 'Roles': listaDatos}
      return result


   def insertRol(self):
      try:
         self.db.cursor.execute(f'insert into Roles(nombre_rol) values("{self.nombre}")')
         self.db.cursor.execute("commit;")
         self.searchRol()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateRol(self):
      try:
         self.db.cursor.execute(f"update Roles set nombre_roles='{self.nombre}' where idRoles={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteRol(self):
      try:
         self.db.cursor.execute(f"delete from Roles where nombre_rol='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre}
      return diccionario

 
   def __str__(self):
      return str(self.id), self.nombre, self.codigo
