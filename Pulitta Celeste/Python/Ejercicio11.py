# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos crear un
# diccionario donde la clave sea el nombre del ususario y el valor
# sea el telefono, el programa tendrá el siguiente menú de opciones
#               1. Nuevo contacto
#               2. Borrar contacto
#               3. Ver contactos existentes
#               4. Salir
agenda = {}
while True:
    print('\n:MENÚ:')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción de menú: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el número de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agendado exitosamente! ')
        else:
            print('Este nombre d econtacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto requuerido')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else:
        print('Se equivoco de opción de menú')
    print()
