# Almacenar los precios de tres productos diferentes
precio_vainilla = 600
precio_chocolate = 700
precio_batido = 1200

# Mostrar los precios almacenados
print("\nBienvenidos al sistema de pago POPS")
print("\n*********Menu*********")
print("Helado Vainilla: ¢", precio_vainilla)
print("Helado Chocolate: ¢", precio_chocolate)
print("Batido: ¢", precio_batido)
print("\n*************************")

print("\nPedido del Cliente")

cantidad_vainilla = int(input("Ingrese la cantidad de helados de Vainilla: "))
cantidad_chocolate = int(input("Ingrese la cantidad de helados de Chocolate: "))
cantidad_batido = int(input("Ingrese la cantidad de batidos: "))

print("\n*** La cuenta total del cliente es:")

total_vainilla = precio_vainilla * cantidad_vainilla
total_chocolate = precio_chocolate * cantidad_chocolate
total_batido = precio_batido * cantidad_batido

print("Total por helados de Vainilla: ¢", total_vainilla)
print("Total por helados de Chocolate: ¢", total_chocolate)
print("Total por batidos: ¢", total_batido)

total_final = total_vainilla + total_chocolate + total_batido
total_descuento= total_final*0.15
print("Total sin descuento: ¢", total_final)
print("Descuento PuraVidaPops: ¢", total_descuento)
print("Total a Pagar: ¢", total_final-total_descuento)


