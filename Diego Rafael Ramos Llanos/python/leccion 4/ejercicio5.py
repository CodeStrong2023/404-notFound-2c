# ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, Juego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario
lista=[]
for i in range (1,11,1):
    lista.append(i)
    print(i,end="-")
valor= int(input("\nDigite un valor a multiplicar: "))
# Multiplicamos por el número ingresado.
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f"Lista final con los elementos multiplicados por {valor}")
for i in  lista:
    print(i, end="-")