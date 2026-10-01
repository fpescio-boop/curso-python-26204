#preentrega curso "introducción a la programación con Python" comisión 26204
#alumno:  Federico Pescio

print("************************************************************************")
print("Bienvenido al sistema de control de stock del almacén 'Abrigo de colina'")  #mensaje de saludo del almacen hillcoat :-)
print("************************************************************************")

productos = ["Yerba", "Azucar", "Arroz"] #inicializa el stock de productos, podria dejarlo vacio para empezar

while True: #el menu se despliega en un bucle hasta que el usuario elija salir
    print ("\nElija la opcion deseada") 
    opcion = input ("\nA - Agregar productos\nM - Mostrar Productos\nB - Buscar productos\nE - Eliminar productos\nS - Salir\n\n").lower().strip() #opciones y almacenamiento de opcion elegida, almacena en minuscula

    match opcion:
        case "s":
            print("Gracias...vuelva pronto")
            break
       
        case "a":
            producto_agregar = input("\nIngrese producto a agregar: \n").title().strip()
            while producto_agregar == "": #bucle que no permite ingresar un producto vacio
                print("El nombre no puede estar vacío.")
                producto_agregar = input("\nIngrese producto a agregar: \n").title().strip()
            productos.append(producto_agregar)
            print(f"\n{producto_agregar} agregado con exito.\n")
            
        case "e":
            if len(productos) ==0: #condicion si la lista está vacia
                print("no hay productos para eliminar")
            else:
                producto_eliminar = input("\nIngrese producto a eliminar: \n").title().strip()
                if producto_eliminar in productos:
                    productos.remove(producto_eliminar)
                    print(f"\n{producto_eliminar} quitado con exito.")
                else:
                    print(f"\n{producto_eliminar} no está en la lista")
        case "m":
            i = 1 #inicio contador
            for producto in productos:
                print (f"{i} - {producto}")
                i = i+1
            
        case "b":
            producto_a_buscar = input("\nIngrese producto a buscar: \n").title().strip()
            if producto_a_buscar in productos:
                print(f"{producto_a_buscar} esta en stock")
            else:
                print(f"\n{producto_a_buscar}, no esta en stock")
        
        case _:
            print ("\nLa opcion elegida no es válida")
        