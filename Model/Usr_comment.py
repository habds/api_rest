class Usr_comment(): 
   def __init__(self,id = 0,descripcion = '',estatus = '', idUSR_MSG=0): 
      self.id = id
      self.descripcion = descripcion
      self.estatus = estatus
      self.idUSR_MSG = idUSR_MSG
 
   def setId(self, id):
      self.id = id
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setEstatus(self, estatus):
      self.estatus = estatus
 
   def getId(self):
      return self.id
 
   def getDescripcion(self):
      return self.descripcion
 
   def getEstatus(self):
      return self.estatus
 
   def __str__(self):
      return str(self.id), str(self.descripcion), str(self.estatus)

   def getUSR_Comentario(self):
      try:
         self.db.cursor.execute(f'select idUSR_Comentario, descripcion, estatus, idUSR_MSG from USR_Comentario where idUSR_Comentario={self.id}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setDescripcion(f'{obj[1]}')
            self.setEstatus(f'{obj[2]}')

            self.setNombre(f'{obj[1]}')
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def getUSR_Comentarios(self):
      self.db.cursor.execute('select idUSR_Comentario, descripcion, estatus, idUSR_MSG from USR_Comentario')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "descripcion": registro[1], 'estatus': registro[2], 'idUSR_MSG': registro[3]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando USR_MSG', 'USR_MSG': listaDatos}
      return result


   def setUSR_Comentario(self):
      try:
         self.db.cursor.execute(f'insert into USR_Comentario(descripcion, estatus, idUSR_MSG) values("{self.descripcion}", "{self.estatus}", {self.idUSR_MSG})')
         self.db.cursor.execute("commit;")
         self.getRate_msg()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateUSR_Comentario(self):
      try:
         self.db.cursor.execute(f"update USR_Comentario set descripcion='{self.descripcion}', estatus='{self.estatus}', idUSR_MSG={self.idUSR_MSG} where idUSR_Comentario={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteUSR_Comentario(self):
      try:
         self.db.cursor.execute(f"delete from USR_Comentario where idUSR_Comentario='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'descripcion': self.descripcion, 'estatus': self.estatus, 'idUSR_MSG': self.idUSR_MSG}
      return diccionario
