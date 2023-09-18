# COLECCIONES EN PYTHON

# Las listas se conocen en otros lenguajes como arreglos o vectores.

# lista = Ariel, Liliana, Natalia, Osvaldo.

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) # Solo muestra el índice 0 , 1 pero no el índice 2.

# Ir del inicio de la lista al índice (sin incluirlo):
print(nombres[ :3]) # Indices a mostrar 0, 1 y 2.

# Desde el índice indicado hasta el final:
print(nombres[1: ])

# Modificamos un valor.
nombres[0] = 'Natalia'
nombres[2] = 'Liliana'
print(nombres)

# Iterar nuestra lista:
for nombre in nombres: # nombre es singular, la lista es plural.
    print(nombre)
else:
    print('Se acabaron los elementos de la lista.')

# Preguntamos cuantos elementos tiene:
print(len(nombres)) # Len es una función que nos regresa la cantidad de elementos que contiene una lista.
# Le pasamos como parámetro la lista.

# Agregamos un elemento:
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un índice específico:
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Débora')
print(nombres)

# Eliminamos un elemento:
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento:
nombres.pop()
print(nombres)

# Eliminamos un índice específico:
del nombres[2] # del significa delete.
print(nombres)

# Eliminar, borrar o limpiar todos los elementos:
nombres.clear()
print(nombres)

# Eliminar la lista:
del nombres
# print(nombres) # Aquí muestra el error.


# Definimos una tupla:
cocina = ('cuchara', 'cutucuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis:
print(cocina[0])

# Mostrar de manera inversa:
print(cocina[-1])

# Acceder a un rango:
print(cocina[0:2])
# Ejemplo:
verduras = ('papa') # Sin la coma pasa a ser un elemento cadena de tipo string y deja de ser una tupla.
print(verduras)

# Recorremos los elementos de la tupla:
for cocinar in cocina: # Print está usando \n para saltos de líneas.
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de línea.

# Esta conversión de tupla a lista y de lista a tupla NO es una buena práctica de la programación.
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print("\n", cocina)

# En TUPLAS no se pueden utilizar las fuciones append, insert y remove.
# Si el programa necesitara modificarse usaremos una LISTA y si no queremos modificaciones usaremos una TUPLA.


# Eliminamos la tupla:
del cocina
# print(cocina) # Muestra el error.




# SET es una colección que no tiene un orden y no permite almacenar elementos duplicados o repetidos, no se puede modificar

# pero si se puede agregar o eliminar.
# No mantiene ningún índice, el orden es aleatorio.
# Set puede servir para evitar la repetición de datos en una base de datos. Ej(Documentos, patentes, etc.)

# Tipo Set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Usamos la función len = lenght significa largo

# Revisar si un elemento existe dentro de Set
print('Marte' in planetas)

# Revisar si un elemento no existe dentro de Set
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función para añadir en conjuntos
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta función ante un mal ingreso o inexistencia de elemento da error
print(planetas)

planetas.discard('Tierra') # Esta función discard no nos presenta ningún error
print(planetas)

# Limpiar Set o conjunto
planetas.clear()
print(planetas)

# Eliminar Set o conjunto
del planetas
# print(planetas)

# 'Maradona': 10 Un diccionario está compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}

# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una función para acceder al valor
    print(valor) # Muestra los valores sin las llaves

# Comprobar la existencia de algún elemento
print('IDE' in diccionario) # devuelve un booleano

# Comprobar la inexistencia de algún elemento
print('IDE' not in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Esta es una función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para saber en que índice está cada elemento
# print(lista3.index(0)) # Esto da error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner nuestra lista al revés
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento, en python es una función
lista3.sort() # Ordena siempre de manera ascendente
print(lista3)

# Para ordenar de manera descendente
lista3.sort(reverse=True)
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Preguntamos si está o no el elemento, responde en booleano
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla.


# Repaso de set o conjunto
# Para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 NO está en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Devuelve como respuesta un booleano.


# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en común los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 están dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto significa si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modifica ni eliminar elementos del conjunto.


# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)


seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 36, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo Derecho'},
    11: {'Nombre': 'Ángel Di María', 'Edad': 35, 'Altura': 1.80, 'Precio': '12 Millones', 'Posición': 'Extremo Izquierdo'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 29, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posición': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posición': 'Portero'},
    13: {'Nombre': 'Cristian Romero', 'Edad': 24, 'Altura': 1.83, 'Precio': '20 Millones', 'Posición': 'Defensa Central'},
    24: {'Nombre': 'Enzo Fernández', 'Edad': 22, 'Altura': 1.79, 'Precio': '120 Millones', 'Posición': 'Medio Centro'},
    9: {'Nombre': 'Julián Álvarez', 'Edad': 23, 'Altura': 1.77, 'Precio': '45 Millones', 'Posición': 'Delantero Centro'},
    4: {'Nombre': 'Gonzalo Montiel', 'Edad': 28, 'Altura': 1.75, 'Precio': '4.5 Millones', 'Posición': 'Lateral Derecho'},
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=" ")
print(len(seleccionArgentina))


# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBoraado = pila.pop() # Elimina el último elemento de nuestra lista. Saca y retorna
print(f'Sacamos el elemento {elementoBoraado}') # Quita el último elemento y lo asigna a la variable elementoBorado
print(f'La pila ahora queda así: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(cola)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")


