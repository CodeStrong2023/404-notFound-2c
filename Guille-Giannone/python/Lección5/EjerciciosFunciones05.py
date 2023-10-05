# Ejercicio 5: convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahreinheit y viceversa.
# Investigar las formulas

# Funcion que convierte de Celsius a Fahreinheit
def celsius_fahreinheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia, multiplicacion, division y suma

# Funcion que convierte de Fahreinheit a Celsius
def fahreinheit_celsius(fahreinheit):
    return (fahreinheit - 32) * 5 / 9 # Respetar la presedencia utilizando parentesis

celsius = float(input("Digite el valor de Celsius: "))
resultado = celsius_fahreinheit(celsius)
print(f"{celsius} C a F -> {resultado: .2f}")

fahreinheit = float(input("Digite el valor en Fahreinheit: "))
resultado = fahreinheit_celsius(fahreinheit)
print(f"{fahreinheit} F a C -> {resultado: .2f}")