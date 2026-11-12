"""
Entrega Final curso "introducción a la programación con Python" comisión 26204
Usa como base el código de la preentrega con las modificaciones propuestas por Esteban, 
mas los requisitos para la entrega final avanzada
utilizando json para persistencia de datos con manejo de diccionarios, 
try/except para manejo de errores, funciones definidas por el usuario, 
colorama para mejorar la visualización de los mensajes, y match/case para el menú de opciones.

alumno:  Federico Pescio
"""
# modulos a utilizar
import json #se carga el modulo json para poder usarlo en el código
from colorama import Fore, Back, init #se carga el modulo colorama para poder usarlo en el código
init (autoreset=True) #inicializo colorama para que los colores se reinicien al final de cada print

#funciones definidas por el usuario
def actualizar():
    """funcion que guarda el diccionario de productos en el archivo json"""
    with open ("inventario_hillcoat.json","w") as archivo:
        json.dump(productos, archivo) #guardo el diccionario de productos en el archivo json  

def buscar_producto(producto_a_buscar): #uso una funcion para buscar un producto en la lista de productos, devuelve el producto si lo encuentra, sino devuelve False
    """funcion que busca un producto en la lista de productos"""
    for producto in productos:
        if producto["nombre"] == producto_a_buscar:
            return producto #Si encuentra el producto, devuelve el diccionario completo del producto, que ademas es evaluado como True  
    return False

# Programa principal

print(Fore.RED + Back.WHITE + "************************************************************************")
print(Fore.GREEN + Back.WHITE + "Bienvenido al sistema de inventario del almacén 'Abrigo de colina'      ")  #mensaje de saludo del almacen hillcoat :-)
print(Fore.RED + Back.WHITE + "************************************************************************")

productos= [] #inicializo la lista de productos, precios y categorias, se usara con diccionarios almacenar los datos de cada producto, precio y categoria
try: #la idea es que si el archivo json no existe, se cree uno nuevo y se inicialice la lista de productos vacia, si existe, se cargue la lista de productos desde el archivo
    with open ("inventario_hillcoat.json","r") as archivo: #abro el archivo json en modo lectura, 
        productos = json.load(archivo)
except FileNotFoundError: #si el archivo no existe, se crea uno nuevo y se inicializa la lista de productos vacia
    with open ("inventario_hillcoat.json","w") as archivo: #abro el archivo json en modo escritura, si no existe se crea uno nuevo
        json.dump(productos, archivo) #guardo la lista de productos vacia para crear el archivo  


while True: #el menu se despliega en un bucle hasta que el usuario elija salir
    print (Fore.RED + "\nElija la opcion deseada") 
    opcion = input ("\nA - Agregar productos\nM - Mostrar Productos\nB - Buscar productos\nE - Eliminar productos\nS - Salir\n\n").lower().strip() #opciones y almacenamiento de opcion elegida, almacena en minuscula
    
    match opcion:
        case "s":
            print(Back.BLACK + Fore.WHITE + "Gracias...vuelva pronto")
            break
       
        case "a":
            producto_agregar = input("\nIngrese producto a agregar: \n").title().strip()
            while producto_agregar == "": #bucle que no permite ingresar un producto vacio
                print(Fore.RED + "El nombre no puede estar vacío.")
                producto_agregar = input("\nIngrese producto a agregar: \n").title().strip()
            if buscar_producto(producto_agregar): #condicion que verifica si el producto ya existe en la lista
                print(Fore.RED + f"\n{producto_agregar} ya existe en la lista")
                respuesta = input("Desea agregarlo de todas formas? (S/N)").title().strip()
                if respuesta != "S": #si no quiere agregarlo, aviso y vuelvo al menu
                    print(Fore.RED + f"\n{producto_agregar} no se agrego a la lista")
                    continue #vuelve al menu principal
           
            precio_agregar = float(input("\nIngrese precio del producto: \n").strip())
            while precio_agregar <= 0: #bucle que no permite ingresar un precio negativo o cero
                print(Fore.RED + "El precio no puede ser negativo o cero.")
                precio_agregar = float(input("\nIngrese precio del producto: \n").strip())
            
            categoria_agregar = input("\nIngrese categoria del producto: \n").title().strip()
            while categoria_agregar == "": #bucle que no permite ingresar una categoria vacia
                print(Fore.RED + "La categoria no puede estar vacía.")
                categoria_agregar = input("\nIngrese categoria del producto: \n").title().strip()

            productos.append({"nombre":producto_agregar,"precio":precio_agregar,"categoria":categoria_agregar}) #agrego el producto, precio y categoria al diccionario
            actualizar() #llamo a la funcion actualizar para guardar los productos en el archivo
            print(f"\n{producto_agregar} agregado con exito.\n")
            
        case "e":
            if len(productos) ==0: #condicion si la lista está vacia
                print("no hay productos para eliminar")
            else:
                producto_eliminar = input("\nIngrese producto a eliminar: \n").title().strip()
                producto = buscar_producto(producto_eliminar) #llamo a la funcion buscar_producto para verificar si el producto existe en la lista, pero producto es el diccionario completo del producto 
                if producto: #si la funcion devuelve un diccionario no vacío (funciona como True), significa que el producto existe en la lista
                    productos.remove(producto) #borro el producto (diccionario completo) de la lista
                    actualizar()  #actualizo el archivo json.
                    print(f"{Fore.GREEN}\n{producto_eliminar} quitado con exito.")
                else:
                    print(f"{Fore.RED}\n{producto_eliminar} no está en la lista")

        case "m":
            if productos == []: #condicion si la lista está vacia
                print("\nNo hay productos en stock")
            else:
                print(Fore.GREEN + "\nProductos en stock:")
                for producto in productos:
                    print (f"Nombre: {producto["nombre"]}")
                    print (f"Precio: ${producto["precio"]}")
                    print (f"Categoria: {producto["categoria"]}")
                    print ("-----------------------------")
            
        case "b":
            producto_a_buscar = input("\nIngrese producto a buscar: \n").title().strip()
            if buscar_producto(producto_a_buscar): #llamo a la funcion buscar_producto para verificar si el producto existe en la lista
                print(f"{producto_a_buscar} esta en stock")
            else:
                print(f"\n{producto_a_buscar}, no esta en stock")
        
        case _:
            print ("\nLa opcion elegida no es válida")
        