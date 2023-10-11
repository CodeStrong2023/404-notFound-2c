# Ejercicio 8: Menu interactivo cajero automatico
# hacer un programa que simule un cajero automatico con saldo
# inicia de 1000$ y tendra el siguiente menu de opciones:
#                    1. ingresar dinero en la cuenta
#                    2. Retirar dinero de la cuenta
#                    3. Mostrar dinero disponible
#                    4. Salir
dinero=1000
def ingresar_dinero():
    global dinero
    monto=float(input("Monto deseado a ingresar: "))
    dinero+=monto
    print(f"Se han depositado ${monto}. El saldo actual es: ${dinero}")
def retirar_dinero():
    global dinero
    monto=float(input("Monto que desea retirar: "))
    if monto > dinero:
        print("\nNo tiene esa cantidad de dinero")
        print(" ")
    else:dinero-=monto
def mostrar_saldo():
    global dinero
    print(f"Monto actual: {dinero}")
while True:
    print("1. ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        ingresar_dinero()
    elif opcion == "2":
        retirar_dinero()
    elif opcion == "3":
        mostrar_saldo()
    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")


