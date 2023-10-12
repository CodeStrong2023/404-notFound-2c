class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")


persona1 = Persona("Guillermo", "Giannone", 38)  # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f"El objeto1 de la clase Persona es: {persona1.nombre} {persona1.apellido} Edad: {persona1.edad}")

persona2 = Persona("Ariel", "Betancud", 40)
print(f"El objeto2 de la clase Persona es: {persona2.nombre} {persona2.apellido} Edad: {persona2.edad}")

persona1.nombre = "Osvaldo"
persona1.apellido = "Giordanini"
persona1.edad = 45
print(f"El objeto1 modificado de la clase Persona es: {persona1.nombre} {persona1.apellido} Edad: {persona1.edad}")

# Los atributos: son caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()