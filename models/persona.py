class Persona():
    nombre = ""
    edad = 0

    def __init__(self, nombre="", edad=0):
        self.nombre=nombre
        self.edad=edad

    def setNombre(self,nombre):
        if len(nombre)>5:
            self.nombre=nombre
        
    def getNombre(self):
        return self.nombre

    def setEdad(self,edad):
        if edad>10:
            self.edad=edad

    def getEdad(self):
        return str(self.edad) 

    def __str__(self):
        return self.getNombre()+" "+self.getEdad()












