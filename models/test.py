from persona import Persona

persona =Persona()
# persona.__init__("matias",0)
# persona.nombre="matias"
# persona.edad=0

persona.setNombre("matias")
persona.setEdad(0)

print (persona.__str__())