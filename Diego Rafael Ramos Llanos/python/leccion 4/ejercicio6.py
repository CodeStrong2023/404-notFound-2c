# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaria de insertar.
# Por último, mostrar los números ordenados de menor a mayor
# Crear una lista vacía para almacenar los números
numeros = []
while True:
    numero = int(input("Introduce un número (0 para dejar de insertar): "))

    if numero == 0:
        break
    else:
        numeros.append(numero)
numeros.sort()
print("Números ordenados:", numeros)
