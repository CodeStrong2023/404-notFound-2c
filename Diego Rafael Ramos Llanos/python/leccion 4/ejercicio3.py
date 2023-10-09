# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [
    {
        'Nombre': 'Aragorn',
        'Clase': 'Guerrero',
        'Raza': 'Dúnadan del norte'
    },
    {
        'Nombre': 'Gandalf',
        'Clase': 'Mago',
        'Raza': 'Istar'
    },
    {
        'Nombre': 'Legolas',

        'Clase': 'Arquero',
        'Raza': 'Elfo Sindar'
    }
]
for personaje in personajes:
    print("Nombre:", personaje['Nombre'])
    print("Clase:", personaje['Clase'])
    print("Raza:", personaje['Raza'])
    print()
# Se podria de igual manera utilizando como diccionario para luego a una variable (P) almacenar la lista como lo hace el profe betancud
