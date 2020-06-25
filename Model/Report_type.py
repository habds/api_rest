class Report_type(): 
   def __init__(self,id = 0,descripcion = '',area = '',area_code = ''): 
      self.id = id
      self.descripcion = descripcion
      self.area = area
      self.area_code = area_code
 
   def setId(self, id):
      self.id = id
 
   def setDescripcion(self, descripcion):
      self.descripcion = descripcion
 
   def setArea(self, area):
      self.area = area
 
   def setArea_code(self, area_code):
      self.area_code = area_code
 
   def getId(self):
      return self.id
 
   def getDescripcion(self):
      return self.descripcion
 
   def getArea(self):
      return self.area
 
   def getArea_code(self):
      return self.area_code
 
   def __str__(self):
      return str(self.id), str(self.descripcion), str(self.area), str(self.area_code)
