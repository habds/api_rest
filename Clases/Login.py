class Login(): 
   def __init__(self,id = 0,username = '',password = '',nombre = ''): 
      self.id = id
      self.username = username
      self.password = password
      self.nombre = nombre
 
   def setId(self, id):
      self.id = id
 
   def setUsername(self, username):
      self.username = username
 
   def setPassword(self, password):
      self.password = password
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def getId(self):
      return self.id
 
   def getUsername(self):
      return self.username
 
   def getPassword(self):
      return self.password
 
   def getNombre(self):
      return self.nombre
 
   def __str__(self):
      return str(self.id), str(self.username), str(self.password), str(self.nombre)
