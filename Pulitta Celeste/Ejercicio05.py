# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
numero = int(input('Digite un número: '))
while numero < 0:
    print('Error -> El número tiene que ser positivo')
    numero = int(inpu('Digite un número: '))
factorial = 1
for i in range(1,numero+1):
    factorial *= i
