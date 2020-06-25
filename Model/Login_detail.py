from conexion2 import DataBaseConexion
import mysql.connector

class Login_detail(): 
   def __init__(self,id = 0,id_logged = False,f_ultimo_login = '',tiempo_log = ''): 
      self.id = id
      self.id_logged = id_logged
      self.f_ultimo_login = f_ultimo_login
      self.tiempo_log = tiempo_log
      self.db = DataBaseConexion()
 
   def setId(self, id):
      self.id = id
 
   def setId_logged(self, id_logged):
      self.id_logged = id_logged
 
   def setF_ultimo_login(self, f_ultimo_login):
      self.f_ultimo_login = f_ultimo_login
 
   def setTiempo_log(self, tiempo_log):
      self.tiempo_log = tiempo_log
 
   def getId(self):
      return self.id
 
   def getId_logged(self):
      return self.id_logged
 
   def getF_ultimo_login(self):
      return self.f_ultimo_login
 
   def getTiempo_log(self):
      return self.tiempo_log

   def searchLogin_detail(self):
      try:
         self.db.cursor.execute(f'select id, id_logged, fecha_last_log, tiempo_logg from login_detail where id_logged="{self.id_logged}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setId_logged(f'{obj[1]}')
            self.setF_ultimo_login(obj[2])
            self.setTiempo_log(obj[3])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def searchLogin_detailById(self):
      try:
         self.db.cursor.execute(f'select id, id_logged, fecha_last_log, tiempo_logg from login_detail where id="{self.id}"')
         obj = self.db.cursor.fetchone()
         if obj != None:
            self.setId(f'{obj[0]}')
            self.setId_logged(f'{obj[1]}')
            self.setF_ultimo_login(obj[2])
            self.setTiempo_log(obj[3])
            return True
      except mysql.connector.Error as err:
         print(err)
         return False


   def selectLogin_detail(self):
      self.db.cursor.execute('select id, id_logged, fecha_last_log, tiempo_logg from login_detail')
      data = self.db.cursor.fetchall()
      dicDatos = {}
      listaDatos = []
      for registro in data:
         dicDatos = {"id": registro[0], "id_logged": registro[1], 'fecha_last_log': registro[2], 'tiempo_logg': registro[3]}
         listaDatos.append(dicDatos)
      result = {'Message': 'Mostrando Roles', 'Roles': listaDatos}
      return result


   def insertLogin_detail(self):
      try:
         self.db.cursor.execute(f'insert into login_detail(id_logged, fecha_last_log, tiempo_log) values("{self.id_logged}",{self.f_ultimo_login},{self.tiempo_log})')
         self.db.cursor.execute("commit;")
         self.searchLogin_detail()
         return True
      except mysql.connector.Error as err:
         print("Ha ocurrido un error: {}".format(err))
         return  False

   def updateLogin_detail(self):
      try:
         self.db.cursor.execute(f"update login_detail set id_logged='{self.id_logged}', fecha_last_log={self.f_ultimo_login}, tiempo_log={self.tiempo_log} where id={self.id}")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(err)
         return False

   def deleteLogin_detail(self):
      try:
         self.db.cursor.execute(f"delete from login_detail where id_logged='{self.id_logged}'")
         self.db.cursor.execute("commit;")
         return True
      except mysql.connector.Error as err:
         print(f"Ha ocurrido un error: {err}")
         return False


   def dic(self):
      diccionario = {'id': self.id, 'id_logged': self.id_logged, 'f_ultimo_login': self.f_ultimo_login, 'tiempo_log' : self.tiempo_log}
      return diccionario
 
   def __str__(self):
      return str(self.id), str(self.id_logged), str(self.f_ultimo_login), str(self.tiempo_log)
