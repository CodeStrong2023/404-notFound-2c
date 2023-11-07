class Persona2:
    def __init__(self, nombre, apellido, edad): # Está encapsulado.
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrarDetalle(self):
        print(f"Los datos a mostrar son: {self._nombre}, {self._apellido}, {self._edad}")

    # Creación del método Getter.
    @property # decorador
    def nombre(self):
        return self._nombre

    # Creación del método Setter.
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Creamos el destructor de objetos.
    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

if (__name__ == "__main__"):
    persona1 = Persona2("Gonzalo", "Balmaceda", 20)
    print(persona1.nombre) # Llamamos al método getter.
    persona1.nombre = "Nicolas" # Llamamos al método setter.
    persona1.mostrarDetalle() # Llamamos al método mostrarDetalle.

    # Es un atributo read-only (solo lectura porque no tiene el método set)
    #print(persona1.edad)

    print("\n")
    # Creamos tres objetos más.
    persona2 = Persona2("Luci", "Fer", 19)
    persona2.nombre = "Luciano"
    persona2.apellido = "Ferreyra"
    persona2.edad = 21
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.mostrarDetalle()

    print("\n")
    persona3 = Persona2("Dari", "Flor", 40)
    persona3.nombre = "Dario"
    persona3.apellido = "Flores"
    persona3.edad = 45
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.mostrarDetalle()

    print("\n")
    persona4 = Persona2("Bri", "Lunares", 24)
    persona4.nombre = "Brian"
    persona4.apellido = "Luna"
    persona4.edad = 21
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.mostrarDetalle()

    print(__name__)