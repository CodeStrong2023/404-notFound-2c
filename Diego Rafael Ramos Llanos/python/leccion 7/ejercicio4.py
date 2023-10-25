# ejercicio 5: convertidor de temperatura
# realizar dos funciones para convertir de grados celsius
# a fahrenheit y viceversa. investigar las formulas

def celcius_farengei(celsius):
    Fahrenheit = (celsius*9 / 5) + 32
    return Fahrenheit
def farengei_selcius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5 / 9
    return Celsius

print("Selecione una opcion")
print("1:Si es de Celsius a Fahrenheit")
print("2:Si es de Fahrenheit a Celsius")
cof=int(input(""))
if cof == 1:
    celsius = float(input("digite el valor de celsius: "))
    resultado = celcius_farengei(celsius)
    print(f"{celsius} C a F ->{resultado:.2f}")
elif cof == 2:
    Fahrenheit = float(input("ingrese el valor de fahrenheit: "))
    resultado =farengei_selcius(Fahrenheit)
    print(f"{Fahrenheit } F a C ->{resultado:.2f}")
else:
    print("Numero equivocado, Digite nuevamente")