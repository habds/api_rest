class Map_setting(): 
   def __init__(self,id = 0,estatus = ''): 
      self.id = id
      self.estatus = estatus
 
   def setId(self, id):
      self.id = id
 
   def setEstatus(self, estatus):
      self.estatus = estatus
 
   def getId(self):
      return self.id
 
   def getEstatus(self):
      return self.estatus
 
   def __str__(self):
      return str(self.id), str(self.estatus)
