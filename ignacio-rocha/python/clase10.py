class Persona2:
    def __init__(self,nombre,apellido,edad):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad

    def mostrar_detalle(self): 
        print(f"los datos importantes a mostrar son: {self._nombre},{self._apellido},{self._edad}")
    @property#decorator
    def nombre(self):#metodo getter
        print("estamos utilizando el metodo get")
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        print("estamos utilizando el metodo set")
        self._nombre=nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        self._edad=edad

    def __del__(self):
        print(f"Persona2: {self._nombre},{self._apellido}{self._edad}")
if __name__=="__main__":

    persona1 = Persona2("ariel","betancud",41)
    print(persona1._nombre)#llamamos al metodo getter
    persona1.nombre="juan pedro"
    print(persona1.mostrar_detalle())
    #atributo read-only seria la edad porque no tiene el metodo set

    #tarea : crear 3 objetos mas, utilizando los metodo getter and setter
    #para modificar, y mostrar los cambios con el metodo mostrar detalles
    persona2=Persona2("flor","Romero",22)
    print(persona2.mostrar_detalle())

    persona3=Persona2("caro","Felisa",21)
    print(persona3.mostrar_detalle())

    #objeto numero tres de la tarea
    persona4=Persona2("naty","lucero",35)
    print(persona4.mostrar_detalle())

    print(__name__)
