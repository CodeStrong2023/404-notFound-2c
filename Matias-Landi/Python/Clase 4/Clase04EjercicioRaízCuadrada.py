import math # Importamos la clase math para hacer uso de la función sqrt (raíz cuadrada)

#Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input('Digite un númeto positivo: '))
while numero < 0:
    print('Error -> Debería esr un número positivo')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')