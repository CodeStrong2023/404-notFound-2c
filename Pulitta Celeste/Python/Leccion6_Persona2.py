class Persona2:
    def __init__(self, nombre, apellido, edad ):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property # decorador
    def nombre(self): # Metodo Getter
        print('Estamos utilizando el método get')
        return  self._nombre
    @nombre.setter
    def nombre(self, nombre): #Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre
    @property
    def apellido(self):
        print('Estamos utilizando el método get')
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('Estamos utilizando el método set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre) #Llamamos al método getter
    persona1.nombre = 'Juan Pedro' # Llamamos la metodo setter
    print(persona1.nombre) # Otra vez con el metodo getter
    print(persona1.mostrar_detalle())# Llamamos el metodo mostrar_detalles
    # Atributo read-only sería la edad porque no tiene el método set
    print(persona1.edad)

    # Tarea crear tres objetos mas, utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el metodo mostrar_detalles

    #Objeto numero uno de la tarea
    persona2 = Persona2('Nadir', 'Meris', 32)
    persona2.nombre = 'Ismael'
    persona2.apellido ='Merhis'
    persona2.edad = 32
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalle())
    #Objeto número dos de la tarea
    persona3= Persona2('kaled', 'Meris', 4)
    persona3.nombre = 'Nuried'
    persona3.apellido = 'Merhis'
    persona3.edad = 5
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalle())
    # Objeto número 3 de la tarea
    persona4 = Persona2 ('Cele', 'Pula', 25)
    persona4.nombre = 'Celeste'
    persona4.apellido = 'Pulitta'
    persona4.edad = 32
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalle())

    print(__name__)
