# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)# Definimos la tupla
# Crear una lista que solo incluya los númems menores a 5
# e imprima por consola [1, 3, 2]

for i in range(len(tupla)):
    if tupla[i] < 5:
        print(tupla[i])

lista_resultado = [numero for numero in tupla if numero < 5]
print(lista_resultado)