class Report(): 
   def __init__(self,id = 0,descripcion = '',codigo = '', idReport_Type=0): 
      self.id = id
      self.descripcion = descripcion
      self.codigo = codigo
      self.idReport_Type = idReport_Type
 
   def setId(self, id):
      self.id = id
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setCodigo(self, codigo):
      self.codigo = codigo
 
   def getId(self):
      return self.id
 
   def getDescripcion(self):
      return self.descripcion
 
   def getCodigo(self):
      return self.codigo
 
   def __str__(self):
      return str(self.id), str(self.descripcion), str(self.codigo)


def getReport(self):
      try:
         self.db.cursor.execute(f'select idReport, desc, code, idReport_Type from Report where idReport="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setDescripcion(f'{obj[1]}')
            self.setCodigo(f'{obj[2]}')
            self.idReport_Type = obj[3]
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


def getReport(self):
   self.db.cursor.execute('select idReport, desc, code, idReport_Type from Report')
   data = self.db.cursor.fetchall()
   dicDatos = {}
   listaDatos = []

   for registro in data:
      dicDatos = {"id": registro[0], "descripcion": registro[1], 'codigo': registro[2], 'idReport_Type': registro[3]}
      listaDatos.append(dicDatos)
   result = {'Message': 'Mostrando Reportes', 'Reportes': listaDatos}
   return result


def setReport(self):
   try:
      self.db.cursor.execute(f'insert into Report(desc, code, idReport_Type) values("{self.descripcion}", "{self.codigo}", {self.idReport_Type})')
      self.db.cursor.execute("commit;")
      self.getSexo()
      return True
   except mysql.connector.Error as err:
      print("Ha ocurrido un error: {}".format(err))
      return  False

def updateReportType(self):
   try:
      self.db.cursor.execute(f"update Report_Type set desc='{self.descripcion}', code='{self.codigo}', idReport_Type='{self.idReport_Type}' where idReport_Type={self.id}")
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
   diccionario = {"id": self.id, "descripcion": self.descripcion, 'codigo': self.codigo, 'idReport_Type': self.idReport_Type}
   return diccionario
