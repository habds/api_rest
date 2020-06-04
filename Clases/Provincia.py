import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector

class Provincia(): 
   def __init__(self,id = 0,nombre = '',idRegion = 0): 
      self.id = id
      self.nombre = nombre
      self.idRegion = idRegion
      self.db =DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setIdregion(self, idRegion):
      self.idRegion = idRegion
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getIdregion(self):
      return self.idRegion

   def getProvincia(self):
      try:
         self.db.cursor.execute(f'select id, nombre,idRegion from provincia where nombre="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.setIdregion(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getProvincias(self):
      self.db.cursor.execute('select id, nombre, idRegion from provincia')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1], 'idRegion':registro[2]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Provincias', 'Provincias': listaDatos}
      return result


   def setProvincia(self):
      try:
         self.db.cursor.execute(f'insert into provincia(nombre,idRegion) values("{self.nombre}","{self.idRegion}")')
         self.db.cursor.execute("commit;")
         self.getProvincia()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateProvincia(self):
      try:
         self.db.cursor.execute(f"update provincia set nombre='{self.nombre}', idRegion={self.idRegion} where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteCategoria(self):
      try:
         self.db.cursor.execute(f"delete from provincia where nombre='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre, 'idRegion':self.idRegion}
      return diccionario

 
   def __str__(self):
      return str(self.id), self.nombre, str(self.idRegion)
