class Cubo:
    '''
    Crear la clase cubo con los atributos, ancho, alto y profundidad,
    con un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    '''
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundidad

alto = int(input("Digite un valor para la altura del cubo: "))
ancho = int(input("Digite un valor para el ancho del cubo: "))
profundidad = int(input("Digite un valor para la profundidad del cubo: "))
cubo1 = Cubo(alto, ancho, profundidad)

print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")