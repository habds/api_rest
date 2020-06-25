class Collector_app(): 
   def __init__(self,id = 0): 
      self.id = id
 
   def setId(self, id):
      self.id = id
 
   def getId(self):
      return self.id
 
   def __str__(self):
      return str(self.id)
