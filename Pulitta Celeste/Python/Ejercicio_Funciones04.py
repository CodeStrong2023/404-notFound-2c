# Ejercicio 4: Calculadora de impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago-total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
# Proporcione el pago sin impuestos : 1000
# Proporcione el pago del impuesto: 21%
# Pago con impuesto: xxxx
def calcular_total_pago(pago_sin_impuestos, impuesto ):
    pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
    return pago_total
pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto =calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuestos es: {pago_con_impuesto}')
