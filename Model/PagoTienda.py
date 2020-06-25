import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class PagoTienda(): 
   def __init__(self,id = 0,idTienda = 0,idMetodoPago = 0): 
      self.id = id
      self.idTienda = idTienda
      self.idMetodoPago = idMetodoPago
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setIdtienda(self, idTienda):
      self.idTienda = idTienda
 
   def setIdmetodopago(self, idMetodoPago):
      self.idMetodoPago = idMetodoPago
 
   def getId(self):
      return self.id
 
   def getIdtienda(self):
      return self.idTienda
 
   def getIdmetodopago(self):
      return self.idMetodoPago

   def searchPagoTienda(self):
      try:
         self.db.cursor.execute(f'select idPago_Tienda, idTienda, idMetodo_Pago from Pago_Tienda where idPago_Tienda="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setIdtienda(f'{obj[1]}')
            self.setIdmetodopago(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectPagoTienda(self):
      self.db.cursor.execute('select idPago_Tienda, idTienda, idMetodo_Pago from Pago_Tienda')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Metodos de pago', 'Metodo de pago': listaDatos}
      return result


   def insertPagoTienda(self):
      try:
         self.db.cursor.execute(f'insert into Pago_Tienda(idTienda, idMetodo_Pago) values({self.idTienda}, {self.idMetodoPago})')
         self.db.cursor.execute("commit;")
         self.searchPagoTienda()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return False

   def updatePagoTienda(self):
      try:
         self.db.cursor.execute(f"update Pago_Tienda set idTienda={self.idTienda}, idMetodo_Pago={self.idMetodoPago} where idPago_Tienda={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deletePagoTienda(self):
      try:
         self.db.cursor.execute(f"delete from Pago_Tienda where idPago_Tienda='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False

   def dic(self):
      diccionario = {'idPago de tienda': self.id, 'id Tienda': self.idTienda, 'id Metodo Pago' : self.idMetodoPago}
      return diccionario
   
 
   def __str__(self):
      return str(self.id), str(self.idTienda), str(self.idMetodoPago)
