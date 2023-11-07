class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    # Método dunder str
    def __str__(self):
        return f"Vehiculo [ Color: {self.color}, Ruedas: {self.ruedas} ]"


class Auto(Vehiculo):
    def __init__(self, color, rueda, velocidad):
        super().__init__(color, rueda)
        self.velocida = velocidad

    def __str__(self):
        return f"Auto [ Velocidad: {self.velocida} km/h ] {super().__str__()}"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta [ Tipo: {self.tipo} ] {super().__str__()}"


vehiculo = Vehiculo("Negro", 4)
print(vehiculo)

auto = Auto("Gris", 4, 180)
print(auto)

bicicleta = Bicicleta("Naranja", 2, "Montaña")
print(bicicleta)
