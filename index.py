#mensaje de bienvenida al iniciar el programa
 
print("""Bienvenido al sistema de validación de productos
=========================================================""")

#definicion de las variables

buli = False
PreUN = 0.0
cantp = 0

#ingresar el valor de las variables

while PreUN <= 0 or cantp <= 0:
   NombrePRodu = (input("ingrese el nombre del producto el cual quieras comprar: "))
   PreUN = float(input("ingrese el precio unitario del producto el cual quieras comprar: "))
   cantp = int(input("ingrese la cantidad de productos que desea agregar a su compra: "))

   while buli != True:
      descuento = float(input("ingrese el descuento que se le aplicara al producto(0-100): "))
      if descuento >= 0 and descuento <= 100:
          buli = True
       
   if PreUN <= 0 or cantp <= 0:
      print("Error ingrese precio y cantidad mayor a cero")

#calculo de el precio total sin aplicar el descuento

precioT = PreUN * cantp

#calculo de el precio total despues de aplicar el descuento

if descuento < 0 or descuento > 100:
   descuento = 0
if descuento > 0 and descuento < 100:
   DescuentoPost = precioT * descuento /100
   PREdes = precioT - DescuentoPost
else:
       PREdes = "no se aplico descuento"

#se imprimen los valores de la compra

print(f"""resumen de la compra
========================================================
    nombre del producto: {NombrePRodu}
    Precio del producto: {PreUN}$
    cantidad del producto: {cantp}
    precio total: {precioT}$
    descuento aplicado: {descuento}%
    precio total del producto despues de el descuento: {PREdes}""")


