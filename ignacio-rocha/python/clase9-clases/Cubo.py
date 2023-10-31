class Cubo:
    """
    crear la clase cubo con los atributos,ancho,alto y profundidad,con
    un metodo calcular_volumen que tendra la formula:
    volumen=ancho*altura*profundidad
    qe el usuario ingrese los valores
    """

    def __init__(self,ancho,altura,profundidad):
        self.ancho=ancho
        self.altura=altura
        self.profundidad=profundidad

    def calcular_volumen(self):
        return self.ancho+sef.altura+self.profundidad

ancho=int(input("digite el ancho: "))
altura=int(input("ingrese la altura: "))
profundidad=int(input("ingrese la profundiddad: "))
cubo1=Cubo(ancho,altura,profundidad)
print(f"el volumen del cubo es: {cubo1.calcular_volumen()}")