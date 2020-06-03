class Persona(): 
   def __init__(self,id = 0,run = '',dv = '',nombre = '',a_paterno = '',a_materno = '',genero = 0,num_fono = '',f_nac = '',email = '',idCiudad = 0): 
      self.id = id
      self.run = run
      self.dv = dv
      self.nombre = nombre
      self.a_paterno = a_paterno
      self.a_materno = a_materno
      self.genero = genero
      self.num_fono = num_fono
      self.f_nac = f_nac
      self.email = email
      self.idCiudad = idCiudad
 
   def setId(self, id):
      self.id = id
 
   def setRun(self, run):
      self.run = run
 
   def setDv(self, dv):
      self.dv = dv
 
   def setNombre(self, nombre):
      self.nombre = nombre
 
   def setA_paterno(self, a_paterno):
      self.a_paterno = a_paterno
 
   def setA_materno(self, a_materno):
      self.a_materno = a_materno
 
   def setGenero(self, genero):
      self.genero = genero
 
   def setNum_fono(self, num_fono):
      self.num_fono = num_fono
 
   def setF_nac(self, f_nac):
      self.f_nac = f_nac
 
   def setEmail(self, email):
      self.email = email
 
   def setIdciudad(self, idCiudad):
      self.idCiudad = idCiudad
 
   def getId(self):
      return self.id
 
   def getRun(self):
      return self.run
 
   def getDv(self):
      return self.dv
 
   def getNombre(self):
      return self.nombre
 
   def getA_paterno(self):
      return self.a_paterno
 
   def getA_materno(self):
      return self.a_materno
 
   def getGenero(self):
      return self.genero
 
   def getNum_fono(self):
      return self.num_fono
 
   def getF_nac(self):
      return self.f_nac
 
   def getEmail(self):
      return self.email
 
   def getIdciudad(self):
      return self.idCiudad
 
   def __str__(self):
      return str(self.id), str(self.run), str(self.dv), str(self.nombre), str(self.a_paterno), str(self.a_materno), str(self.genero), str(self.num_fono), str(self.f_nac), str(self.email), str(self.idCiudad)
