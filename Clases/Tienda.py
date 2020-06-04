class Tienda(): 
   def __init__(self,id = 0,nombre = '',direccion = '',email = '',telefono = '',idCiudad = 0,idTipoTienda = 0): 
      self.id = id
      self.nombre = nombre
      self.direccion = direccion
      self.email = email
      self.telefono = telefono
      self.idCiudad = idCiudad
      self.idTipoTienda = idTipoTienda
 
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
 
   def setIdciudad(self, idCiudad):
      self.idCiudad = idCiudad
 
   def setIdtipotienda(self, idTipoTienda):
      self.idTipoTienda = idTipoTienda
 
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
 
   def getIdciudad(self):
      return self.idCiudad
 
   def getIdtipotienda(self):
      return self.idTipoTienda
 
   def __str__(self):
      return str(self.id), self.nombre, self.direccion, self.email, self.telefono, str(self.idCiudad), str(self.idTipoTienda)
