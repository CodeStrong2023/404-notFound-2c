# Ejercicio 9: mostrar una frase sin espacios y contar su longitud
# hacer un programa donde el usuario ingrese una frase, se le
# devolvera la misma frase pero sin espacios en blanco, y
# ademas un contador de cuantos caracteres tiene la frase
# (sin contar los espacios en blanco)
# ejemplo:          frase= vivir por siempre en paz
#                   frase final= vivir porsiempreenpaz
#                   Nro de caracteres= 20

frase = input("Ingrese una frase: ")

frase_sin_espacios = frase.replace(" ", "")

longitud_sin_espacios = len(frase_sin_espacios)
print(f"Frase inicial: {frase}")
print("Frase final:", frase_sin_espacios)
print("Número de caracteres (sin contar espacios):", longitud_sin_espacios)
# Ahun me sigo preguntado por que al profesor le salio 21 letras
