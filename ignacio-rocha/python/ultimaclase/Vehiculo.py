class Vehiculo:
    """
    definir una clase padre llamada vehiculo y dos clases
    hijas llamadas auto y bicicleta, los cuales heredan de la clase padre
    vehiculo. la clase padre tener los siguientes atributos y metodos:
    vehiculo (clase padre)
    atributos(color,ruedas)
    metodos(__init__(color,ruedas) y __str__())

    Auto(clase hija de vehiculo)
    -atributos(vecocidad(km/hr))
    -metodos(__init__(color,ruedas,velocidad) y __str__())

    Bicicleta(clase hija de vehiculo)
    -Atributos(tipo(urbana/montaña/etc.))
    -Metodos(__init__(color,ruedas,tipo) y __str__())

    crear un objeto  de cada clase

    """
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return "color: "+self.color+" ruedas: "+str(self.ruedas)
    
class Auto(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad=velocidad

    def __str__(self):
        return super().__str__()+', velocidad km/h ) '+str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(Self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        Self.tipo=tipo

    def __str__(Self):
        return super().__str__()+" . tipo:" +Self.tipo
#primer objeto de la clase padre vehiculo
vehiculo=Vehiculo("blanco",4)
print(vehiculo)

#segundo objeto, pero ahora de la clase Auto
auto=Auto("amarillo",4,120)
print(auto)

#tercer objeto , el ultimo de la clase biblioteca
bici=Bicicleta("azul",2,"urbana")
print(bici)