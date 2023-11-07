class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, edad):  # self significa uno mismo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")


persona1 = Persona("Ariel", "Betancud", 40)  # Nesecitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

persona2 = Persona("Osvaldo", "Giordanini", 45)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

# Los atributos son caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostar_detalle()
persona2.mostar_detalle()