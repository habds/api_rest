class Aviso_publicitario(): 
   def __init__(self,id = 0,f_inicio = '',f_termino = '',compania = ''): 
      self.id = id
      self.f_inicio = f_inicio
      self.f_termino = f_termino
      self.compania = compania
 
   def setId(self, id):
      self.id = id
 
   def setF_inicio(self, f_inicio):
      self.f_inicio = f_inicio
 
   def setF_termino(self, f_termino):
      self.f_termino = f_termino
 
   def setCompania(self, compania):
      self.compania = compania
 
   def getId(self):
      return self.id
 
   def getF_inicio(self):
      return self.f_inicio
 
   def getF_termino(self):
      return self.f_termino
 
   def getCompania(self):
      return self.compania
 
   def __str__(self):
      return str(self.id), str(self.f_inicio), str(self.f_termino), str(self.compania)
