# *********************************************************
# Funciones auxiliares
# *********************************************************
def normalizar_nombre(nombre):
    """Normaliza el nombre de un producto eliminando espacios y convirtiendo a minúsculas."""
    return nombre.strip().lower()


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre en el inventario. Devuelve el artículo si se encuentra, o None si no."""
    nombre_normalizado = normalizar_nombre(nombre)
    for articulo in inventario:
        if normalizar_nombre(articulo["herramienta"]) == nombre_normalizado:
            return articulo
    return None


def buscar_articulos_similares(inventario, nombre):
    """Busca artículos con nombres que incluyan al nombre dado. Devuelve una lista de artículos similares."""
    nombre_normalizado = normalizar_nombre(nombre)
    similares = []
    for articulo in inventario:
        if nombre_normalizado in normalizar_nombre(articulo["herramienta"]):
            similares.append(articulo)
    return similares


def pedir_entero(mensaje, minimo=0):
    """Solicita un entero al usuario con validación básica."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"🚫 Error: El valor debe ser >= {minimo}. Ingresá de nuevo.")
            else:
                return valor
        except ValueError:
            print("🚫 Error: Entrada inválida. Ingresá un número entero.")


def texto_unidad(cantidad):
    """Devuelve 'unidad' si la cantidad es 1, o 'unidades' en caso contrario."""
    return "unidad" if cantidad == 1 else "unidades"


def mostrar_tabla(productos, incluir_cantidad=True):
    """
    Muestra una tabla con los productos y sus cantidades. Si incluir_cantidad es False, muestra solo los nombres de los productos.
    """
    if not productos:
        print("\nNo se encontraron productos.")
        return

    ancho_nombre = max(len(articulo["herramienta"]) for articulo in productos)
    ancho_nombre = max(ancho_nombre, len("Producto")) + 2
    separador = f" {'-' * (ancho_nombre + 4)}{'-' * (13 if incluir_cantidad else 0)} "

    print(separador)
    if incluir_cantidad:
        print(f" | {'Producto':<{ancho_nombre}} | {'Cantidad':>10} | ")
    else:
        print(f" | {'Productos':<{ancho_nombre}} | ")
    print(separador)

    if incluir_cantidad:
        for articulo in productos:
            print(
                f" | {articulo['herramienta']:<{ancho_nombre}} | {articulo['cantidad']:>10} | "
            )
    else:
        for articulo in productos:
            print(f" | {articulo['herramienta']:<{ancho_nombre}} | ")

    print(separador)


# Registrar venta
def registrar_venta(inventario):
    """Permite al usuario registrar una venta, disminuyendo el stock del producto vendido."""
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    while True:
        nombre = input("\nIngrese el nombre del producto a vender: ").strip()
        if not nombre:
            print("Operación cancelada.")
            return

        producto = buscar_producto(inventario, nombre)
        if not producto:
            print(f"Producto '{nombre}' no encontrado en el inventario.")
            similares = buscar_articulos_similares(inventario, nombre)
            if similares:
                print(f"Productos con nombres similares:")
                for producto in similares:
                    unidad = texto_unidad(producto["cantidad"])
                    print(
                        f"- {producto['herramienta']} ({producto['cantidad']} {unidad})"
                    )

            continue
        elif producto["cantidad"] == 0:
            print(
                f"🚫 Error: Producto '{producto['herramienta']}' está agotado. No se puede vender."
            )
            return

        break

    while True:
        try:
            cantidad = input(
                f"Cantidad a vender de '{producto['herramienta']}' (pulse enter para cancelar): "
            ).strip()
            if not cantidad:
                print("Operación cancelada.")
                return

            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            elif cantidad > producto["cantidad"]:
                unidad = texto_unidad(producto["cantidad"])
                raise ValueError(
                    f"No hay suficiente stock. Stock disponible: {producto['cantidad']} {unidad}."
                )
            break
        except ValueError as e:
            print(f"🚫 Error: {e}")

    producto["cantidad"] -= cantidad
    unidad = texto_unidad(producto["cantidad"])
    print(f"Venta registrada. Stock de '{nombre}': {producto['cantidad']} {unidad}")


# Registrar ingreso
def registrar_ingreso(inventario):
    """Permite al usuario registrar un ingreso, aumentando el stock del producto ingresado."""
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    while True:
        nombre = input("Ingrese el nombre del producto a ingresar: ").strip()
        if not nombre:
            print("Operación cancelada.")
            return

        producto = buscar_producto(inventario, nombre)
        if not producto:
            print(f"Producto '{nombre}' no encontrado en el inventario.")
            similares = buscar_articulos_similares(inventario, nombre)
            if similares:
                print(f"Productos con nombres similares:")
                for producto in similares:
                    unidad = texto_unidad(producto["cantidad"])
                    print(
                        f"- {producto['herramienta']} ({producto['cantidad']} {unidad})"
                    )

            continue
        break

    while True:
        cantidad = input(f"Cantidad a ingresar de '{producto['herramienta']}': ")

        if not cantidad:
            print("Operación cancelada.")
            return

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            break
        except ValueError as e:
            print(f"🚫 Error: {e}")

    producto["cantidad"] += cantidad
    unidad = texto_unidad(producto["cantidad"])
    print(f"Ingreso registrado. Stock de '{nombre}': {producto['cantidad']} {unidad}")


