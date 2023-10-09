# Ejercicio 05: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsiues
# a fahrenheit y viceversa
# Investigar las fórmulas

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32  # La precedencia: multiplicación, división y suma


celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C a F -> {resultado:.2f}")


# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # Respetar la precedencia utilizando paréntesis


fahrenheit = (float(input("Digite el valor en fahrenheit: ")))
resultado = fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} -> F a C {resultado:.2f}")
