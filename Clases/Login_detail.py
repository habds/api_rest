class Login_detail(): 
   def __init__(self,id = 0,id_lodded = False,f_ultimo_login = '',tiempo_log = ''): 
      self.id = id
      self.id_lodded = id_lodded
      self.f_ultimo_login = f_ultimo_login
      self.tiempo_log = tiempo_log
 
   def setId(self, id):
      self.id = id
 
   def setId_lodded(self, id_lodded):
      self.id_lodded = id_lodded
 
   def setF_ultimo_login(self, f_ultimo_login):
      self.f_ultimo_login = f_ultimo_login
 
   def setTiempo_log(self, tiempo_log):
      self.tiempo_log = tiempo_log
 
   def getId(self):
      return self.id
 
   def getId_lodded(self):
      return self.id_lodded
 
   def getF_ultimo_login(self):
      return self.f_ultimo_login
 
   def getTiempo_log(self):
      return self.tiempo_log
 
   def __str__(self):
      return str(self.id), str(self.id_lodded), str(self.f_ultimo_login), str(self.tiempo_log)
