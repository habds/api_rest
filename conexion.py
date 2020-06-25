import sys, os
sys.path.append(os.getcwd())
import mysql.connector

class DataBaseConexion():
    def __init__(self):
        try:
            self.db = mysql.connector.connect(host='201.148.104.16', port=3306, user='rollback_test', password='Ayrton2020', database='rollback_BApp')
            self.cursor = self.db.cursor()
            print('Conexion Exitosa')
        except mysql.connector.Error as err:
            print("Ha ocurrido un error: {}".format(err))
        
    def getData(self, query):
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()    