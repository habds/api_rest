import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
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
      self.db.cursor.execute(f'select id, nombre, idRegion from ciudad where nombre="{self.nombre}"')
      obj = self.db.cursor.fetchone()
      setId(f'{obj[0]}')
      setNombre(f'{obj[1]}')
      setId(f'{obj[2]}')


   def __str__(self):
      return str(self.id), str(self.nombre)



