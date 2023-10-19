#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye",}
conjunto2.add(7)
conjunto2.add("hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1)

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)#Nos devuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #La linea une los dos conjuntos
print(conjunto3)
conjunto3 = conjunto1 -conjunto2 #Que elementos tienen en común
print(conjunto3)
conjunto3 = conjunto2 -conjunto1
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2 #Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) #Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto2)) #Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto1))
print(conjunto1.issuperset(conjunto3))

#Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común

print(conjunto2.isdisjoint(conjunto1)) #No hay cosas en común

#Convertir un conjunto totalmente en inmutable
conjunto2 = frozenset #Esto hace que el conjunto sea totalmente inmutable
#No se puede agregar, modificar ni eliminar elementos

#Repaso diccionarios
diccionarioNuevo = {"azul":"blue","rojo":"red","verde":"green","amarillo":"yellow"}
print(diccionarioNuevo)

#como eliminar 
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar difererentes tipos de datos
diccionario2={"ariel":{"edad":40,"altura":1.83},"osvaldo":[45,1.85],"Natalia":[35,1.67]}

seleccionArgentina={
    10:{"Nombre":"Lionel Messi","Edad":36,"Altura":1.70,"Precio":"35 millones", "Posición":"Extremo derecho"},
    11:{"Nombre":"Angel Di Maria","Edad":35,"Altura":1.80,"Precio":"8 millones","Posición":"Extremo derecho"},
    21:{"Nombre":"Paulo Dybala","Edad":29,"Altura":1.77,"Precio":"30 millones","Posición":"Media punta"},
    19:{"Nombre":"Nicolas Otamendi","Edad":35,"Altura":1.83,"Precio":"2 millones","Posición":"Defensa central"},
    1:{"Nombre":"Franco Armani", "Edad":37,"Altura":1.89,"Precio":"1.5 millones","Posición":"Portero"},

    9:{"Nombre":"Julian Alvarez","Edad":23,"Altura":1.70,"Precio":"80 millones", "Posición":"Delantero"},
    25:{"Nombre":"Lisandro Martinez","Edad":25,"Altura":1.75,"Precio":"50 Millones","Posición":"Defensor central"},
    7:{"Nombre":"Rodrigo De Paul","edad":29,"Altura":1.80,"Precio":"40 millones","Posición":"Centrocampista"},
    13:{"Nombre":"Cristian Romero","edad":25,"altura":1.85,"precio":"60 millones","Posición":"Defensor central"},
}

print(seleccionArgentina)

for llave,valor in seleccionArgentina.items():
    print(llave,valor)

#Como tarea agregar por lo menos 4 jugadores mas al diccionario seleccionArgentina
print("Tenemos cargados en el diccionario la cantidad de jugadores : ",end=" ")
print(len(seleccionArgentina))


#Pilas usando listas

pila= [1, 2, 3,]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
#Pila.pop()
#Print(pila)

#Sacamos elementos desde el final
elementoBorrado=pila.pop() #Quita el ultimo elemento y lo guarda en la variable
print(f"sacamos el elemento {elementoBorrado}")
print(f"la pila ahora queda asi: {pila}")

#Colas con listas
#Estructura de datos de tipo fifo (first input/first output)

cola= ["Ariel", "Osvaldo", "Liliana", "Pilar", "Natalia", "Jose"]

#Agregamos elementos al final de la cola
print(cola)

#Sacamos elementos de la cola
seRetira=cola.pop()
print(f"atendido el cliente: {seRetira}")
print(cola)

seRetira=cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)

seRetira=cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)
seRetira=cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)
seRetira=cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)