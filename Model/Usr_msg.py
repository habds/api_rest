class USR_MSG(): 
   def __init__(self,idUSR_MSG = 0,nombre = '',descripcion = '',precio_anuncio = 0,estatus = '',Rate_Container = '',idRate_MSG = 0,idProducto = 0): 
      self.idUSR_MSG = idUSR_MSG
      self.nombre = nombre
      self.descripcion = descripcion
      self.precio_anuncio = precio_anuncio
      self.estatus = estatus
      self.Rate_Container = Rate_Container
      self.idRate_MSG = idRate_MSG
      self.idProducto = idProducto
 
   def setIdusr_msg(self, idUSR_MSG):
      self.idUSR_MSG = idUSR_MSG
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setPrecio_anuncio(self, precio_anuncio):
      self.precio_anuncio = precio_anuncio
 
   def setEstatus(self, estatus):
      self.estatus = estatus
 
   def setRate_container(self, Rate_Container):
      self.Rate_Container = Rate_Container
 
   def setIdrate_msg(self, idRate_MSG):
      self.idRate_MSG = idRate_MSG
 
   def setIdproducto(self, idProducto):
      self.idProducto = idProducto
 
   def getIdusr_msg(self):
      return self.idUSR_MSG
 
   def getNombre(self):
      return self.nombre
 
   def getDescripcion(self):
      return self.descripcion
 
   def getPrecio_anuncio(self):
      return self.precio_anuncio
 
   def getEstatus(self):
      return self.estatus
 
   def getRate_container(self):
      return self.Rate_Container
 
   def getIdrate_msg(self):
      return self.idRate_MSG
 
   def getIdproducto(self):
      return self.idProducto
 
   def __str__(self):
      return str(self.idUSR_MSG), str(self.nombre), str(self.descripcion), str(self.precio_anuncio), str(self.estatus), str(self.Rate_Container), str(self.idRate_MSG), str(self.idProducto)


   def getUsr_msg(self):
      try:
         self.db.cursor.execute(f'select idUSR_MSG, nombre, descripcion, precio_anuncio, estatus, Rate_Container, idRate_MSG, idProducto from USR_MSG where idUSR_MSG={self.idUsr_MSG}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setIdusr_msg(obj[0])
            self.setNombre(obj[1])
            self.setDescripcion(obj[3])
            self.setPrecio_anuncio(obj[4])
            self.setEstatus(obj[5])
            self.setRate_container(obj[6])
            self.setIdrate_msg(obj[7])
            self.setIdproducto(obj[8])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def getUsr_msgs(self):
      self.db.cursor.execute('select idUSR_MSG, nombre, descripcion, precio_anuncio, estatus, Rate_Container, idRate_MSG, idProducto from USR_MSG')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []

      for registro in data:
         dicDatos = {"id": registro[0], "nombre": registro[1], 'descripcion': registro[2], 'precio': registro[3], 'estatus':registro[4], 'Rate_Container': registro[5], 'idRate_MSG': registro[6], 'idProducto':registro[7]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Anuncio', 'Anuncios': listaDatos}
      return result

   def getUsr_msgByNombre(self):
      try:
         self.db.cursor.execute(f'select idUSR_MSG, nombre, descripcion, precio_anuncio, estatus, Rate_Container, idRate_MSG, idProducto from USR_MSG where nombre="{self.nombre}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setIdusr_msg(obj[0])
            self.setNombre(obj[1])
            self.setDescripcion(obj[3])
            self.setPrecio_anuncio(obj[4])
            self.setEstatus(obj[5])
            self.setRate_container(obj[6])
            self.setIdrate_msg(obj[7])
            self.setIdproducto(obj[8])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def setUsr_msg(self):
      try:
         self.db.cursor.execute(f'insert into USR_MSG(nombre, descripcion, precio_anuncio, estatus, Rate_Container, idRate_MSG, idProducto) values("{self.nombre}","{self.descripcion}", {self.precio_anuncio}, {self.estatus}, "{self.Rate_Container}", {self.idRate_MSG}, {self.idProducto})')
         self.db.cursor.execute("commit;")
         self.getUsr_msgbyNombre()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateUsr_msg(self):
      try:
         self.db.cursor.execute(f"update USR_MSG set nombre='{self.nombre}', descripcion='{self.descripcion}', precio_anuncio={self.precio_anuncio}, estatus={self.estatus}, Rate_Container='{self.Rate_Container}', idRate_MSG={self.idRate_MSG}, idProducto={self.idProducto} where idUSR_MSG={self.idUsr_MSG}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteUsr_msg(self):
      try:
         self.db.cursor.execute(f"delete from USR_MSG where idUSR_MSG={self.idUsr_MSG}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.idUSR_MSG, 'nombre': self.nombre, 'descripcion': self.descripcion, 'precio': self.precio_anuncio, 'estatus': self.estatus, 'Rate_Container': self.Rate_Container, 'idRate_MSG': self.idRate_MSG, 'idProducto': self.idProducto}
      return diccionario