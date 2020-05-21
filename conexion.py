import psycopg2
#conexion = psycopg2.connect("dbname=dah4ovgnh5u7uj user=scpuhirqcifnzq password=ac1f425c77c31e67ae108b18f58baeb86b6a25e185b48382ef6f8876b1f5bcca port=5432")


# Ejecutamos una consulta


# Recorremos los resultados y los mostramos
#for nombre in cur.fetchall() :
#    print(nombre)


def select(query):
    conexion = psycopg2.connect(host="ec2-50-17-21-170.compute-1.amazonaws.com", database="dah4ovgnh5u7uj", user="scpuhirqcifnzq", password="ac1f425c77c31e67ae108b18f58baeb86b6a25e185b48382ef6f8876b1f5bcca")
    # Creamos el cursor con el objeto conexion  
    cur = conexion.cursor()
    respuesta=cur.execute( "query" )
    conexion.close()
    return respuesta

def coneccion(query):
    conexion = psycopg2.connect(host="ec2-50-17-21-170.compute-1.amazonaws.com", database="dah4ovgnh5u7uj", user="scpuhirqcifnzq", password="ac1f425c77c31e67ae108b18f58baeb86b6a25e185b48382ef6f8876b1f5bcca")
    
    return conexion
    
# Cerramos la conexión
