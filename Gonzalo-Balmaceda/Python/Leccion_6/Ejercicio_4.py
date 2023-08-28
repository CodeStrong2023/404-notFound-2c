# Ejercicio 4: Etapas de vida

edad = int(input("Ingrese su edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = "La infacia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
else:
    print("Error, etapa de vida no reconocida")

print(f'Tu edad es {edad}, {mensaje}')