class Cubo:
    """
    crear la clase cubo con los atributos,ancho,alto y profundidad,con
    un metodo calcular_volumen que tendra la formula:
    volumen=ancho*altura*profundidad
    qe el usuario ingrese los valores
    """
    def __init__(self):
        self.ancho = float(input("Ingrese el ancho del cubo: "))
        self.alto = float(input("Ingrese el alto del cubo: "))
        self.profundidad = float(input("Ingrese la profundidad del cubo: "))

    def calcular_volumen(self):
        # Calcular el volumen del cubo
        volumen = self.ancho * self.alto * self.profundidad
        return volumen

cubo = Cubo()

volumen = cubo.calcular_volumen()

print("El volumen del cubo es:", volumen)
