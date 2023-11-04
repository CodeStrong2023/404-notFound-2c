# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista

# Creamos una lista
lista= [8, 22, 15, 'Kaled', 'Nuried', 22, 'Kaled']
conjunto = set(lista)
lista = list(conjunto)
print(lista)
