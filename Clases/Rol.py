class Rol(): 
   def __init__(self,id = 0,nombre = '',codigo = ''): 
      self.id = id
      self.nombre = nombre
      self.codigo = codigo
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setCodigo(self, codigo):
      self.codigo = codigo
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getCodigo(self):
      return self.codigo
 
   def __str__(self):
      return str(self.id), str(self.nombre), str(self.codigo)
