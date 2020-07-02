import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class Metodo_pago(): 
   def __init__(self,id = 0,nombre = ''): 
      self.id = id
      self.nombre = nombre
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      if len(nombre)<46:
         self.nombre = nombre
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
   
   def searchMetodoPago(self):
      try:
         self.db.cursor.execute(f'select idMetodo_Pago, nombre_metodoPago from Metodo_Pago where nombre_metodoPago="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectMetodoPago(self):
      self.db.cursor.execute('select idMetodo_Pago, nombre_metodoPago from Metodo_Pago')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1]}
         listaDatos.append(dicDatos)
      result = listaDatos
      return result


   def insertMetodoPago(self):
      try:
         self.db.cursor.execute(f'insert into Metodo_Pago(nombre_metodoPago) values("{self.nombre}")')
         self.db.cursor.execute("commit;")
         self.searchMetodoPago()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateMetodoPago(self):
      try:
         self.db.cursor.execute(f"update Metodo_Pago set nombre_metodopago='{self.nombre}' where idMetodo_Pago={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteMetodoPago(self):
      try:
         self.db.cursor.execute(f"delete from Metodo_Pago where nombre_metodopago='{self.nombre}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False
   
   # def filtrarProvincia(self, provinciaid):
   #    try:
   #       self.db.cursor.execute(f"select idMetodo_Pago, nombre_metodoPago from Metodo_Pago where idMetodo_Pago = {provinciaid}")
   #       data = self.db.cursor.fetchall()
   #       dicDatos = {}
   #       listaDatos = []
   #       provinciaope = Provincia(id=provinciaid)
   #       provinciaope.getProvinciaId()
   #       for registro in data:
   #          dicDatos = {"id": registro[0], "nombre": registro[1], 'idProvincia': registro[2]}
   #          listaDatos.append(dicDatos)
   #       result = {'Message': f'Mostrando Comunas de {provinciaope.nombre}', 'Comunas': listaDatos}
   #       return result   
   #    except mysql.connector.Error as err:
   #       print(f"Ha ocurrido un error: {err}")
   #       return False


   def dic(self):
      diccionario = {'id': self.id, 'nombre': self.nombre}
      return diccionario



   def __str__(self):
      return str(self.id), self.nombre
