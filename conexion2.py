import sys, os
sys.path.append(os.getcwd())
import mysql.connector

class DataBaseConexion():
    def __init__(self):
        try:
            self.db = mysql.connector.connect(host='198.37.123.229', port=3306, user='electroa_sudo', password='quesocaliente', database='electroa_api')
            self.cursor = self.db.cursor()
            print('Conexion Exitosa')
        except mysql.connector.Error as err:
            print("Ha ocurrido un error: {}".format(err))
        
    def getData(self, query):
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()    