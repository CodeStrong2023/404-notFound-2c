# ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repeticion)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = ["hola",1,42,"adios",66, "sin que dcir", "holax2",12,"c"]
lista2 = ["num1",4, "hola",5, "numa3",66, "num4", "num5"]
set_lista1 = set(lista1)
set_lista2 = set(lista2)
union=list(set_lista1 | set_lista2)
print(union)
palabras_solo_en_lista1 = []
palabras_solo_en_lista2 = []
palabras_enambas = []
for palabra in lista1:
    if palabra not in lista2 and palabra not in palabras_solo_en_lista1:
        palabras_solo_en_lista1.append(palabra)
print("palabras que aparecen en la primera lista, pero no en la segunda: ",palabras_solo_en_lista1)
for palabra in lista2:
    if palabra not in lista1 and palabra not in palabras_solo_en_lista2:
        palabras_solo_en_lista2.append(palabra)
print("palabras que aparecen en la segunda lista, pero no en la primera: ",palabras_solo_en_lista2)
for palabra in lista1:
    if palabra in lista2 and palabra not in palabras_enambas:
       palabras_enambas.append(palabra)
print("palabras que aparecen en ambas listas: ",palabras_enambas)