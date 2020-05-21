class Producto(): 
   def __init__(self,id = 0,nombre = '',descripcion = '',precio = ''): 
      self.id = id
      self.nombre = nombre
      self.descripcion = descripcion
      self.precio = precio
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setPrecio(self, precio):
      self.precio = precio
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getDescripcion(self):
      return self.descripcion
 
   def getPrecio(self):
      return self.precio
 
   def __str__(self):
      return str(self.id), str(self.nombre), str(self.descripcion), str(self.precio)
