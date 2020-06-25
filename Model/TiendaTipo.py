import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class TiendaTipo(): 
   def __init__(self,id = 0,descripcion = ''): 
      self.id = id
      self.descripcion = descripcion
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setDescripcion(self, descripcion):
      if len(descripcion)<46:
         self.descripcion = descripcion
 
   def getId(self):
      return self.id
 
   def getDescripcion(self):
      return self.descripcion
 
   def getTiendaTipo(self):
      try:
         self.db.cursor.execute(f'select idTipo_Tienda, descr from Tipo_Tienda where descr="{self.descripcion}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setDescripcion(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getTiendaTipoId(self):
      try:
         self.db.cursor.execute(f'select idTipo_Tienda, descr from Tipo_Tienda where idTipo_Tienda="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setDescripcion(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectTiendaTipos(self):
      self.db.cursor.execute('select idTipo_Tienda, descr from Tipo_Tienda')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], 'descripcion':registro[1]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Tipos de tiendas', 'Tipos de tiendas': listaDatos}
      return result


   def createTiendaTipo(self):
      try:
         self.db.cursor.execute(f'insert into Tipo_Tienda(descr) values("{self.descripcion}")')
         self.db.cursor.execute("commit;")
         self.getTiendaTipo()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateTiendaTipo(self):
      try:
         self.db.cursor.execute(f"update Tipo_Tienda set descr='{self.descripcion}' where idTipo_Tienda={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteTiendaTipo(self):
      try:
         self.db.cursor.execute(f"delete from Tipo_Tienda where descr='{self.descripcion}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'descripcion':self.descripcion}
      return diccionario

   def __str__(self):
      return str(self.id), self.descripcion
