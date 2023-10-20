# Desempaquetado de listas o list Unpacking

def show(name, lastName):
    print(name+' '+lastName)
person = ['Matias', 'Landi']
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista de la función
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ('Osvaldo', 'Giordanini') # Desempaquetamos a través de una tupla
show(*person2)
person3 = {'lastName': 'Lucero', 'name': 'Natalia'}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacía se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la única manera para que no se ejecute el else
else:
    print('Esto se termina')

# List comprehension, lista de comprensión

names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{'name': 'Quilmes', 'country': 'Arg'},
           {'name': 'Corona', 'country': 'Mx'},
           {'name': 'Stella Artois', 'country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['country'] == 'Arg']
print(Arg)
print(bottleC)

# Paso de argumentos (funciones)

def mi_funcion2(name, lastName):
    print('Saludos a todos los que ven a través del canal de YouTube')
    print(f'Nombre: {name}, Apellido, {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Matias', 'Landi')

# La palabra return en funciones
# Creamos una función para sumar

def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resludado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones

def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudio', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')