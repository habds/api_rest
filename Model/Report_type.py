import sys, os
sys.path.append(os.getcwd())
from conexion import DataBaseConexion
import mysql.connector

class Report_type(): 
   def __init__(self,id = 0,descripcion = '',area = '',area_code = ''): 
      self.id = id
      self.descripcion = descripcion
      self.area = area
      self.area_code = area_code
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setArea(self, area):
      self.area = area
 
   def setArea_code(self, area_code):
      self.area_code = area_code
 
   def getId(self):
      return self.id
 
   def getDescripcion(self):
      return self.descripcion
 
   def getArea(self):
      return self.area
 
   def getArea_code(self):
      return self.area_code
 
   def __str__(self):
      return str(self.id), str(self.descripcion), str(self.area), str(self.area_code)


   def getReportType(self):
      try:
         self.db.cursor.execute(f'select idReport_Type, desc, area, area_code from Report_Type where idReport_Type="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setArea(f'{obj[1]}')
            self.setArea_code(f'{obj[2]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def getReportTypes(self):
      self.db.cursor.execute('select idReport_Type, desc, area, area_code from Report_Type')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "descripcion": registro[1], 'area': registro[2], 'area_code': registro[3]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Report Types', 'Report Types': listaDatos}
      return result


   def setReportType(self):
      try:
         self.db.cursor.execute(f'insert into Report_Type(desc, area, area_code) values("{self.descripcion}", "{self.area}", "{self.area_code}")')
         self.db.cursor.execute("commit;")
         self.getSexo()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateReportType(self):
      try:
         self.db.cursor.execute(f"update Report_Type set desc='{self.descripcion}', area='{self.area}', area_code='{self.area_code}' where idReport_Type={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteReportType(self):
      try:
         self.db.cursor.execute(f"delete from Report_Type where idReport_Type='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {"id": self.id, "descripcion": self.descripcion, 'area': self.area, 'area_code': self.area_code}
      return diccionario