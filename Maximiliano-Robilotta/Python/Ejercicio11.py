# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario dónde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
#   1. Nuevo contacto
#   2. Borrar contacto
#   3. Ver contactos existentes
#   4. Salir

agenda = {}
while True:
    print("\t.:MENÚ:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opción del menú: "))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el número de teléfono: ")
        if nombre not in agenda:  # Si el nombre no está en la agenda
            agenda[nombre] = telefono
            print("¡Contacto creado exitosamente!")
        else:
            print("Este nombre de contacto ya existe.")
    elif opcion == 2:
        nombre = input("Cuál es el nombre del contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Contacto eliminado.")
        else:
            print("Contacto inexistente.")
    elif opcion == 3:
        print("AGENDA DE CONTACTOS")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Teléfono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos.")
        break  # Rompe estructura for, if, elif y else
    else:
        print("Opción de menú INCORRECTA.")
        print()