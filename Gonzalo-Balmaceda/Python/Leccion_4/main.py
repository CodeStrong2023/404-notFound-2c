"""
# Operadores logicos.
a = True
b = True
resultado = a and b #El operador 'and' nos devuleve True si ambos operandos son True.
print(resultado)

#Operdador or
resultado = a or b #En el operador 'or' nos devuelve True con que solamente un operando sea True.
print(resultado)

#Operador not
resultado = not a #El operador 'not' nos devuelve el valor contrario del operando asignado.
print(resultado)
"""
"""
#Ejercicio: Valor dentro de un rango
valor = int(input('Digite un numero dentro del rango 0 a 5: '))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} esta fuera de rango')
"""
"""
#Ejercicio con el operador or, operador not
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print('Puede asistir al juego')
else:
    print('Hay trabajo que hacer')
"""
"""
#Ejercicio: Rango entre 20 y 30 años
edad = int(input('Digite su edad: '))
#veinte = (edad >= 20 and edad < 30)
#print(veinte)
#treinta = (edad >= 30 and edad < 40)
#print(treinta)
if (20 <= edad < 30) or (30 <= edad < 40): #Sintaxis simplificada del operador 'ant'
    print( 'estas dentro del rango de los (20\'0) a (30\'0) años')
#    if veinte:
#        print('Estas dentro del rango de los (20\'0) años')
#    elif treinta:
#        print('Estas dentro del rango de los (30\'0) años')
else:
    print('No estas dentro del rango de los (20\'0) a (30\'0) años')
"""
"""
#Ejercicio: El mayor de dos numeros
numero1 = int(input('Digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))
if numero1 > numero2:
    print('El numero 1 es mayor')
else:
    print('El numero 2 es mayor')
"""
#Ejercicio: Tienda de libros
print('Ingrese los siguientes datos del libro')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el id del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el envio es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')
