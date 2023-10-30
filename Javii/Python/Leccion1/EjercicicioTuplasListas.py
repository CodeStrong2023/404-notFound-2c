import math # Importamos la clase mach para hacer uso de la funcion sqrt(raiz cuadrada)
#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definir la tupla
#Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 3, 2]

lista = [] #Definimos fla lista
#Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento <5:
        lista.append(elemento)
        print(lista)

# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo"))
while numero < 0:
    print("Error -> Deveria der un numero positivo")
    numero = int(input("Digite un numero positivo: "))
print(f"\Su raiz cuadrada es: {math.sqrt(numero):.2f}")