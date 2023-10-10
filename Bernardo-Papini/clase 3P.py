
conjunto=set()
conjunto1={"bye",}
conjunto.add(7)
conjunto.add("hola")
print(conjunto)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1)  

print(conjunto1==conjunto)

conjunto3=conjunto | conjunto1 
print(conjunto3)
conjunto3=conjunto-conjunto1
print(conjunto3)
conjunto3=conjunto ^ conjunto1
print(conjunto3)

conjunto3=conjunto | conjunto1
print(conjunto1.issubset(conjunto3))
print(conjunto.issubset(conjunto3))
print(conjunto3.issubset(conjunto))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto)) 
print(conjunto3.issuperset(conjunto1))
print(conjunto1.issuperset(conjunto3))


print(conjunto.isdisjoint(conjunto1))


conjunto=frozenset 

diccionarioNuevo={"azul":"blue","rojo":"red","verde":"green","amarillo":"yellow"}
print(diccionarioNuevo)

 
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)


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


print("tenemos cargados en el diccionario la cantidad de : ",end=" ")
print(len(seleccionArgentina))


pila=[1,2,3]

pila.append(4)
pila.append(5)
print(pila)


elementoBorrado=pila.pop() 
print(f"sacamos el elemento {elementoBorrado}")
print(f"la pila ahora queda asi: {pila}")


cola=["ariel","osvaldo","liliana","pilar"]


cola.append("natalia")
cola.append("jose")
print(cola)

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
