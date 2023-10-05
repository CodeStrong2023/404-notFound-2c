numero = int(input("Ingrese un número: "))
def imprimirNumeroRecursivos(numero):
    if numero >= 1:
        print(numero)
        imprimirNumeroRecursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("El valor ingresado es incorrecto")

imprimirNumeroRecursivos(numero)