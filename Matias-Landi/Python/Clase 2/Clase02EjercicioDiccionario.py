#EjercicioDiccionario
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Datos'
}
print(len(diccionario))
print(diccionario)

print(diccionario['IDE'])
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves como al principio

for valor in diccionario.values():
    print(valor) #Muestra los valores sin las llaves

print('IDE' in diccionario)

diccionario['PK'] = 'Primary Key'
print(diccionario)

diccionario.pop('SABD')
print(diccionario)

diccionario.clear()
print(diccionario)

del diccionario

