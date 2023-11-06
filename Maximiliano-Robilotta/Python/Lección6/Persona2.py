class Persona2:
    def __init__(self, nombre, apellido, edad):  # Está encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  # Decorador
    def nombre(self):  # Método Getter: Obtener los atributos de una clase
        print("Estamos usando el método get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter: Modificar los atributos de una clase
        print("Estamos usando el método set")
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

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")


if __name__ == "__main__":
    persona1 = Persona2("Ariel", "Betancud", 41)
    print(persona1.nombre)  # Llamamos al método getter
    persona1.nombre = "Juan Pedro"  # Llamamos al método setter
    print(persona1.nombre)
    print(persona1.mostrar_detalles())  # Llamamos al método mostrar_detalles
    # Atributo read-only sería la edad porque no tiene el método set
    print(persona1.edad)
    # Tarea crear tres objetos más utilizando los métodos getter and setter
    # para modificar y mostrar los cambios con el método mostrar_detalles

    # Objeto número 1 de la tarea
    persona2 = Persona2("Angel", "Frias", 25)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = "Matias"
    persona2.apellido = "Bustamante"
    persona2.edad = "19"
    print(persona2.mostrar_detalles())

    # Objeto número 2 de la tarea
    persona3 = Persona2("Mirko", "Cascon", 33)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = "Laureano"
    persona3.apellido = "Ramos"
    persona3.edad = "43"
    print(persona3.mostrar_detalles())

    # Objeto número 3 de la tarea
    persona4 = Persona2("Joaquin", "Armani", 25)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = "Agustin"
    persona4.apellido = "Romero"
    persona4.edad = "26"
    print(persona4.mostrar_detalles())

    print(__name__)
