nombres = ['Nagy', 'Osvaldo', 'Lily', 'Ariel']
"""print(nombres)
print( nombres[0])
print( nombres[1])
print( nombres[3])
print( nombres [-1])
print( nombres[-2])"""

print (nombres)
print (nombres [0:2])

print (nombres [0:3])

print (nombres [1: ])
nombres[2]="liliana"
nombres[0]="natalia"
print(nombres)

for nombre in nombres:
    print(nombre)
else: print("se acabaron los nombres")

print(len(nombres))
nombres.append("marcelo")
nombres.append([1, 2, 3])
nombres.append( True )
nombres.append( 10.45 )
nombres.append([14, 5])
nombres.append(7)
print(nombres)

nombres.insert(1,"alverto")
print(nombres)
nombres.insert(3,"debora")
print(nombres)

nombres.remove("alverto")
print(nombres)

nombres.pop()
print(nombres)

del nombres[2]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombre)
#definimos un tupla
cocina=("cuchara","cuchillo","tenedor")
print(len(cocina))

print(cocina[0])
print(cocina[0:1])

verdura=("papa",)

for cocinar in cocina:
    print(cocinar, end=" ")

cocinalit=list(cocina)
cocinalit[0]="plato"
cocina=tuple(cocinalit)
print("\n",cocina)

#tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))

print ('Júpiter' in planetas)
planetas.add("Tierra")
print(planetas)
#eliminar elementos peno esten en la lista arroja error
planetas.remove("Marte")
print(planetas)
planetas.discard("Tierra")
print(planetas)

planetas.clear()
print(planetas)

del planetas
#print(planetas)

diccionario = {
    "IDE": "Integrated Development Environment",
    "POO":'Programacion Orientada a Objetos',
    "SABD":"Sistema de administracion de base de datos",
}
print(len(diccionario))
print(diccionario)

print(diccionario["IDE"])
# Otra forma de un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = ' Enterne de Integrado'
print(diccionario)
# como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una función para un
for termino, valor in diccionario.items():
    print(termino, valor)

# maneras de acceder a un diççiqoarip
for termino in diccionario.keys(): # usando una función
    print(termino) # Muestra solo las llaves
for valor in diccionario.values():  # us_amps una función para acceder al valor
    print(valor)

# la existencia de algun
print('IDE' in diccionario)# devuelve un booleano

# Agregar un elemento
diccionario["PK"]='Primary key'
print(diccionario)

# Eliminar un el gntg
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario#el diccionario se borro

# Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2 #Concatenamos
print(lista3)

lista3.extend([7, 8, 9,1]) #Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))#Función para en que esta el valor
# print(lista3.index(0)) # esto daria un error por nos ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay de una lista
print(lista3.count(1))# Cuenta cuantos valores hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una usta se multiplique sus elementos
lista3= lista3 * 2
print(lista3)

# Método de ordenamiento, en python es una funció
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort( reverse=True)# Ordena descendentemente
print(lista3)

#repaso de tuplas
tupla = (4,"hola",6.78, [1, 2, 78], 4,'Hola')# Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)#Acción booleana, su respuesta es de tipo booleana

conjunto1 = set() # Con el set y los parentesis el conjunto se puede iniciar vacio.
conjunto2 = {"bye"}

conjunto1.add(7)
conjunto1.add("Hola")
print(conjunto1)

conjunto2.add("hola")
print(conjunto2)

# Preguntamos si el 3 no esta en el conjunto1.
print(3 not in conjunto1)

# Como hacer la igualdad de dos conjuntos.
print(conjunto1 == conjunto2)

# Operaciones en conjunto.
conjunto3 = conjunto1 | conjunto2 # Con la linea entre los conjuntos hace que los dos se unan.
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Guardara en el conjunto3 el elemento que tengan en común el conjunto1 y 2
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2.
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferente entre ambos.
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Preguntamos si un conjunto es subconjunto dentro de otro.
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto1)) # conjunto3 es un super conjunto del conjunto1 porque contiene todos sus elementos.
print(conjunto3.issuperset(conjunto2))
print(conjunto1.issuperset(conjunto3))

# Preguntamos si ambos conjuntos son disconexos, esto si no comparten elementos en comun.
print(conjunto1.isdisjoint(conjunto2)) # true = no hay elementos en comun.

# Convertir un conjunto totalmente en inmutable.
conjunto1 = frozenset
#repaso diccionarios
diccionarioNuevo={"azul":"blue","rojo":"red","verde":"green","amarillo":"yellow"}
print(diccionarioNuevo)

#como eliminar
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

#los diccionarios pueden almacenar difererentes tipos de datos
diccionario2={"ariel":{"edad":40,"altura":1.83},"osvaldo":[45,1.85],"Natalia":[35,1.67]}
print(diccionario2)

seleccionArgentina={
    10:{"nombre":"Lionel Messi","edad":35,"altura":1.70,"precio":"50 millones", "posicion":"extremo derecho"},
    11:{"nombre":"Angel Di Maria","edad":34,"altura":1.80,"precio":"12 millones","posicion":"extremo derecho"},
    24:{"nombre":"paulo dybala","edad":28,"altura":1.77,"precio":"35 millones","posicion":"media punta"},
    19:{"nombre":"Nicolas Otamendi","edad":34,"altura":1.83,"precio":"3.5 millones","posicion":"defensa central"},
    1:{"nombre":"Franco Armani", "edad":35,"altura":1.89,"precio":"3.5 millones","posicion":"portero"},

    7: {"nombre": "Lautaro Martinez", "edad": 29, "altura": 1.80, "precio": "37 millones","posicion": "centrocampista"},
    22: {"nombre": "Lautaro Martinez", "edad": 26, "altura": 1.74, "precio": "35 millones", "posicion": "delantero"},
    17: {"Nombre": "Alejandro Gomez", "Edad": 35, "Altura": 1.67, "Precio": "10 Millones", "Posicion": "Centrocampista"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print("Tenemos cargados en el diccionario la cantidad de jugadores:", end=" ")
print(len(seleccionArgentina))

# Pila usando listas
pila = [1, 2, 3]

# En pilas se trabaja siempre con el último elemento.
# Agregar elementos a la pila por el final.
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final.
elementoQuitado = pila.pop()
print(f"Quitamos el elemento {elementoQuitado}")
print(f"Ahora la pila queda así {pila}")

# Cola con listar.
# Estructura de datos de tipo fifo(first input / first output)
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]

# Agregamos elementos al final de la cola.
cola.append("Natalia")
cola.append("José")
print(cola)

# Sacamos elmentos de la cola.
seRetira = cola.pop(0)
print(f"Atendido el cliente:  {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente:  {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente:  {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente:  {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente:  {seRetira}")
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")