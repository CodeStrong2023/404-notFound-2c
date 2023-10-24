# Ejercicio 4: Convertidor de temperaturas
# Realizar dos funciones para covnertir de grados celsius
# a farenheit y viseversa.
# Invsetigar las fórmulas

#Función que convierte de celsius a fahrenheit

def celsius_farenheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia: multiplicación, división y suma

#Función que convierte de fahrenheit a celsius
def  fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respetar la presedencia utilizando paréntesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_farenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')