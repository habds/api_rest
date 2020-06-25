class Usr_msg(): 
   def __init__(self,id = 0,nombre = '',descripcion = '',precio_anuncioo = 0,estatus = '',rate_container = ''): 
      self.id = id
      self.nombre = nombre
      self.descripcion = descripcion
      self.precio_anuncioo = precio_anuncioo
      self.estatus = estatus
      self.rate_container = rate_container
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setPrecio_anuncioo(self, precio_anuncioo):
      self.precio_anuncioo = precio_anuncioo
 
   def setEstatus(self, estatus):
      self.estatus = estatus
 
   def setRate_container(self, rate_container):
      self.rate_container = rate_container
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getDescripcion(self):
      return self.descripcion
 
   def getPrecio_anuncioo(self):
      return self.precio_anuncioo
 
   def getEstatus(self):
      return self.estatus
 
   def getRate_container(self):
      return self.rate_container
 
   def __str__(self):
      return str(self.id), str(self.nombre), str(self.descripcion), str(self.precio_anuncioo), str(self.estatus), str(self.rate_container)
