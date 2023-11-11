class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f"La Clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Javier", "Mariñanco", 42449860, 24)  # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f"El objeto1 de la clase Persona es: {persona1.nombre} {persona1.apellido} Edad: {persona1.edad}")

persona2 = Persona("Ariel", "Betancud", 32456789, 40)
print(f"El objeto2 de la clase Persona es: {persona2.nombre} {persona2.apellido} Edad: {persona2.edad}")

persona1.nombre = "Osvaldo"
persona1.apellido = "Giordanini"
persona1.edad = 45
print(f"El objeto1 modificado de la clase Persona es: {persona1.nombre} {persona1.apellido} Edad: {persona1.edad}")

# Los atributos: son caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle() # La referencia en este caso es de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) # debemos pasar una referencia manual para el self, sino aparecera un error

persona1.telefono = "2604123456"
print(f"Este es el telefono de: {persona1.nombre} {persona1.telefono}") # Hemos creado un atributo de un objeto

# print(persona2.telefono) # el objeto persona2 no tiene este atributo, da error

persona3 = Persona("Rogelio", "Romero", 34930022, 29, "Telefono", "26933667779", "Calle San Jose", 83, "Manzana", 7, "Casa", 18, Altura= 1.74, Peso= 86, CFavorito= "Azul", Auto= "Citroen", Modelo= 2020 )
persona3.mostrar_detalle()
# print(persona3._dni) #esto no se debe utilizar (esta encapsulado) en python, esto dice que lo desconocemos la sintaxis
# persona3.__nombre # Esta totalmente encapsulado