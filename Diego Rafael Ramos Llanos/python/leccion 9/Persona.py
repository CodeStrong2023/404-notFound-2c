class Persona:  # creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # se lo llama metodo init dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni  # encapsulado
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # self es igual a this
        print(
            f"Persona: {self.nombre},{self.apellido},{self._dni},{self.edad} direccion: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("ariel", "betancud", 32456987, 40)  # se necesita enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f"el objeto1 de la clase persona:{persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")
persona2 = Persona("osvaldo", "giordanini", 11111111, 45)
print(f"el objeto de la clase persona:{persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}")

persona1.nombre = "liliana "
persona1.apellido = 'buccella'
persona1.edad = 40
print(f"el objeto de la clase persona:{persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")

persona1.mostrar_detalle()
persona2.mostrar_detalle()

persona1.telefono = "8912879129872"
print(persona1.telefono)  # hemos creado un atributo de un objeto
print(f"este es el telefono de: {persona1.nombre}{persona1.telefono}")

# print(persona2.telefono) #el objeto persona2 no tiene este atributo, da error
persona3 = Persona("Rogelio", "Romero", 22424, 22, "telefono", "24323424", "calle lopez", 823, "manzana", 77, "casa",
                   18, Altura=1.83, Peso=100, CFavorito="Azul", Auto="citroen", modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) esto no se debe utilizar en python, esto dice que lo desconocemos
