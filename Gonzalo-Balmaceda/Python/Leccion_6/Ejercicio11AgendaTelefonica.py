agenda = {}
while True:
    print(".:Menú:.")
    print("1. Nuevo Contacto")
    print("2. Borrar Contacto")
    print("3. Ver Contactos Existentes")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))

    if (opcion == 1):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = int(input("Ingrese el número de teléfono: "))
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agendado exitosamente!")
        else:
            print("El nombre del contacto ya existe en su agenda.")
    elif (opcion == 2):
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("No se encontro el nombre del contacto a borrar.")
    elif (opcion == 3):
        if len(agenda) >= 1:
            print(".:Contactos:.")
            for clave, valor in agenda.items():
                print(f"Nombre: {clave}, Teléfono: {valor}")
        else:
            print("No tiene contacto agendados.")
    elif (opcion == 4):
        print("Saliendo del programa...")
        break
    else:
        print("Esa opción no existe, pruebe con otra.")