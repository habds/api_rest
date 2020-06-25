import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector

class Sexo(): 
   def __init__(self,id = 0,nombre = ''): 
      self.id = id
      self.nombre = nombre
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre

   def getSexo(self):
      try:
         self.db.cursor.execute(f'select id, nombre from sexo where nombre="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def getSexos(self):
      self.db.cursor.execute('select id, nombre from sexo')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Sexos', 'Sexos': listaDatos}
      return result


   def setSexo(self):
      try:
         self.db.cursor.execute(f'insert into sexo(nombre) values("{self.nombre}")')
         self.db.cursor.execute("commit;")
         self.getSexo()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateSexo(self):
      try:
         self.db.cursor.execute(f"update sexo set nombre='{self.nombre}' where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteSexo(self):
      try:
         self.db.cursor.execute(f"delete from sexo where nombre='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre}
      return diccionario

 
   def __str__(self):
      return str(self.id), str(self.nombre)
