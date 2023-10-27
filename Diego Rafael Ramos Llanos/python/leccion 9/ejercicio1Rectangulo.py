class Rectangulo:
    """
    crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area=base*altura, pero la base y la altura deben ser ingresadas por el usuario
    y los objetos deben ser 3.
    """
    def __init__(self):
        # Pedir al usuario que ingrese la base y la altura
        self.base = float(input("Ingrese la base del rectángulo: "))
        self.altura = float(input("Ingrese la altura del rectángulo: "))

    def calcular_area(self):
        # Calcular el área del rectángulo
        area = self.base * self.altura
        return area

rectangulo1 = Rectangulo()

area1 = rectangulo1.calcular_area()

print("Área del rectángulo es: ", area1)