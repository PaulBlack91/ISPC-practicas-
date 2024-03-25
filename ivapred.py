montoProducto = int(input("ingrese el monto del producto:"))
iva = int(input('ingrese el porcentaje a cobrar:'))

total = montoProducto * iva / 100 + montoProducto

print(total) 