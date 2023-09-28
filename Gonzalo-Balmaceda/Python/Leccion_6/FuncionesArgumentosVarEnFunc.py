def listaNombres(*nombres): # Hacemos que se puedan agregar una cantidad indefinida de nombres.
    for nombre in nombres:
        print(nombre)

listaNombres("Gonzalo", "Nicolas", "Luciano")
listaNombres("Agustin", "Dario", "Claudia", "Mirta", "Nestor")