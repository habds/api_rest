import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class Region(): 
   def __init__(self,id = 0,nombre = ''): 
      self.id = id
      self.nombre = nombre
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      if len(nombre)<81:
         self.nombre = nombre
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre

   def getRegion(self):
      try:
         self.db.cursor.execute(f'select idRegion, nombre_region from Region where nombre_region="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getRegionId(self):
      try:
         self.db.cursor.execute(f'select idRegion, nombre_region from Region where idRegion="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def getRegiones(self):
      self.db.cursor.execute('select idRegion, nombre_region from Region')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Regiones', 'Regiones': listaDatos}
      return result


   def setRegion(self):
      try:
         self.db.cursor.execute(f'insert into Region(nombre_region) values("{self.nombre}")')
         self.db.cursor.execute("commit;")
         self.getRegion()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateRegion(self):
      try:
         self.db.cursor.execute(f"update Region set nombre_region='{self.nombre}' where idRegion={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteRegion(self):
      try:
         self.db.cursor.execute(f"delete from Region where nombre_region='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre}
      return diccionario

 
   def __str__(self):
      return str(self.id), str(self.nombre), str(self.codigo)
