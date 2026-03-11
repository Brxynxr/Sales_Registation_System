# creamos una lista vacía donde se guardará toda la información de las ventas registradas
listaV = []

# creamos una función que se encarga de solicitar y almacenar la información de cada venta
def registroV(): 
    # Le preguntamos al usuario si desea registrar una venta
    venta = input("desea registrar una venta?: si/no ").lower()
    
    # El bucle se repetira mientras el usuario responda "si"
    while venta == "si":
        print("\n-----REGISTRO DE NUEVA VENTA-----\n")
        
        # Usamos try/except para evitar que el programa se rompa si el usuario ingresa datos incorrectos
        try:
            # Solicitamos los datos del producto
            nombre = input("ingrese el producto que desea comprar: ")
            precio = float(input("ingrese precio por unidad: "))
            cantidad = int(input("ingrese la cantidad de productos: "))
            
            # Creamos un diccionario con la información de la venta
            nuevaVenta = {
                "producto": nombre, 
                "cantidad": cantidad, 
                "subtotal": precio * cantidad
                }
            
            # Agregamos el diccionario a la lista de ventas
            listaV.append(nuevaVenta)
            
        # Si el usuario ingresa letras donde van números, capturamos el error
        except ValueError:
            print("Error: informacion invalida")
            
        # Preguntamos si desea registrar otra venta para continuar o salir del bucle
        venta = input("desea registrar otra venta?: si/no ").lower()


# función que recorre la lista y suma todos los subtotales para obtener el total general
def Ctotal():
    totalG = 0  # iniciamos el acumulador en 0
    
    # recorremos cada venta registrada en la lista
    for venta in listaV:
        totalG += venta["subtotal"]  # sumamos el subtotal de cada venta al acumulador
        
    return totalG  # retornamos el total calculado


# creamos una función que muestra en pantalla el resumen completo de todas las ventas
def resumen():
    print("\n-----RESUMEN DE VENTAS-----\n")
    
    # recorremos la lista e imprimimos los datos de cada venta
    for venta in listaV:
        print(f"producto: {venta['producto']}")
        print(f"cantidad: {venta['cantidad']}")
        print(f"subtotal: {venta['subtotal']}")
    
    # llamamos a Ctotal() para obtener la suma de todas las ventas
    total = Ctotal()
    print(f"\nTOTAL RECAUDADO: {total}\n")


# ---- EJECUCIÓN DEL PROGRAMA ----
registroV()
Ctotal()
resumen()