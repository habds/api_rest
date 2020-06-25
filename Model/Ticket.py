import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class Ticket(): 
   tabla = "Ticket"
   def __init__(self,id = 0, ticket_abierto = "", estado = ""): 
      self.id = id
      self.ticket_abierto = ticket_abierto
      self.estado = estado
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setTicket_abierto(self, ticket_abierto):
      if len(ticket_abierto) < 46:
         self.ticket_abierto = ticket_abierto
 
   def setEstado(self, estado):
      if len(estado) < 46:
         self.estado = estado
 
   def getId(self):
      return self.id
 
   def getTicket_abierto(self):
      return self.ticket_abierto
 
   def getEstado(self):
      return self.estado
 
   def searchTicket(self):
      try:
         self.db.cursor.execute(f'select idTicket, ticket_abierto, estado from {self.tabla} where idTicket="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setTicket_abierto(f'{obj[1]}')
            self.setEstado(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def selectTicket(self):
      self.db.cursor.execute(f'select idTicket, ticket_abierto, estado from {self.tabla}')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "ticket abierto": registro[1], "estado" : registro[2]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Tickets', 'Tickets': listaDatos}
      return result


   def insertTicket(self):
      try:
         self.db.cursor.execute(f'insert into {self.tabla}(ticket_abierto, estado) values({self.ticket_abierto}, {self.estado})')
         self.db.cursor.execute("commit;")
         self.searchTicket()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return False

   def updateTicket(self):
      try:
         self.db.cursor.execute(f"update {self.tabla} set ticket_abierto='{self.ticket_abierto}', estado='{self.estado}' where idTicket={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteTicket(self):
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
      return str(self.id), self.ticket_abierto, self.estado
