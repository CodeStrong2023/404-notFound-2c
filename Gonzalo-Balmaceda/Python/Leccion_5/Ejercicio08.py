dineroDisp = 1000
agregarDin = 0
retirarDin = 0

while True:
    opcion = int(input("Opciones \n 1. Agregar dinero a la cuenta \n 2. Retirar dinero de la cuenta \n 3. Mostrar dinero "
              "diponible \n 4. Salir \n Ingrese un Opcion: "))
    if (opcion == 1):
        agregarDin = int(input("Digite la suma de dinero a agregar: "))
        if (agregarDin < 0):
            print("Dinero agregado con éxito")
        else:
            print("Error, la suma a agregar debe ser mayor a cero")
    elif (opcion == 2):
        retirarDin = int(input("Ingrese la cantidad de dinero a retirar: "))
        if (retirarDin < 1000 or retirarDin == 0):
            print("Error, ingreso un valor igual a cero o esta intentando retirar más dinero de lo disponible, vuelva a intentar")
        else:
            print("Dinero retirado con éxito")
    elif (opcion == 3):
        print(f"Dinero disponible en la cuenta = {(agregarDin + dineroDisp) - retirarDin}")
    elif (opcion == 4):
        break