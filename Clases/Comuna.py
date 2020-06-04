import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector
from Clases.Provincia import Provincia
class Comuna(): 

   def __init__(self,id = 0,nombre = '', idProvincia=0): 
      self.id = id
      self.nombre = nombre
      self.idProvincia = idProvincia
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setIdProvincia(self, idProvincia):
      self.idProvincia = idProvincia

   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre

   def getComuna(self):
      try:
         self.db.cursor.execute(f'select id, nombre, idProvincia from comuna where nombre="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.idProvincia = obj[2]
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getComunas(self):
      self.db.cursor.execute('select id, nombre, idProvincia from comuna')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1], 'idProvincia': registro[2]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Comunas', 'Comunas': listaDatos}
      return result


   def setComuna(self):
      try:
         self.db.cursor.execute(f'insert into comuna(nombre, idProvincia) values("{self.nombre}",{self.idProvincia})')
         self.db.cursor.execute("commit;")
         self.getComuna()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateComuna(self):
      try:
         self.db.cursor.execute(f"update comuna set nombre='{self.nombre}', idProvincia={self.idProvincia} where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteComuna(self):
      try:
         self.db.cursor.execute(f"delete from comuna where nombre='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False
   
   def filtrarProvincia(self, provinciaid):
      try:
         self.db.cursor.execute(f"select nombre, idProvincia from comuna where idProvincia = {provinciaid}")
         data = self.db.cursor.fetchall()
         dicDatos = {}
         listaDatos = []
         provinciaope = Provincia(id=provinciaid)
         provinciaope.getProvincia()
         for registro in data:
            dicDatos = {"id": registro[0], "nombre": registro[1], 'idProvincia': registro[2]}
            listaDatos.append(dicDatos)
         result = {'Message': f'Mostrando Comunas de {provinciaope.nombre}', 'Comunas': listaDatos}
         return result   
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre, 'idProvincia': self.idProvincia}
      return diccionario

   def __str__(self):
      return str(self.id), str(self.nombre)



