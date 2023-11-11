class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalle(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")
    @property # Decorador
    def nombre(self): #Metodo Getter
        print("Estamos utilzando el metodo Get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # Metodo Setter
        print("Estamos utilizando el metodo Set")
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")


if __name__ == "__main__":
    persona1 = Persona2("Ariel","Betancud",41)
    print(persona1.nombre) # Llamamos al metodo getter
    persona1.nombre = "Juan Pedro" # Llamamos al metodo setter
    print(persona1.nombre) # Otra vez con el metodo getter
    print(persona1.mostrar_detalle()) # Llamamos al metodos mostrar_detalle
    # Atributo read-only (solo lectura) seria la edad porque no tiene el metodo set
    print(persona1.edad)

    # Tarea crear tres objetos mas, utilizando los metodos getter and setter
    # para modificar y mostrar los cambios con el metodo mostrar_detalle

    persona2 = Persona2("Mariñanco","Javier",24)
    persona3 = Persona2("Rodrigo","Alcaraz",27)
    persona4 = Persona2("leonel","Fernandez",36)
    print(persona2.nombre,persona2.apellido,persona2.edad)
    print(persona3.nombre,persona3.apellido,persona3.edad)
    print(persona4.nombre,persona4.apellido,persona4.edad)

    persona2.nombre = "Kevin"
    persona2.apellido = "Velazquez"
    persona2.edad = 40

    persona3.nombre = "Luciano"
    persona3.apellido = "Garcia"
    persona3.edad = 43

    persona4.nombre = "Rolan"
    persona4.apellido = "Miranda"
    persona4.edad = 45

    print(persona2.mostrar_detalle())
    print(persona3.mostrar_detalle())
    print(persona4.mostrar_detalle())

    print(__name__)