class Persona: # Creamos una clase
   def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):# Se lo llama método init dunder
       self.nombre = nombre
       self.apellido = apellido
       self._dni = dni #Este atribito esta encapsulado de una manera sugerida
       self.edad = edad
       self.args = args
       self.kwargs = kwargs
   def mostar_detalle(self): # self es igual a this
       print(f'Persona: {self.nombre} {self.apellido} {self.edad} La dirección es: {self.args}, los datos importantes son: {self.kwargs}')
persona1 = Persona('Ariel', 'Betancud', 7689533, 40)
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El ojeto1 de la calse persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')
persona2 = Persona('Osvaldo', 'Giordanini', 765432, 45)
print(f'El ojeto2 de la calse persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona3 = Persona('Debora', 'Pulitta', 566899987, 32)
print(f'El objeto3 de la clase persona: {persona3.nombre} {persona3.apellido} Su edad es: {persona3.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Bucella'
persona1.edad = 40
print(f'El ojeto1 modificado de la calse persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostar_detalle() # la referencia en este caso se pasa de manera automatica
persona2.mostar_detalle()

#Persona.mostar_detalle(persona1)#Debemos pasarle una referencia para el self o dará error
persona1.telefono = 2727282929
print(f'Este es el telefono de:{persona1.nombre} {persona1.telefono}') # Hemos creado un atributo de un objeto
#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona4 = Persona('Rogelio', 'Romero', 65789912, 22, 'Telefono', '678921376', 'Calle lopez', 789, 'Manzana', 77, 'Casa', 18, Altura= 1.83, peso= 105, CFavorito='Azul', Auto= 'Citroen', Modelo=2021)
persona4.mostar_detalle()

persona5 = Persona('Nadir', 'Merhis', 33, 'Telefono', 78901233, 'Calle Independencia', 4567, 'Manzana', 6, 'Casa', 5, Altura=1.76, Peso=96, CFavorito='negro', Auto='Logan', Modelo=2020)
persona5.mostar_detalle()
#print(persona3._dni) Esto no se debe usar en python, esto dice que lo desconocemos

