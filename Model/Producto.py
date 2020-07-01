import sys, os
sys.path.append(os.getcwd())
from conexion2 import DataBaseConexion
import mysql.connector

class Producto(): 
   def __init__(self,id = 0,nombre = '',descripcion = '',precio = '', idcategoria=0): 
      self.id = id
      self.nombre = nombre
      self.descripcion = descripcion
      self.precio = precio
      self.db = DataBaseConexion()
      self.idcategoria = idcategoria
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setPrecio(self, precio):
      self.precio = precio
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getDescripcion(self):
      return self.descripcion
 
   def getPrecio(self):
      return self.precio

   def getProducto(self):
      try:
         self.db.cursor.execute(f'select idProducto, nombre_producto, descripcion, precio, idCategoria from Producto where idProducto={self.id}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.setDescripcion(obj[2])
            self.setPrecio(obj[3])
            self.idcategoria = obj[4]
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getProductoByNombre(self):
      try:
         self.db.cursor.execute(f'select idProducto, nombre_producto, descripcion, precio, idCategoria from Producto where nombre_producto="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            self.setDescripcion(obj[2])
            self.setPrecio(obj[3])
            self.idcategoria = obj[4]
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getProductos(self):
      self.db.cursor.execute('select idProducto, nombre_producto, descripcion, precio, idCategoria from Producto')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1], 'descripcion': registro[2], 'precio': registro[3], 'idcategoria':registro[4]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Productos', 'Productos': listaDatos}
      return result


   def setProducto(self):
      try:
         self.db.cursor.execute(f'insert into Producto(nombre_producto, descripcion, precio, idCategoria) values("{self.nombre}","{self.descripcion}", {self.precio}, {self.idcategoria})')
         self.db.cursor.execute("commit;")
         self.getProductoByNombre()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateProducto(self):
      try:
         self.db.cursor.execute(f"update Producto set nombre_producto='{self.nombre}', descripcion='{self.descripcion}', precio={self.precio}, idCategoria={self.idcategoria} where idProducto={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteProducto(self):
      try:
         self.db.cursor.execute(f"delete from Producto where idProducto={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre, 'descripcion': self.descripcion, 'precio': self.precio, 'idcategoria': self.idcategoria}
      return diccionario


 
   def __str__(self):
      return str(self.id), self.nombre, self.descripcion, str(self.precio)
