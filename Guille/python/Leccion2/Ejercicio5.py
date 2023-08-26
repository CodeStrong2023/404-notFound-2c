nota = int(input("Digite su calificacion (de 0 a 10): "))
if 0 <= nota < 6:
    print(f"Su calificacion es: {nota}, E")
elif 6 <= nota < 7:
    print(f"Su calificacion es: {nota}, D")
elif 7 <= nota < 8:
    print(f"Su calificaion es: {nota}, C")
elif 8 <= nota < 9:
    print(f"Su calificacion es: {nota}, B")
elif 9 <= nota <= 10:
    print(f"Su calificacion es: {nota}, A")
else:
    print("EL Valor ingresado es incorrecto")

