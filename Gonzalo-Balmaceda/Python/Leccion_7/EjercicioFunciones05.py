# De celsius a fahrenheit
def celsiusAFahrenheit(celsius):
    return celsius * 9 / 5 + 32

celsius = float(input("Ingrese el valor en celsius: "))
resultado = celsiusAFahrenheit(celsius)
print(f"{celsius} C a F => {resultado:.2f}")

# De fahrenheit a celsius.
def fahrenheitACelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = (float(input("Ingrese el valor en fahrenheit: ")))
resultado = fahrenheitACelsius(fahrenheit)
print(f"{fahrenheit} => F a C {resultado:.2f}")