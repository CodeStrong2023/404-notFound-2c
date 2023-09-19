"""
ejercicio 4: sumar numeros pares dentro de un rango
hcaer un programa para sumar numeros pares dentro
de un rango, por ejemplo:
                        suma de numeros pares del 2 al 30
                        suma=240


a=int(input("digite de donde va a comenzar la suma: "))
b=int(input("digite hasta donde quiere llegar a sumar: "))
suma=0
for i in range(a,b+1):
    if i%2==0: #esto es si el numero es par
        suma+=i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
"""
"""
ejercicio 5: factorial de un numero positivo
hacer un programa para calcular el factorial de un numero positivo

numero=int(input("ingrese un numero: "))
while numero<0: #mientras el numero sea negativo
    print("error -> el numero tiene que ser positivo ")
    numero=int(input("ingrese un numero: "))
factorial=0#la variable para calcular el factorial
for i in range(1,numero +1):
    factorial*=i
print(f"\nEl factorial del numero {numero} positivo ingresado es {factorial}")

print("comenzamos con funciones ")
#mi_funcion() #no se puede llamar antes de definir a una funcion
#definimos una funcion
def mi_funcion(): #para identificar a la funcion utilizamos parentesis
    print("saludos a todos los alumnos de la tecnicatura")

mi_funcion() #estamos llamando a la funcion
mi_funcion()
"""
"""
ejercicio 6: tabla de multiplicar
hacer un programa que pida un numero por teclado y guarde en una lista su tabla de
multipicar hasta el 10. por ejemplo: si digita el 5, la lista sera: 5,10,15,20,25,30,35,40,45,50



numero=int(input("digite un numero: "))
lista=[] #creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
print(f"\nTabla de multiplicar del {numero}: \n{lista}")

for indice,i in enumerate(lista):
    print(f"{numero} x {i} = {lista[indice]}")#este ciclo es para ver el formato de una tabla de multiplicar


"""
"""
#Ejercicio 7: juego adivina el numero
#realizar un juego para adivinar un numero, para ello se debe generar un numero aleatorio entre 1- 100, y luego ir pidiendo
numeros indicado "es mayor" o "es menor" segun sea mayor o menor con respecto a N. el proceso termina cuando el usuario 
acierta y alli se debe mostrar el nuero de intentos.



import random
aleatorio=random.randint(0,100)#toma de 0 a 100, generamos un numero aleatorio
contador=0
while True:
    numero=int(input("ingrese un numero: "))
    contador+=1
    if numero>aleatorio:
        print("\tNo es el numero, digite un numero menor")
    elif numero<aleatorio:
        print("\tNo es el numero digite un numero mayor")
    else:
        print(f"Felicidades, acabas de adivinar el numero { aleatorio}")
        break #rompe el ciclo y el bucle

print(f"\nNumero de intentos : {contador}")
"""
"""
Ejercicio 8: menu interactivo - cajero automatico
hacer un programa que simule un cajero automatico con un saldo
inicial de 1000 pesos y tendra el siguiente menu de opciones:
1)ingresar dinero a la cuenta
2)retirar dinero de la cuenta
3)mostrar dinero disponible
4)salir

saldo=1000
while True:
    print("\t.:Menu:.")
 print("1:ingresar dinero a la cuenta: ")
    print("1- retirar dinero de la cuenta")
    print("4-mostrar dinero dispoble")
    opcion=int(input("digite una opcion de menu"))
    print()
    if opcion==1:
        extra=float(input("cuanto dinero desea ingresar->))
        saldo+=resta
        print(f"dinero en la cuenta al momento ${saldo})
    elif opcion==2:"
        retirar = float(input(cuanto de dinero desea retirrar->)))
        if retirar >saldo:
            print("no tiene esa cantidad de dinero")
        else:
            saldo-=retirar
            print(f"dinero en la cuota )
    elif opcion==3:
        print(f"diinero en la cuenta al momento: ${saldo})        
    elif(opcion==4):
        print("gracias por utilizar su cajero automatico, hasta pronto")
    else:
        print("gracias, se equivoco de opcion de menu")        
        
        
        
        """

"""
ejercicio 9: mostrar una frase sin espacios y contar su longitud
hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase 
pero sin espacios en blanco, y ademas un contador de cuentos caracteres tiene la frase 
(sin contar los espcios)
ejemplo: frase=vivir por siempre en paz
         frase final= vivirporsuerteenpaz
         nroCacteres=70

         
frase 1=input("digite una frase")
frase2=""
for i in range1:
    if i!=" " :
        frase2+-1
frase1=frase2
print(f"\nFrase final: {frase1}")
print(f"numeros de caractes: {len(frase1)}")
"""




