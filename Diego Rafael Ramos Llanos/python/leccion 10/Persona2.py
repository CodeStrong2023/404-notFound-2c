class Persona2:
    def __init__(self, nombre, apellido, edad):  # Está encapsulado.
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrarDetalle(self):
        print(f"Los datos a mostrar son: {self._nombre}, {self._apellido}, {self._edad}")

    @property  # decorador
    def nombre(self):  # metodo getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Creación del método Setter.
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


if (__name__ == "__main__"):
    persona1 = Persona2("Ariel", "Betancud", 41)
    print(persona1.nombre)  # Llamamos al método getter.
    persona1.nombre = "juan pedro"  # Llamamos al método setter.
    persona1.mostrarDetalle()  # Llamamos al método mostrarDetalle.
    # persona1._edad = 40 (solo lectura)
    # print(persona1.edad)

    #Tarea: crear tres objetos mas, utilizando los metodos getter and setter
    #para modificar , y mostrar los cmbios con el metodo mostrar detalle
    print("\n")
    # Creamos tres objetos más.
    persona2 = Persona2("flor", "romero", 19)
    persona2.nombre = "Luciano"
    persona2.apellido = "Ferreyra"
    persona2.edad = 21
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.mostrarDetalle()


    persona3 = Persona2("claro", "Feliza", 21)
    persona3.nombre = "Dario"
    persona3.apellido = "Flores"
    persona3.edad = 23
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.mostrarDetalle()


    persona4 = Persona2("nati", "lucer", 35)
    persona4.nombre = "natalia"
    persona4.apellido = "lucero"
    persona4.edad = 21
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.mostrarDetalle()

    print(__name__)
