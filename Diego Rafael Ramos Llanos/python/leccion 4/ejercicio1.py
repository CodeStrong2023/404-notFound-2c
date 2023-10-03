# 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos una lista
lista = [1, "d", 4, "ar", 24, 24, 1, "f", "g", "f"]
lista_sin_duplicados=[]
for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
print(lista_sin_duplicados)

# otra manera mas facil, sin embarogo no imprime ordenadamente debido a una caracteristica de python
conjunto = list(set(lista))
print(conjunto)