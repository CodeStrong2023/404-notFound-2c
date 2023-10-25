# ejercicio 4: calculadora de impuestos
# crear una funcion para calcular el total de un pago
# incluyendo un impuesto aplicado (IVA)
# formula: pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
# proporcione el pago sin impuesto:1000
# proporcione el monto del impuesto: 21%
# pago con impuesto: xxxxx

def calcular_total_pago(pago_sin_impuesto,impuesto):
    pago_total=pago_sin_impuesto+pago_sin_impuesto*(impuesto/100)
    return pago_total

#ejecutamos la funcion
pago_sin_impuesto=float(input("ingrese el pago sin impuestos: "))
impuesto=float(input("digite el monto del impuesto a aplicar: "))
pago_con_impuesto=calcular_total_pago(pago_sin_impuesto,impuesto)
print(f"el pago con impuesto es: {pago_con_impuesto}")