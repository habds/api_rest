from conexion2 import DataBaseConexion
import mysql.connector

class Persona(): 
   def __init__(self,id = 0,run = '',dv = '',nombres = '',a_paterno = '',a_materno = '',correo = '',fono = '', fono2 = '',fono3 = '',idComuna = '', idGenero = 0): 
      self.id = id
      self.run = run
      self.dv = dv
      self.nombres = nombres
      self.a_paterno = a_paterno
      self.a_materno = a_materno
      self.correo = correo
      self.fono = fono
      self.fono2 = fono2
      self.fono3 = fono3
      self.idComuna = idComuna
      self.idGenero = idGenero
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setRun(self, run):
      self.run = run
 
   def setDv(self, dv):
      self.dv = dv
 
   def setNombres(self, nombres):
      self.nombres = nombres
 
   def setA_paterno(self, a_paterno):
      self.a_paterno = a_paterno
 
   def setA_materno(self, a_materno):
      self.a_materno = a_materno
 
   def setIdgenero(self, idGenero):
      self.idGenero = idGenero
 
   def setFono(self, fono):
      self.fono = fono
   
   def setFono2(self, fono2):
      self.fono2 = fono2
   
   def setFono3(self,fono3):
      self.fono3 = fono3
 
   def setEmail(self, email):
      self.email = email
 
   def setIdcomuna(self, idComuna):
      self.idComuna = idComuna
 
   def getId(self):
      return self.id
 
   def getRun(self):
      return self.run
 
   def getDv(self):
      return self.dv
 
   def getNombres(self):
      return self.nombres
 
   def getA_paterno(self):
      return self.a_paterno
 
   def getA_materno(self):
      return self.a_materno
 
   def getIdgenero(self):
      return self.idGenero
 
   def getFono(self):
      return self.fono
 
 
   def getEmail(self):
      return self.email
 
   def getIdcomuna(self):
      return self.idComuna

   def searchPersona(self):
      try:
         self.db.cursor.execute(f'select idPersona, run, dv, nombres, apellido_paterno, apellido_materno, correo, telefono, telefono2, telefono3, idCiudad, idGenero  from Persona where run="{self.run}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setRun(f'{obj[1]}')
            self.setDv(obj[2])
            self.setNombres(obj[3])
            self.setA_paterno(obj[4])
            self.setA_materno(obj[5])
            self.setEmail(obj[6])
            self.setFono(obj[7])
            self.setFono2(obj[8])
            self.setFono3(obj[9])
            self.setIdcomuna(obj[10])
            self.setIdgenero(obj[11])
            
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def searchPersonaById(self):
      try:
         self.db.cursor.execute(f'select idPersona, run, dv, nombres, apellido_paterno, apellido_materno, correo, telefono, telefono2, telefono3, idCiudad, idGenero  from Persona where idPersona="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setRun(f'{obj[1]}')
            self.setDv(obj[2])
            self.setNombres(obj[3])
            self.setA_paterno(obj[4])
            self.setA_materno(obj[5])
            self.setEmail(obj[6])
            self.setFono(obj[7])
            self.setFono2(obj[8])
            self.setFono3(obj[9])
            self.setIdcomuna(obj[10])
            self.setIdgenero(obj[11])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def selectPersonas(self):
      self.db.cursor.execute('select idPersona, run, dv, nombres, apellido_paterno, apellido_materno, correo, telefono, telefono2, telefono3, idCiudad, idGenero from Persona')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []
      for registro in data:
         dicDatos = {"id": registro[0], "run": registro[1], 'dv': registro[2], "nombres": registro[3], 'a_paterno': registro[4]
                     , "a_materno": registro[5], 'correo': registro[6], "fono": registro[7], 'fono2': registro[8]
                     , "fono3": registro[9],'idcomuna': registro[10], 'idGenero': registro[11]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Personas', 'Personas': listaDatos}
      return result


   def insertPersona(self):
      try:
         self.db.cursor.execute(f'insert into Persona(run, dv, nombres, apellido_paterno, apellido_materno, correo, telefono, telefono2, telefono3, idCiudad, idGenero) values("{self.run}","{self.dv}","{self.nombres}","{self.a_paterno}","{self.a_materno}","{self.correo}",{self.fono},{self.fono2},{self.fono3},{self.idComuna},{self.idGenero})')
         self.db.cursor.execute("commit;")
         self.searchPersona()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updatePersona(self):
      try:
         self.db.cursor.execute(f"update Persona set run='{self.run}', dv='{self.dv}', nombres='{self.nombres}', apellido_paterno='{self.a_paterno}', apellido_materno='{self.a_materno}', email='{self.correo}', telefono={self.fono}, telefono2={self.fono2}, telefono3={self.fono3}, email='{self.email}', idcomuna={self.idComuna} where idPersona={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deletePersona(self):
      try:
         self.db.cursor.execute(f"delete from Persona where run='{self.run}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'run' : self.run, 'dv' : self.dv, 'nombre' :self.nombres, 'a_paterno' : self.a_paterno, 'a_materno' : self.a_materno, 'correo' : self.correo, 'fono' : self.fono, 'fono2' : self.fono2, 'fono3' : self.fono3, 'idComuna' : self.idComuna,'idGenero' : self.idGenero}
      return diccionario   
 
   def __str__(self):
      return str(self.id), str(self.run), str(self.dv), str(self.nombres), str(self.a_paterno), str(self.a_materno), str(self.correo), str(self.fono),str(self.fono2),str(self.fon3), str(self.idComuna), str(self.idGenero)
