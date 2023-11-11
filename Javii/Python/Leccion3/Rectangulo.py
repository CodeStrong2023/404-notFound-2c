class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresados por el usuario
    y los objetos deben ser tres.
    """
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Digite un numero para la base del rectangulo: '))
altura = int(input('Digite un numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo( base, altura)
print(f'La base del rectangulo es: {rectangulo1.calcular_area()}')