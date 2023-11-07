class Persona:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        self._edad=edad

    def __str__(self):#override -sobreescribir
        return f"persona: nombre: {self._nombre} edad:{self._edad}"

class  Empleado(Persona):#esta clase es hija de la clase persona
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self._sueldo=sueldo

    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.getter
    def sueldo(self,sueldo):
        self._sueldo=sueldo

    def __str__(self):
        return f"empleado: {self._sueldo} - {super().__str__()}"
empleado1=Empleado("ariel",40,75000)
print(empleado1._nombre)
print(empleado1._edad)
print(empleado1._sueldo)
#tarea encapsular los atributos y agregar los 
#metodos getter and setters 
#crear otro objeto, pasar los datos para nombre, edad, sueldo
#mostrar estos datos, luego modificar y mostrar
empleado2=Empleado('liliana',38,70000)
print(empleado2._nombre)
print(empleado2._edad)
empleado2.nombre="natalia"
empleado2._edad=35
empleado2._sueldo=75000
print(empleado2._nombre)
print(empleado2._edad)
print(empleado2._sueldo)
