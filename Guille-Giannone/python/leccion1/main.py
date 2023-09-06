'''
miVariable = 3;
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))  # ubicacion de memeria x405
# las literales se escriben x408
print(id(y))  # ubicacion de memeria x152
print(id(z))  # ubicacion de memeria x472 a esto se lo conoce como referencia de memoria

# tipos de variables: int(tipo entero), float(tipo decimal), bool (verdadero o falso), string(texto o caracter)

x = 10
print(x)
print(type(x))
x = 10.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (tipo string)
miGrupoFavorito = "Los Redonditos de Ricota"+", "+"La Mejor Banda de Rock Nacional"
print("Mi Grupo Favorito es: "+miGrupoFavorito) # el simbolo "+" se usa para concatenar

miGrupoFavorito = "Los Redonditos de Ricota"
caracteristica = "La Mejor Banda de Rock Nacional"
print("Mi grupo favorito es: "+miGrupoFavorito+", "+caracteristica) # Ejemplo de concatenar usando 2 variables
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristica) # Ejemplo de concatenar usando "," para unir las variables

numero1 = "7"
numero2 = "8"
print(numero1 + numero2) # En este ejemplo el signo + esta concatenando las 2 variables
print(int(numero1) + int(numero2))
# En este ejemplo la asignamos que sean variables de tipo entero y las encerramos en parentesis para que nos ralice la suma

# Ahora vemos tipos Booleanos (bool) este tipo es para saber si el valor es verdadero o falso
# para hacer signo mayor > (alt+62), y signo menor < (alt+60)
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
# Procesar entrada de datos del usuario
# para eso se utiliza una funcion que se llama input

#resultado = input("Digite un numero: ") # esta funcion regresa un dato tipo string
#print("El numero digitado es:",resultado)

#Conversion de la entrada de datos

#numero1 = input("Escribe el primer numero: ")
#numero2 = input("Escribe el segundo numero: ")
#resultado = numero1 + numero2
#print("El resultado es: ", resultado) # de esta forma me muestra el resultdo de tipo string

numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
# Para que me sume las variables como entero debo asignar el "int" antes de input


# Estos son los operadores Aritmeticos

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("El resultado es: ",suma)
print(f'EL resultado de la suma es: {suma}') # al utilizar la f se lo denomina como interpolacion

resta = operandoA - operandoB
print(f"EL resultado de la resta es: {resta}")
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")
division = operandoA / operandoB
print(f"EL resultado de la division es. {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"EL resultado de la division o modulo (residuo) es: {modulo}")
exponete = operandoA ** operandoB
print(f"El resultado del exponente es: {exponete}")
'''
"""
alto = int(input('Proporciona el alto del resctangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('El perimetro es: ',perimetro)
print('El area es: ',area)
"""
'''
miVariable3 = 10
print(miVariable3)

#Operadores de reasignacion - lo que hacemos es resumir la sintaxis en las operaciones aritmeticas (+,-,*,/)

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)


# Operadores de Comparacion
d=4
b=2
resultado = d==b # Comprobamos si son iguales
print(resultado)

#Oerador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

#Operador menor que
resultado = d < b
print(resultado)

#Operador menor o igual que
resultado = d <= b
print(resultado)

#Operador mayor o igual que
resultado = d >= b
print(resultado)


a = int(input("Digite un numeero: "))
print(f"El residuo de la division es: {a%2}")
if a % 2 == 0:
    print(f"EL valor de a es: {a} es un numero PAR")
else:
    print(f"El valor de a es: {a} es un numero IMPAR")


edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años,  usted es menor de edad")

# Operadores logicos
# Operador and
a = False
b = False
resultado = a and b
print(resultado)
# Operador or
resultado = a or b
print(resultado)
# Operador not
resultado = not a
print(resultado)

# Ejercicio: Valor dentro de un rango

valor = int(input("DIgite un numero dentro del rango del 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")


# Ejercicio con el Operador or, Operador not (este operador hace la contra a la logica real)

vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("TIene trabajo que hacer")

# Ejercicio: Rango entre las edades 20 y 30 años
edad = int(input("Digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)
#if veinte or treinta:
# if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
if (20 <= edad < 30) or (30 <= edad < 40):  # Sintanxis simpplificada del orperador and
    print("Estas dentro del rango de los (20'0) a (30'0) años")
#    if veinte:
#        print('Estas dentro del rango de los (20 \'0) años')
#    elif treinta:
#        print('Estas dentro del rango de los (30 \'0) años')
#    else:
#        print("NO estas dentro del rango")
else:
    print("NO estas dentro del rango de los (20'0) a (30'0) años")

# Ejercicio: El mayor de dos numeros
numero1 = int(input("Digite el valor para el numero 1: "))
numero2 = int(input("Digite el valor para el numero 2: "))
if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es el mayor")
'''
# Ejercicio: Tienda de libros
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el id del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el libro es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto debe escribir True/False"
print(f'''
           Nombre: {nombre}
           Id: {id}
           Precio: {precio}
           Envio Gratuito?: {envioGratuito}
''')