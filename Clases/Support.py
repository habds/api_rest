class Support(): 
   def __init__(self,id = 0,estatus = '',codigo = ''): 
      self.id = id
      self.estatus = estatus
      self.codigo = codigo
 
   def setId(self, id):
      self.id = id
 
   def setEstatus(self, estatus):
      self.estatus = estatus
 
   def setCodigo(self, codigo):
      self.codigo = codigo
 
   def getId(self):
      return self.id
 
   def getEstatus(self):
      return self.estatus
 
   def getCodigo(self):
      return self.codigo
 
   def __str__(self):
      return str(self.id), str(self.estatus), str(self.codigo)
