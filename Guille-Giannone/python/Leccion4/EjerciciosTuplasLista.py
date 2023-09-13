import math # Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla
# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]

lista = [] # Definimos la lista
# Filtramos los elementos menores a 5 en la tupla
for elementos in tupla:
    if elementos <5:
        lista.append(elementos)
print(lista)

# Ejercicio de matematicas
# Sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error -> deberia ser un numero positivo")
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")
