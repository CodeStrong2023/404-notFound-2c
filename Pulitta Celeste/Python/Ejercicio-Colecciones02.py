# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a conyinuación
# cree las siguientes listas (en las que no debe haber repetición)
# 1 lista de palabras que aparecen en la lista
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista,  pero no el la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = ['Kaled', 'Merhis', 'Nuried', 1, 5, 9,]
lista2 = ['Celeste', 'Nadir', 'Ismael', 25, 43, 35, 9, 'Nuried']

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto2 - conjunto1)
interseccion = list(conjunto1 & conjunto2)

print(f'lista de palabras que aparecen en la listas: {union}')
print(f'lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}')
print(f'lista de palabras que aparecen en la segunda lista,  pero no el la primera: {solo2}')
print(f'lista de palabras que aparecen en ambas listas: {interseccion}')