# *********************************************************
# Funciones principales
# *********************************************************
# Opción 1: Carga inicial de productos
def cargar_productos(inventario):
    """
    Carga los productos iniciales del inventario.
    """
    if inventario:
        print("Ya hay herramientas cargadas. Usá la opción 5 para agregar.")
        return

    cantidad = pedir_entero("¿Cuántas herramientas desea cargar? ", minimo=1)

    cargados = 0
    while cargados < cantidad:
        try:
            if cantidad > 1:
                herramienta = input(
                    f"Nombre del producto {cargados + 1}/{cantidad}: "
                ).strip()
            else:
                herramienta = input("Nombre del producto: ").strip()
            if not herramienta:
                raise ValueError("El nombre no puede estar vacío.")
            if buscar_producto(inventario, herramienta):
                raise ValueError(f"'{herramienta}' ya existe en el inventario.")

            stock = pedir_entero(f"Stock de {herramienta}: ")

            inventario.append(
                {
                    "herramienta": herramienta,
                    "cantidad": stock,
                }
            )
            cargados += 1

        except ValueError as e:
            print(f"🚫 Error: {e}")


# Opción 2: Ver inventario
def mostrar_inventario(inventario):
    """
    Muestra el inventario completo con formato legible.
    """
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    mostrar_tabla(inventario)


# Opción 3: Consultar stock
def consultar_stock(inventario):
    """
    Permite al usuario consultar el stock de un producto específico.
    """
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    while True:
        nombre = input("\nIngrese el nombre del producto a consultar: ").strip()
        producto = buscar_producto(inventario, nombre)
        if producto:
            unidad = texto_unidad(producto["cantidad"])
            print(
                f"Stock de '{producto['herramienta']}': {producto['cantidad']} {unidad}"
            )

        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")
            similares = buscar_articulos_similares(inventario, nombre)
            if similares:
                print(f"Productos con nombres similares:")
                for producto in similares:
                    unidad = texto_unidad(producto["cantidad"])
                    print(
                        f"- {producto['herramienta']} ({producto['cantidad']} {unidad})"
                    )

        respuesta = input("\n¿Desea consultar otro producto? (s/n): ").strip().lower()
        if respuesta != "s":
            break


# Opción 4: Reporte de productos agotados
def reporte_agotados(inventario):
    """Genera un reporte de productos que están agotados (cantidad 0)."""
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    agotados = [articulo for articulo in inventario if articulo["cantidad"] == 0]
    if agotados:
        print("\nProductos agotados:")
        mostrar_tabla(agotados, incluir_cantidad=False)
    else:
        print("No hay productos agotados.")


# Opción 5: Alta de nuevo producto
def alta_producto(inventario):
    """
    Permite al usuario agregar un nuevo producto al inventario.
    """
    try:
        nombre = input("\nNombre del nuevo producto: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if buscar_producto(inventario, nombre):
            raise ValueError(f"'{nombre}' ya existe en el inventario.")

        stock = pedir_entero(f"Stock de {nombre}: ")

        inventario.append(
            {
                "herramienta": nombre,
                "cantidad": stock,
            }
        )
        print(f"Producto '{nombre}' agregado al inventario.")

    except ValueError as e:
        print(f"🚫 Error: {e}")


# Opción 6: Registrar venta/ingreso
def actualizacion_stock(inventario):
    """Permite al usuario elegir entre registrar una venta o un ingreso para actualizar el stock de un producto."""
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    while True:
        print("1. Registrar venta")
        print("2. Registrar ingreso")
        print("3. Volver al menú principal")

        try:
            sub_opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("🚫 Error: Por favor, ingrese un número válido.")
            continue

        if sub_opcion == 1:
            registrar_venta(inventario)
        elif sub_opcion == 2:
            registrar_ingreso(inventario)
        elif sub_opcion == 3:
            break
        else:
            print("🚫 Error: Opción inválida. Por favor, seleccione 1, 2 o 3.")


# *********************************************************
# Menú principal
# *********************************************************
def main():
    inventario = [] # Lista de diccionarios [{"herramienta": str, "cantidad": int},]

    while True:
        print("\n~~~~~~~~~ Sistema de Control de Inventario ~~~~~~~~~")
        print("""
1. Carga inicial de productos
2. Ver inventario
3. Consultar stock de un producto
4. Reporte de productos agotados
5. Alta de nuevo producto
6. Registrar venta/ingreso
7. Salir
""")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("🚫 Error: Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            cargar_productos(inventario)
        elif opcion == 2:
            mostrar_inventario(inventario)
        elif opcion == 3:
            consultar_stock(inventario)
        elif opcion == 4:
            reporte_agotados(inventario)
        elif opcion == 5:
            alta_producto(inventario)
        elif opcion == 6:
            actualizacion_stock(inventario)
        elif opcion == 7:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print(
                "🚫 Error: Opción inválida. Por favor, seleccione un número entre 1 y 7."
            )


# Inicio del programa
main()
