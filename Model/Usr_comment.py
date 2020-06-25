class Usr_comment(): 
   def __init__(self,id = 0,descripcion = '',estatus = ''): 
      self.id = id
      self.descripcion = descripcion
      self.estatus = estatus
 
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
