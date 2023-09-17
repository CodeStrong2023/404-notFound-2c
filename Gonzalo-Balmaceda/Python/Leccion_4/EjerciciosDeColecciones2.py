lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

# Eliminamos los elementos repetidos de cada lista.
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Unimos las dos listas.
union = list(conjunto1 | conjunto2)
print(f"Union: {union}")

# Mostramos solo el conjunto1.
mostrar1 = list(conjunto1 - conjunto2)
print(f"Mostramos el conjunto1: {conjunto1}")

# Mostramos solo el conjunto2.
mostrar2 = list(conjunto2 - conjunto1)
print(f"Mostramos el conjunto2: {conjunto2}")

# Mostramos los elementos que tienen en común los dos conjuntos
elementosEnComun = list(conjunto1 & conjunto2)
print(f"Mostramos los elementos que tienen en común los dos conjuntos: {elementosEnComun}")
