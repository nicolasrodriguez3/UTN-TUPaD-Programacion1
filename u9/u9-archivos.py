ARCHIVO = "productos.txt"


# Funciones auxiliares
def mostrar_producto(nombre, precio, cantidad):
    print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")


# 1. Crear archivo inicial con productos
def ejercicio1():
    try:
        with open(ARCHIVO, "x", encoding="utf-8") as archivo:
            archivo.write("lapicera,500,10\n")
            archivo.write("resaltadores,2500,5\n")
            archivo.write("regla,100,15\n")
        print("Archivo creado exitosamente.")
    except FileExistsError:
        print("El archivo ya existe, no se sobreescribe.")


# 2. Leer y mostrar productos
def ejercicio2():
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_lista = linea.strip().split(",")
            mostrar_producto(
                nombre=linea_lista[0],
                precio=linea_lista[1],
                cantidad=linea_lista[2],
            )


# 3. Agregar producto desde teclado
def ejercicio3(productos):
    nombre = input("Ingrese el nombre del producto: ").strip()

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: ").strip())
            if precio <= 0:
                print("Error: El precio debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: El precio debe ser un número.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: ").strip())
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo)

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print(f"Producto '{nombre}' agregado.")


# 4. Cargar productos en una lista de diccionarios
def ejercicio4():
    productos = []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            producto_list = linea.strip().split(",")

            nombre = producto_list[0]
            precio = float(producto_list[1])
            cantidad = int(producto_list[2])

            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
            }
            productos.append(producto)

    return productos


# 5. Buscar producto por nombre
def ejercicio5(productos):
    while True:
        input_usuario = (
            input("Nombre del producto (Enter para salir): ").strip().lower()
        )
        if input_usuario == "":
            break

        encontrado = False
        for producto in productos:
            if producto.get("nombre").lower() == input_usuario:
                mostrar_producto(**producto)
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")


# 6. Guardar productos actualizados
def ejercicio6(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(
                f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            )
    print("Cambios guardados correctamente.")


def main():
    ejercicio1()
    productos = ejercicio4()

    while True:
        print("\n--- Menú ---")
        print("1. Mostrar productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Salir")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            ejercicio2()
        elif opcion == "2":
            ejercicio5(productos)
        elif opcion == "3":
            while True:
                ejercicio3(productos)
                respuesta = (
                    input("¿Desea agregar otro producto? (s/n): ").strip().lower()
                )
                if respuesta not in ("s", "si"):
                    break
        elif opcion == "4":
            ejercicio6(productos)
            print("Gracias por usar el programa. Saludos!")
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 4.")


main()
