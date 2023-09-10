seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad": 35, "Altura": 1.80, "Precio": "75 Millones", "Posicion": "Extremo Derecho"},
    24: {"Nombre": "Enzo Fernandez", "Edad": 22, "Altura": 1.78, "Precio": "38 Millones", "Posicion": "Centrocampista"},
    19: {"Nombre": "Nicolas Otamendi", "Edad": 35, "Altura": 1.83, "Precio": "15 Millones", "Posicion": "Defensor"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Arquero"},
    7: {"Nombre": "Rodrigo De Paul", "Edad": 29, "Altura": 1.80, "Precio": "37 Millones", "Posicion": "Centrocampista"},
    9: {"Nombre": "Julian Alvarez", "Edad": 23, "Altura": 1.70, "Precio": "21 Millones", "Posicion": "Delantero"},
    13: {"Nombre": "Cristian Romero", "Edad": 25, "Altura": 1.85, "Precio": "26 Millones", "Posicion": "Defensor"},
    17: {"Nombre": "Alejandro Gomez", "Edad": 35, "Altura": 1.67, "Precio": "10 Millones", "Posicion": "Centrocampista"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print("Tenemos cargados en el diccionario la cantidad de jugadores:", end=" ")
print(len(seleccionArgentina))
