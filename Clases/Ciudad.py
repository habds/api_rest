class Ciudad(): 
   def __init__(self,id = 0,nombre = ''): 
      self.id = id
      self.nombre = nombre
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def __str__(self):
      return str(self.id), str(self.nombre)
