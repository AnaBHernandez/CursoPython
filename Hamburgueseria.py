inventario = 100
print(f"El inventario contiene {inventario} hamburguesas")

while inventario > 10:
    num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente? "))

    if num_hamburguesas > inventario or inventario == 10:
        print("No hay suficientes hamburguesas en el inventario")

    else:
        num_hamburguesas <= inventario
        inventario -= num_hamburguesas
        print(f"inventario restante: {inventario}. Hay que comprar mas hamburguesas")

inventario = 100
print(f"El inventario contiene {inventario} hamburgesas")
while inventario > 0:
    if inventario <= 10:
        print("Advertencia: El inventario está casi vacío.")
    num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente? "))
    if num_hamburguesas > inventario:
        print("No hay suficientes hamburguesas en stock. Solo hay", inventario, "hamburguesas disponibles.")
    else:
        inventario -= num_hamburguesas
        print(f"El cliente ha pedido {num_hamburguesas} hamburguesas. El inventario ahora tiene {inventario} hamburguesas.")