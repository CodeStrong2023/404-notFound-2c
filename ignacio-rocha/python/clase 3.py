#repaso de set o conjunto
#para definir un conjunto
conjunto=set()
conjunto1={"bye",}
conjunto.add(7)
conjunto.add("hola")
print(conjunto)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el numero 3 no esta en el conjunto 

#como hacer la igualdad de dos conjuntos
print(conjunto1==conjunto)#nos devuelve como respuesta un booleano

#operaciones en conjuntos
conjunto3=conjunto | conjunto1 #la linea une los dos conjuntos
print(conjunto3)
conjunto3=conjunto-conjunto1
print(conjunto3)
conjunto3=conjunto ^ conjunto1 #elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3=conjunto | conjunto1
print(conjunto1.issubset(conjunto3)) #aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto.issubset(conjunto3))
print(conjunto3.issubset(conjunto))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto)) #preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto1))
print(conjunto1.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun

print(conjunto.isdisjoint(conjunto1)) #no hay cosas en comun

#convertir un conjunto totalmente en inmutable
conjunto=frozenset #esto hace que el conjunto sea totalmente inmutable
#no se puede agregar, modificar ni eliminar elementos

#repaso diccionarios
diccionarioNuevo={"azul":"blue","rojo":"red","verde":"green","amarillo":"yellow"}
print(diccionarioNuevo)

#como eliminar 
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

#los diccionarios pueden almacenar difererentes tipos de datos
diccionario2={"ariel":{"edad":40,"altura":1.83},"osvaldo":[45,1.85],"Natalia":[35,1.67]}

seleccionArgentina={
    10:{"nombre":"Lionel Messi","edad":35,"altura":1.70,"precio":"50 millones", "posicion":"extremo derecho"},
    11:{"nombre":"Angel Di Maria","edad":34,"altura":1.80,"precio":"12 millones","posicion":"extremo derecho"},
    24:{"nombre":"paulo dybala","edad":28,"altura":1.77,"precio":"35 millones","posicion":"media punta"},
    19:{"nombre":"Nicolas Otamendi","edad":34,"altura":1.83,"precio":"3.5 millones","posicion":"defensa central"},
    1:{"nombre":"Franco Armani", "edad":35,"altura":1.89,"precio":"3.5 millones","posicion":"portero"},

    27:{"nombre":"Julian Alvarez","edad":23,"altura":1.70,"precio":"18 millones", "posicion":"delantero"},
    7:{"nombre":"Lautaro Martinez","edad":29,"altura":1.80,"precio":"37 millones","posicion":"centrocampista"},
    22:{"nombre":"Lautaro Martinez","edad":26,"altura":1.74,"precio":"35 millones","posicion":"delantero"},
    17:{"nombre":"Alejandro Dario Gomez","edad":35,"altura":1.67,"precio":"3.5 millones","posicion":"centrocampista"},
    

}

print(seleccionArgentina)

for llave,valor in seleccionArgentina.items():
    print(llave,valor)

#como tarea agregar por lo menos 4 jugadores mas al diccionario seleccionArgentina
print("tenemos cargados en el diccionario la cantidad de : ",end=" ")
print(len(seleccionArgentina))


#pilas usando listas

pila=[1,2,3]

#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#sacamos elementos desde el final
#pila.pop()
#print(pila)

#sacamos elementos desde el final
elementoBorrado=pila.pop() #quita el ultimo elemento y lo guarda en la variable
print(f"sacamos el elemento {elementoBorrado}")
print(f"la pila ahora queda asi: {pila}")

#colas con listas
#estructura de datos de tipo fifo (first input/first output)

cola=["ariel","osvaldo","liliana","pilar"]

#agregamos elementos al final de la cola
cola.append("natalia")
cola.append("jose")
print(cola)

#sacamos elementos de la cola
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
