# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#                               suma de números pares del 2 al 30
#                               suma = 240
lista =[]
suma =0
numInicio =int(input("Digite el inicio de la suma de numeros pares: "))
numFinal =int(input("Digite el final de la suma de numeros pares: "))
for i in range (numInicio,numFinal+1,1):
    if i % 2 == 0:
        suma += i
        lista.append(i)
print(lista)
print(f"La suma de números pares del {numInicio} al {numFinal} es {suma}")
