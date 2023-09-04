# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)

# Crea una lista que solo incluya los numeros menores a 5.
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)