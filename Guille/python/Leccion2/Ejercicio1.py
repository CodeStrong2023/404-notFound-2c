
#Ejercicio 1:
#Deberemos plasmar la expresion en una expresion algoritmica,
#osea hacerlo en codigo
'''
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print(f"EL resultado es: {resultado}")


#Ejercico 2
a= float(input("Digite un valor para a: "))
b= float(input("Digite un valor para b: "))
resultado = ((3 + 5 * 8 ) < 3 and ((- 6/3 * 4 ) + 2 < 2)) or ( a > b)
print(f"la expresion logica es: {resultado}")



#Ejercicio 3
a = 10
b = 5
print("valor original a: ",a)
print("valor original b: ",b)
cambio = a
a = b
b = cambio
print("valor cambiado a:",a)
print("valor cambiado b: ",b)
'''


#Ejercicio 4
import math
radio = float(input("Ingrese el valor de radio: "))
area = math.pi * (radio ** 2)
longitud = 2 * math.pi * radio
print(f"el area es: {area}")
print(f"la longitud es: {longitud}")

