# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde trnga una lista y que a continuación
# elimine los elementos repetidos, por último mosstrar la lista.

# Creamos una lista
lista = [1, 2, 3, 'Ariel', 7, 7, 3, 'Alberto', 5, 'Ariel', 2, 'Alberto']
#conjunto = set(lista) #Convertimos la lista a un conjunto de tipo set
#lista = list(conjunto) #Convertimos el conjunto a una lista
lista = list(set(lista)) #La converión hecha en una sola línea de código (eficiente)
print(lista)