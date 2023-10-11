class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, edad): # Se lo llama Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self): # Función para acceder a los atributos dentro de una clase.
        print(f"Persona: {self.nombre}, {self.apellido}, {self.edad}")

persona1 = Persona("Gonzalo", "Balmaceda", 20) # Necesitamos enviar argumentos.
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")

persona2 = Persona("Osvaldo", "Giordanini", 45)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}")

# Modificamos un objeto.
persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = "40"
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")

# Los atributos son: Caracteristicas.
# Los metodos son: El comportamiento que van a tener.

persona1.mostrar_detalle()
persona2.mostrar_detalle()