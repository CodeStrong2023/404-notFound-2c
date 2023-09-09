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
# Lo que podemos usar dentro de tuplas son: index, count, ler
# En se pgg_dg convertir de a lista y de lista a

