# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa que tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista.

# Creamos una lista
lista = [1,2,3,"Ariel","Guillermo",7,1,1,7,"Alberto","Ariel",2,"Alberto"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversion hecha en una sola linea de codigo (mas eficiente)
print(lista)