def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE = 'Integrated Development Environment', PK = 'Primal Key')
listarTerminos(Nombre = 'Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones Recursivas

def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo
numeroFactorial = int(input('Digite el número para calcular el factorial: '))
resultado = factorial(numeroFactorial) # Lo hacemos en código duro
print(f'El factorial del número {numeroFactorial} es: {resultado}') # Tarea que el usuario ingrese el número para calcular el factorial