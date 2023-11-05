# Comenzamos con Funciones
#miFuncion() # No se puede llamar antes de definir una funcion
# Definimos una función
def miFuncion(): #Para identificar a la funcion utilizamos paréntesis
    print('Saludos a todos los alumnos de la Tecnicatura')
miFuncion() # Estamos llamando la función
miFuncion() # se puede llamar n cantidad de veces

# Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel','Betancud']
show(person[0], person[1])#Pasamos uno por uno los datos de la lisa a la función
show(*person)# Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ('Osvaldo', 'Giordanini')# desempaquetamos através de la tupla
show(*person2)
person3 = {'lastName': 'Lucero', 'name': 'Natalia'}
show(**person3)

numbers = [1, 2, 3, 4, 5]# Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break# Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se termino')
# list comprehension, lista de comprensión
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0]== 'p']# Esto regresa una nueva lista
print(alongP)

bottleC = [{'Name': 'Quilmes', 'Country': 'Arg'},
           {'Name': 'Corona', 'Country': 'Mx'},
           {'Name': 'Stella Artois', 'Country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['Country'] =='Arg']
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)

def mi_funcion2(Name, lastName):
    print('Saludos a todos los que ven através del canal de YouTube')
    print(f'Nombre: {Name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

# La palabra return en funciones
# Creamos ua función para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b= 0):# Le damos un valor por defaul
    return a + b
resultado = sumar2()
print(f'Resltado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22,40)}')

# Argumentos, variables en función
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela')

def listarTerminos(**terminos):# Lo mas usado es **kwars para recibir los argumentso
    for llave, valor in terminos.items(): # kwars significa: ke word argument
        print(f'{llave}: {valor}')

listarTerminos()# No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy key')
listarTerminos(nombre= 'Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11)# No es un objeto iterable
desplegarNombres((10, 11))# la convertimos a una tupla
desplegarNombres([22, 55])# La convertimos en una lista

#Función recursivas
def factorial(numero):
    if numero == 1:# caso base
       return 1
    else:
        return numero * factorial(numero-1)# Caso recursivo
numeroFactorial = int(input('Digite el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial)# Lo hacemos en cadigo duro
print(f'El factorial del número {numeroFactorial} es: {resultado}') #Tarea que el usuario ingrese el númemro para
