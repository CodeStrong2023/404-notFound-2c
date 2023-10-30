# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numero del 1 al 10, luego medificar los
# elementos de la lista multiplicandolos por un valor ingresado por un usuario
lista = list(range(1, 11))
print("Lista original")
for i in lista:
    print(i, end=" - ")
valor = int(input("\nDigite un valor a multiplicar: "))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):# Funcion para modificar los indices de la lista
    lista[indice] *= valor # El iterador solo recorre los indices, em esta linea se multiplica

print(f"Lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i,end=" - ")