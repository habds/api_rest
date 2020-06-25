import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class Support(): 
   tabla = "Support"
   def __init__(self,id = 0,estatus = "",codigo = "", idTicket = 0): 
      self.id = id
      self.estatus = estatus
      self.codigo = codigo
      self.idTicket = idTicket
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setEstatus(self, estatus):
      if len(estatus)< 46:
         self.estatus = estatus
 
   def setCodigo(self, codigo):
      if len(codigo) < 46:
         self.codigo = codigo

   def setIdTicket(self, idTicket):
      self.idTicket = idTicket
 
   def getId(self):
      return self.id
 
   def getEstatus(self):
      return self.estatus
 
   def getCodigo(self):
      return self.codigo

   def getIdTicket(self):
      return self.idTicket

   def searchSup(self):
      try:
         self.db.cursor.execute(f'select idSupport, status, code, idTicket from {self.tabla} where idTicket={self.id}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setEstatus(f'{obj[1]}')
            self.setCodigo(f'{obj[2]}')
            self.setCodigo(f'{obj[3]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectSup(self):
      self.db.cursor.execute(f'select idSupport, status, code, idTicket from {self.tabla}')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "estatus": registro[1], "codigo" : registro[2], "idTicket" : registro[3]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Support', 'Support': listaDatos}
      return result


   def insertSup(self):
      try:
         self.db.cursor.execute(f"insert into {self.tabla}(status, code, idTicket) values('{self.estatus}', '{self.codigo}', {self.idTicket})")
         self.db.cursor.execute("commit;")
         self.searchSup()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return False

   def updateSup(self):
      try:
         self.db.cursor.execute(f"update {self.tabla} set status='{self.estatus}', code='{self.codigo}', idTicket={self.idTicket} where idSupport={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteSup(self):
      try:
         self.db.cursor.execute(f"delete from {self.tabla} where idTicket='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False

   def dic(self):
      diccionario = {'idTicket': self.id, 'Ticket Abierto': self.ticket_abierto, 'Estado' : self.estado}
      return diccionario   
 
   def __str__(self):
      return str(self.id), str(self.estatus), str(self.codigo)
