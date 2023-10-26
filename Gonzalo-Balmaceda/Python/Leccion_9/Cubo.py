class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la fórmula:
    volumen = ancho * alto * profundidad
    que el usuario ingrese sus valores.
    """

    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundiad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundiad

ancho = int(input("Ingrese el ancho del cubo: "))
alto = int(input("Ingrese el alto del cubo: "))
profundidad = int(input("Ingrese la profundidad del cubo: "))

volumen = Cubo(ancho, alto, profundidad)
print(f"El volumen del cubo es {volumen.calcular_volumen()}")