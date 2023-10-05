def calcularTotalPago(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal

pagoSinImpuesto = float(input("Digite el pago sin impuesto: "))
impuesto = float(input("Digite el monto del impuesto a aplicar: "))
pagoConImpuesto = calcularTotalPago(pagoSinImpuesto, impuesto)

print(f"El pago con impuesto es {pagoConImpuesto}")