class TiendaTipo(): 
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
 
   def __str__(self):
      return str(self.id), str(self.codigo), str(self.descripcion)
