class Vehiculo:
    ''' Definir una clase padre llamada vehiculo y dos clase hijas llamdas
    auto y vicicleta, las cuales heredan la clase padre vehiculo.La clase padre
    debe tener los siguientes atributos y metodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Métodos(__init__(color,ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (km/hr))
    -Métodos(__init__(color,ruedas,velocidad) y __str__() )

    Bicicleta(clase hija de Vehiculo)
    -Atributos (tipo(urbana/montaña/etc.)
    -Métodos(__init__(color,ruedas,tipo) y __ str__()

    Crear un objeto de cada clase.
    '''
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color:"+self.color+" Ruedas:"+str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, rueda, velocidad):
        super().__init__(color, rueda)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+" Velocidad(km/hr):" + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() +", Tipo: " + self.tipo

vehiculo = Vehiculo("Blanco", 4)
print(vehiculo)

auto = Auto("Verde", 4, 170)
print(auto)

bicicleta = Bicicleta("Rojo", 2, "Urbana")
print(bicicleta)

