# ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# un diccionario donde la clave sea el nombre del usuario y el
# valor sea el telefono, el programa tendra el siguiente menu de opciones.
#           1. nuevo contacto
#           2. Borrar contacto
#           3. Ver contactos existentes
#           4: Salir
agenda={}
def nuevo_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto {nombre} con número {telefono} agregado.")
def borrar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea borrar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} borrado.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")
def ver_contactos():
    print("Contactos en la agenda:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
while True:
    print("\nMenú de opciones:")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        nuevo_contacto()
    elif opcion == "2":
        borrar_contacto()
    elif opcion == "3":
        ver_contactos()
    elif opcion == "4":
        print("Gracias por usar la agenda telefónica. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

