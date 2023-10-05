def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ["Gonzalo", "Nicolas", "Luciano"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
#desplegarNombres(10, 11) # No es un objeto iterable.
desplegarNombres((10, 11)) # La convertimos en una tupla.
desplegarNombres([22, 55]) # La convertimos en una lista.