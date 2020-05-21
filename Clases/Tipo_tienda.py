class Tipo_tienda(): 
   def __init__(self,id = 0,nombre = '',direccion = '',email = '',telefono = ''): 
      self.id = id
      self.nombre = nombre
      self.direccion = direccion
      self.email = email
      self.telefono = telefono
 
   def setId(self, id):
      self.id = id
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setDireccion(self, direccion):
      self.direccion = direccion
 
   def setEmail(self, email):
      self.email = email
 
   def setTelefono(self, telefono):
      self.telefono = telefono
 
   def getId(self):
      return self.id
 
   def getNombre(self):
      return self.nombre
 
   def getDireccion(self):
      return self.direccion
 
   def getEmail(self):
      return self.email
 
   def getTelefono(self):
      return self.telefono
 
   def __str__(self):
      return str(self.id), str(self.nombre), str(self.direccion), str(self.email), str(self.telefono)
