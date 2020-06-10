from conexion2 import DataBaseConexion
import mysql.connector

class Persona(): 
   def __init__(self,id = 0,run = '',dv = '',nombres = '',a_paterno = '',a_materno = '',idGenero = 0,fono = '',fecha_n = '',email = '',idComuna = ''): 
      self.id = id
      self.run = run
      self.dv = dv
      self.nombres = nombres
      self.a_paterno = a_paterno
      self.a_materno = a_materno
      self.idGenero = idGenero
      self.fono = fono
      self.fecha_n = fecha_n
      self.email = email
      self.idComuna = idComuna
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
 
   def setFecha_n(self, fecha_n):
      self.fecha_n = fecha_n
 
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
 
   def getFecha_n(self):
      return self.fecha_n
 
   def getEmail(self):
      return self.email
 
   def getIdcomuna(self):
      return self.idComuna

   def searchPersona(self):
      try:
         self.db.cursor.execute(f'select id, run, dv, nombre, a_paterno, a_materno, idgenero, n_contacto, fecha_n, email, idcomuna from persona where run="{self.run}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setRun(f'{obj[1]}')
            self.setDv(obj[2])
            self.setNombres(obj[3])
            self.setA_paterno(obj[4])
            self.setA_materno(obj[5])
            self.setIdgenero(obj[6])
            self.setFono(obj[7])
            self.setFecha_n(obj[8])
            self.setEmail(obj[9])
            self.setIdcomuna(obj[10])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def searchPersonaById(self):
      try:
         self.db.cursor.execute(f'select id, run, dv, nombre, a_paterno, a_materno, idgenero, n_contacto, fecha_n, email, idcoomuna from persona where id="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setRun(f'{obj[1]}')
            self.setDv(obj[2])
            self.setNombres(obj[3])
            self.setA_paterno(obj[4])
            self.setA_materno(obj[5])
            self.setIdgenero(obj[6])
            self.setFono(obj[7])
            self.setFecha_n(obj[8])
            self.setEmail(obj[9])
            self.setIdcomuna(obj[10])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def selectPersonas(self):
      self.db.cursor.execute('select id, run, dv, nombre, a_paterno, a_materno, idgenero, n_contacto, fecha_n, email, idcomuna from persona')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []
      for registro in data:
         dicDatos = {"id": registro[0], "run": registro[1], 'dv': registro[2], "nombre": registro[3], 'a_paterno': registro[4]
                     , "a_materno": registro[5], 'idgenero': registro[6], "fono": registro[7], 'fecha_n': registro[8]
                     , "email": registro[9],'idcomuna': registro[10]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Personas', 'Personas': listaDatos}
      return result


   def insertPersona(self):
      try:
         self.db.cursor.execute(f'insert into persona(run, dv, nombre, a_paterno, a_materno, idgenero, n_contacto, fecha_n, email, idcomuna) values("{self.run}","{self.dv}","{self.nombres}","{self.a_paterno}","{self.a_materno}",{self.idGenero},"{self.fono}","{self.fecha_n}","{self.email}",{self.idComuna})')
         self.db.cursor.execute("commit;")
         self.searchPersona()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updatePersona(self):
      try:
         self.db.cursor.execute(f"update persona set run='{self.run}', dv='{self.dv}', nombre='{self.nombres}', a_paterno='{self.a_paterno}', a_materno='{self.a_materno}', idgenero={self.idGenero}, n_contacto='{self.fono}', fecha_n='{self.fecha_n}', email='{self.email}', idcomuna={self.idComuna} where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deletePersona(self):
      try:
         self.db.cursor.execute(f"delete from persona where run='{self.run}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'run' : self.run, 'dv' : self.dv, 'nombre' :self.nombres, 'a_paterno' : self.a_paterno, 'a_materno' : self.a_materno, 'idgenero' : self.idGenero, 'n_contacto' : self.fono, 'fecha_n' : self.fecha_n,'email' : self.email, 'idCiudad ' : self.idComuna}
      return diccionario   
 
   def __str__(self):
      return str(self.id), str(self.run), str(self.dv), str(self.nombres), str(self.a_paterno), str(self.a_materno), str(self.idGenero), str(self.fono), str(self.fecha_n), str(self.email), str(self.idComuna)
