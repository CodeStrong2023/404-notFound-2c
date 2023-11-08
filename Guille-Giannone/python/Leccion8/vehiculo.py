class Vehiculo:
    """
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas
    auto y bicicleta, las cuales heredan de la clase padre vehiculo. La clase padre
    debe tener los siguientes atributos y métodos:

    Vehiculo (Clase Padre)
    - Atributos (color, ruedas)
    - Métodos (__init__(color, ruedas) y __str__())

    Auto (clase hija de vehiculo)
    - Atributos (velocidad (km/hr))
    -Métodos (__init__(color, ruedas, velocidad) y __str__())

    Bicicleta (clase hija de vehiculo)
    - Atributos (tipo(urbana/montaña/etc.))
    - Métodos (__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase
    """

    def __init__(self,color,ruedas):
        self.ruedas = ruedas
        self.color = color


    def __str__(self):
        return "Color: "+self.color+", Ruedas: "+str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+", Velocidad(km/h): "+str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__()+", Tipo: "+self.tipo
#Primer objeto de la clase padre vehiculo
vehiculo = Vehiculo("Blanco",4)
print(vehiculo)

#Segundo objeto, pero ahora de la clase Auto
auto = Auto("Amarillo", 4, 120)
print(auto)

#Tercer objeto, ahora de la calse Bicicleta
bicicleta = Bicicleta("Rojo",2,"montaña")
print(bicicleta)