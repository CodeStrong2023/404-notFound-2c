# Tipos de datos.
# Tipo int.
a = 10
print(a)
print(type(a))  # El comando 'type' nos muestra en consola el tipo de dato de la variable.
# Tipo float.
a = 3.1416
print(a)
print(type(a))
# Tipo string.
a = 'Hola alumnos'
print(a)
print(type(a))
# Tipo booleano.
a = True
print(a)
print(type(a))
a = False
print(a)
print(type(a))

# Manejo de cadenas (String).
miGrupoFavorito = 'Los enanitos verdes:'
caracteristicas = 'La mejor banda de Argentina'
print('Mi grupo favorito es: ', miGrupoFavorito, caracteristicas)

# Mas temas de manejo de cadenas.
# numero1 = '7'
# numero2 = '8'
# print(int(numero1) + int(numero2))

# Tipo Booleano (bool).
miBooleano = 3 > 5
print(miBooleano)

if miBooleano:
    print('El resultado es verdadero')
else:
    print('El resultado es falso')

# Procesar entrada del usuario (Función input)
# resultado = input('Digite un numero: ')  # Regresa un dato tipo string.
# print(' El numero ingresado es: ' + resultado)

# Conversión de la entrada de datos
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
suma = numero1 + numero2
print('La suma de los dos numeros es: ', suma)
