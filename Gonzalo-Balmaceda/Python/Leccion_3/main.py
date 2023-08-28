"""
# Operadores Aritmeticos.
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
division = operandoA // operandoB
print(f'El resultado de la division (int) es: {division}')

modulo = operandoA % operandoB
print(f'El resultado de la division de residuo es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')
"""
"""
#Ejercicio: Rectangulo
alto = int(input('Proporcione el alto del rectangulo: '))
ancho = int(input('Proporcione el ancho del rectangulo: '))
area = alto * ancho
print(f'Area: {area}')
perimetro = (alto + ancho)*2
print(f'Perimetr: {perimetro}')
"""
"""
miVariable3 = 10
print(miVariable3)

#Operadores de reasignacion.
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVarible3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)
"""
"""
# Operadores de comparacion.
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales.
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)
"""
"""
# Ejercicio_1: numero par o impar

a = int(input('Ingrese un numero: '))
print(f'El residuo de la division es: {a % 2}')
if a % 2 == 0:
    print(f'El valor de a es: {a} es un numero par')
else:
    print(f'El valor de a es: {a} es un numero impar')
"""

# Ejercicio_2: Determinar si es mayor de edad

edadAdulto = 18
edadPersona = int(input('Ingrese su edad: '))
if edadPersona >= edadAdulto:
    print(f'Su edad es: {edadPersona} años, usted es mayor de edad')
else:
    print(f'Su edad es: {edadPersona} años, usted es menor de edad')
