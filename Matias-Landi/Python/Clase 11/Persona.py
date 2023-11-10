class Persona:  # Hereda de la clase Object.
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    # Creación del método Setter.
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Método dunder str
    def __str__(self): # Override = sobre escribír.
        return f"Persona [ Nombre: {self._nombre}, Edad: {self._edad} ]"


class Empleado(Persona):  # Hereda de la clase Persona.
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Importamos los atributos de la clase padre.
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado [ Sueldo: {self._sueldo} ] {super().__str__()}"


empleado1 = Empleado("Ariel", 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
# Tarea: encapsular los atributos y agregar los métodos getters and setters
# Crear un objeto, pasar los datos para nombre, edad y sueldo.
# Mostrar estos datos, luego modificar y mostrar nuevamente.

empleado2 = Empleado("Liliana", 33, 70000)

print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = "Natalia"
empleado2.edad = 35
empleado2.sueldo = 75000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)