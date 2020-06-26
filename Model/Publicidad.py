import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector
import datetime

class Publicidad(): 
   tabla = "Publicidad"
   def __init__(self,id = 0,f_inicio = datetime.date,f_termino = datetime.date,compania = ''): 
      self.id = id
      self.f_inicio = f_inicio
      self.f_termino = f_termino
      self.compania = compania
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setF_inicio(self, f_inicio):
      self.f_inicio = f_inicio
 
   def setF_termino(self, f_termino):
      self.f_termino = f_termino
 
   def setCompania(self, compania):
      self.compania = compania
 
   def getId(self):
      return self.id
 
   def getF_inicio(self):
      return self.f_inicio
 
   def getF_termino(self):
      return self.f_termino
 
   def getCompania(self):
      return self.compania
 
   def search(self):
      try:
         self.db.cursor.execute(f'select idPublicidad, inicio, termino, nombre_empresa from {self.tabla} where idPublicidad={self.id}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setF_inicio(f'{obj[1]}')
            self.setF_termino(f'{obj[2]}')
            self.setCompania(f'{obj[3]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def select(self):
      self.db.cursor.execute(f'select idPublicidad, inicio, termino, nombre_empresa from {self.tabla}')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "Fecha Inicio": registro[1], "Fecha Termino" : registro[2], "Nombre de Empresa" : registro[3]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando publicidad', 'Publicidad': listaDatos}
      return result


   def insert(self):
      try:
         self.db.cursor.execute(f"insert into {self.tabla}(inicio, termino, nombre_empresa) values('{self.f_inicio}', '{self.f_termino}', {self.compania})")
         self.db.cursor.execute("commit;")
         self.search()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return False

   def update(self):
      try:
         self.db.cursor.execute(f"update {self.tabla} set inicio={self.f_inicio}, termino={self.f_termino}, nombre_empresa={self.compania} where idPublicidad={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def delete(self):
      try:
         self.db.cursor.execute(f"delete from {self.tabla} where idPublicidad='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False

   def dic(self):
      diccionario = {'IdPublicidad': self.id, 'Fecha de Inicio' : self.f_inicio, 'Fecha de Termino': self.f_termino, 'Nombre de empresa' : self.compania}
      return diccionario  

   def __str__(self):
      return str(self.id), str(self.f_inicio), str(self.f_termino), str(self.compania)
