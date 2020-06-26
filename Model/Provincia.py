import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
from Model.Region import Region
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
      if len(nombre)<81:
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
         self.db.cursor.execute(f'select idProvincia, nombre_provincia,idRegion from Provincia where nombre_provincia="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.setIdregion(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def filtroRegion(self, region_id):
      try:
         self.db.cursor.execute(f'select idProvincia, nombre_provincia, idRegion from Provincia where idRegion = {region_id}')
      
         data = self.db.cursor.fetchall()
         dicDatos = {}
         listaDatos = []
         regionope = Region(id=region_id)
         regionope.getRegionId()
         for registro in data:
            dicDatos = {"id": registro[0], "nombre": registro[1], 'idRegion':registro[2]}
            listaDatos.append(dicDatos)
         result = {'Message': f'Mostrando Provincias de {regionope.nombre}', 'Provincias': listaDatos}
         return result
      except mysql.connector.Error as err:
         print(err)
         return None

   def getProvinciaId(self):
      try:
         self.db.cursor.execute(f'select idProvincia, nombre_provincia, idRegion from Provincia where idProvincia="{self.id}"')
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
      self.db.cursor.execute('select idProvincia, nombre_provincia, idRegion from Provincia')
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
         self.db.cursor.execute(f'insert into Provincia(nombre_provincia,idRegion) values("{self.nombre}","{self.idRegion}")')
         self.db.cursor.execute("commit;")
         self.getProvincia()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateProvincia(self):
      try:
         self.db.cursor.execute(f"update Provincia set nombre_provincia='{self.nombre}', idRegion={self.idRegion} where idProvincia={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteProvincia(self):
      try:
         self.db.cursor.execute(f"delete from Provincia where nombre_provincia='{self.nombre}'")
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
