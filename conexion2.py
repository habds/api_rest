import mysql.connector

class DataBaseConexion():
    def __init__(self):
        try:
            self.db = mysql.connector.connect(host='localhost', port=3306, user='root', password='12345', database='baratappdb')
            self.cursor = self.db.cursor()
            print('Conexion Exitosa')
        except mysql.connector.Error as err:
            print("Ha ocurrido un error: {}".format(err))
        
    def getData(self, query):
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()