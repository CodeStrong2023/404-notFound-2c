# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendra el siguiente menu de opciones:
#     1.Nuevo contacto
#     2.Borrar contacto
#     3.Ver contactos existentes
#     4.Salir
agenda = {}
while True:
    print("\n.:MENU:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion de Menu: "))
    if opcion == 1:
        nombre = input("Digite nombre del contacto: ")
        telefono = input("Digite numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agragado exitosamente!")
        else:
            print("Este nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("Cual el nombre del contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Se ha eliminado el contacto requerido")
        else:
            print("Ese contacto no existe en la agenda")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Se equivoco de opcion de menu")
    print()