class Report(): 
   def __init__(self,id = 0,descripcion = '',codigo = ''): 
      self.id = id
      self.descripcion = descripcion
      self.codigo = codigo
 
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
