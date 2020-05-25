import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector
class Ciudad(): 

   def __init__(self,id = 0,nombre = '', idRegion=0): 
      self.id = id
      self.nombre = nombre
      self.idRegion = idRegion
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre

   def getCiudad(self):
      try:
         self.db.cursor.execute(f'select id, nombre, idRegion from ciudad where nombre="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         self.setId(f'{obj[0]}')
         self.setNombre(f'{obj[1]}')
         self.setId(f'{obj[2]}')
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getCiudades(self):
      self.db.cursor.execute('select id, nombre, idRegion from ciudad')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1], 'idRegion': registro[2]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Ciudades', 'Ciudades': listaDatos}
      return result

   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre, 'idregion': self.idRegion}
      return diccionario

   def __str__(self):
      return str(self.id), str(self.nombre)



