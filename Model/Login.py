from conexion2 import DataBaseConexion
import mysql.connector

class Login(): 
   def __init__(self,id = 0,username = '',password = '',idPersona = 0,idRol = 0): 
      self.id = id
      self.username = username
      self.password = password
      self.idPersona = idPersona
      self.idRol = idRol
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setUsername(self, username):
      self.username = username
 
   def setPassword(self, password):
      self.password = password
 
   def setIdpersona(self, idPersona):
      self.idPersona = idPersona
 
   def setIdrol(self, idRol):
      self.idRol = idRol
 
   def getId(self):
      return self.id
 
   def getUsername(self):
      return self.username
 
   def getPassword(self):
      return self.password
 
   def getIdpersona(self):
      return self.idPersona
 
   def getIdrol(self):
      return self.idRol
 
   def searchLogin(self):
      try:
         self.db.cursor.execute(f'select idUsuario, nombre_usuario, contrasena, idPersona, idRoles from Login where nombre_usuario="{self.username}" and contrasena="{self.password}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setUsername(f'{obj[1]}')
            self.setPassword(obj[2])
            self.setIdpersona(obj[3])
            self.setIdrol(obj[4])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def searchLoginById(self):
      try:
         self.db.cursor.execute(f'select idUsuario, nombre_usuario, contrasena, idPersona, idRoles from Login where idUsuario={self.id}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setUsername(f'{obj[1]}')
            self.setPassword(obj[2])
            self.setIdpersona(obj[3])
            self.setIdrol(obj[4])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def searchLoginByNombre(self):
      try:
         self.db.cursor.execute(f'select idUsuario, nombre_usuario, contrasena, idPersona, idRoles from Login where nombre_usuario={self.username}')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setUsername(f'{obj[1]}')
            self.setPassword(obj[2])
            self.setIdpersona(obj[3])
            self.setIdrol(obj[4])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def selectLogin(self):
      self.db.cursor.execute('select idUsuario, nombre_usuario, contrasena, idPersona, idRoles from Login')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []
      for registro in data:
         dicDatos = {"id": registro[0], "username": registro[1], 'password': registro[2], "idPersona": registro[3], 'idRol': registro[4]}
         listaDatos.append(dicDatos)
      result = listaDatos
      return result


   def insertLogin(self):
      try:
         self.db.cursor.execute(f'insert into Login(nombre_usuario, contrasena, idPersona, idRoles) values("{self.username}","{self.password}",{self.idPersona},{self.idRol})')
         self.db.cursor.execute("commit;")
         self.searchLogin()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateLogin(self):
      try:
         self.db.cursor.execute(f"update Login set nombre_usuario='{self.username}', contrasena='{self.password}', idPersona={self.idPersona}, idRoles={self.idRol} where idUsuario={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteLogin(self):
      try:
         self.db.cursor.execute(f"delete from Login where idUsuario='{self.id}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'username' : self.username, 'password' : self.password, 'idPersona' :self.idPersona, 'idRol' : self.idRol}
      return diccionario   

   def __str__(self):
      return str(self.id), str(self.username), str(self.password), str(self.idPersona), str(self.idRol)
