if __name__ == '__main__':

    productos = [["Pan", 60], ["Chiles", 50],["Frijoles",20], ["Platanos", 58]]
    salir = False
    opc : int = 0
    nombre : str
    cantidad : int
    while salir == False:
        print("1. Agregar producto  2. Mostrar inventario   3. Vender producto   4. Salir")
        opc = int(input("Seleccione una opcion  "))
        match opc:
            case 1 :
                validacion = False
                nombre = input("Cual es el producto?  ")
                cantidad = int(input("Cual es el total?  "))

                for producto in productos:
                    if producto[0] == nombre:
                        producto[1] += cantidad
                        print(f"Fue aumentada la cantidad del producto: {nombre}")
                        validacion = True

                if not validacion:
                    nuevo_Producto = {cantidad, nombre}
                    productos.append(nuevo_Producto)
                    print("Se agrego un nuevo producto")
            case 2:
                print("*****Productos*****")
                for fila in productos:
                     print(fila)
            case 3:
                conteo = 0
                nombre_venta = input("Cual es el producto?  ")
                cantidad_venta = int(input("Cuanto quieres comprar?  "))
                validacion = False
                for producto in productos:

                    if producto[0] == nombre_venta:
                        validacion = True
                        if producto[1] >= cantidad_venta:
                            producto[1] -= cantidad_venta
                            print(f"Se vendio el producto: {nombre_venta}")
                            if producto[1]==0:
                                productos.pop(conteo)
                        else:
                            print("Sobrepasa la cantidad del inventario")
                    conteo += 1
                if not validacion:
                    print("No se encontro el producto")


            case 4:
                salir = True