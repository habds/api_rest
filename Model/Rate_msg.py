class Rate_msg(): 
   def __init__(self,id = 0,codigo = '',descripcion = ''): 
      self.id = id
      self.codigo = codigo
      self.descripcion = descripcion
 
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


   def getRate_msg(self):
      try:
         self.db.cursor.execute(f'select idRate_MSG, desc from Rate_MSG where idRate_MSG={self.id}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def getRate_msgs(self):
      self.db.cursor.execute('select idRate_MSG, desc from Rate_MSG')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "descripcion": registro[1]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Rate_MSG', 'Rate_MSG': listaDatos}
      return result


   def setRate_MSG(self):
      try:
         self.db.cursor.execute(f'insert into Rate_MSG(desc) values("{self.descripcion}")')
         self.db.cursor.execute("commit;")
         self.getRate_msg()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateRate_msg(self):
      try:
         self.db.cursor.execute(f"update Rate_MSG set desc='{self.descripcion}' where idRate_MSG={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteRate_msg(self):
      try:
         self.db.cursor.execute(f"delete from Rate_MSG where idRate_MSG='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'descripcion': self.descripcion}
      return diccionario
 
   def __str__(self):
      return str(self.id), str(self.descripcion)
