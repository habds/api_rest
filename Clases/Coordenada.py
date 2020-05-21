class Coordenada(): 
   def __init__(self,id = 0,longitud = '',latitud = '',estatus = ''): 
      self.id = id
      self.longitud = longitud
      self.latitud = latitud
      self.estatus = estatus
 
   def setId(self, id):
      self.id = id
 
   def setLongitud(self, longitud):
      self.longitud = longitud
 
   def setLatitud(self, latitud):
      self.latitud = latitud
 
   def setEstatus(self, estatus):
      self.estatus = estatus
 
   def getId(self):
      return self.id
 
   def getLongitud(self):
      return self.longitud
 
   def getLatitud(self):
      return self.latitud
 
   def getEstatus(self):
      return self.estatus
 
   def __str__(self):
      return str(self.id), str(self.longitud), str(self.latitud), str(self.estatus)
