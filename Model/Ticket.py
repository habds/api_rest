class Ticket(): 
   def __init__(self,id = 0,ticket_abierto = False,area_code = ''): 
      self.id = id
      self.ticket_abierto = ticket_abierto
      self.area_code = area_code
 
   def setId(self, id):
      self.id = id
 
   def setTicket_abierto(self, ticket_abierto):
      self.ticket_abierto = ticket_abierto
 
   def setArea_code(self, area_code):
      self.area_code = area_code
 
   def getId(self):
      return self.id
 
   def getTicket_abierto(self):
      return self.ticket_abierto
 
   def getArea_code(self):
      return self.area_code
 
   def __str__(self):
      return str(self.id), str(self.ticket_abierto), str(self.area_code)
