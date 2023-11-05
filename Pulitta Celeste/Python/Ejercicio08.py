 Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule u cajero automatico con un saldo
# inicial de 1000$ y tendra el sig menú de opciones:
#                   1. Ingresar dinero en la cueta
#                   2. Retirar diero de la cuenta
#                   3. Mostrar dinero disponible
#                   4. Salir

saldo = 1000
while True:
    print('\t.:MENÚ:.')
    print('1. Ingresar dinero en la cueta')
    print('2. Retirar diero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input("Digite una opción de menú: "))
    print()
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar'))
        saldo +=extra
        print(f'Dinero en la cuenta: $ {saldo}')
    elif opcion == 2:
        retirar = float(input('Cuanto dinero desea retirar -> '))
        if retirar > saldo:
            print('No tiene esa cantidad de dinero')
        else:
            saldo -= retirar
            print(f'Dinero en la cuenta al momento: $ {saldo}')
    elif opcion == 3:
        print(f'Dinerooen la cuenta al momento: $ {saldo}')
    elif opcion == 4:
        print('Gracias por utilizar su cajero automatico, hasta pronto')
        break
    else:
        print('Error se equivoco de opción de manú')
