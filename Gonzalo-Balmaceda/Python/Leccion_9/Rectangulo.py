class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos, altura y base
    el nombre del método será calcular área utilizando la formula:
    área = base * altura. Pero la besa y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """
    
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input("Ingrese un número para la base del rectangulo: "))
altura = int(input("Ingrese otro número para la altura del rectangulo: "))
area = Rectangulo(base, altura)
print(f"El área del rectrangulo es: {area.calcular_area()}")