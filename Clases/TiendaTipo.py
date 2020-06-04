import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector

class TiendaTipo(): 
   def __init__(self,id = 0,codigo = '',descripcion = ''): 
      self.id = id
      self.codigo = codigo
      self.descripcion = descripcion
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setCodigo(self, codigo):
      self.codigo = codigo
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def getId(self):
      return self.id
 
   def getCodigo(self):
      return self.codigo
 
   def getDescripcion(self):
      return self.descripcion
 
   def getTiendaTipo(self):
      try:
         self.db.cursor.execute(f'select id, codigo,descripcion from tipo_tienda where codigo="{self.codigo}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setCodigo(f'{obj[1]}')
            self.setDescripcion(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getTiendaTipoId(self):
      try:
         self.db.cursor.execute(f'select id, codigo, descripcion from tipo_tienda where id="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setCodigo(f'{obj[1]}')
            self.setDescripcion(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectTiendaTipos(self):
      self.db.cursor.execute('select id, codigo, descripcion from tipo_tienda')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "codigo": registro[1], 'descripcion':registro[2]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Tipos de tiendas', 'Tipos de tiendas': listaDatos}
      return result


   def createTiendaTipo(self):
      try:
         self.db.cursor.execute(f'insert into tipo_tienda(codigo,descripcion) values("{self.codigo}","{self.descripcion}")')
         self.db.cursor.execute("commit;")
         self.getTiendaTipo()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateTiendaTipo(self):
      try:
         self.db.cursor.execute(f"update tipo_tienda set codigo='{self.codigo}', descripcion='{self.descripcion}' where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteTiendaTipo(self):
      try:
         self.db.cursor.execute(f"delete from tipo_tienda where codigo='{self.codigo}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'codigo': self.codigo, 'descripcion':self.descripcion}
      return diccionario



   def __str__(self):
      return str(self.id), self.codigo, self.descripcion
