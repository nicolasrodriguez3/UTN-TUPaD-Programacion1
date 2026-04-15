# Link al video
# https://youtu.be/cKWycDwmFrM

# Configuraciones
OPCIONES_VALIDAS = [1, 2, 3, 4, 5, 6, 7, 8]

# Almacenamiento de datos
herramientas = []
existencias = []


while True:
    # Menú
    print(
        f"""
{" Menú ".center(38, "~")}

1) Carga Inicial de Herramientas
2) Carga de Existencias
3) Ver Inventario
4) Consulta de Stock
5) Reporte de Agotados
6) Alta de Nuevo Producto
7) Actualización de Stock (Venta/Ingreso)
8) Salir
"""
    )
    opcion = input("Ingrese una opción: ").strip()

    if not opcion.isdigit() or int(opcion) not in OPCIONES_VALIDAS:
        print("Error: la opción ingresada no es válida")
        continue

    opcion = int(opcion)
    match opcion:
        case 1:
            # 1) Carga Inicial de Herramientas
            print(" Carga inicial ".center(38, "~"))

            while True:
                herramientas_a_cargar = input(
                    "Ingrese la cantidad de herramientas a cargar: "
                ).strip()

                if not herramientas_a_cargar.isdigit():
                    print("Error: El valor ingresado debe ser un número.")
                    continue

                herramientas_a_cargar = int(herramientas_a_cargar)
                if herramientas_a_cargar < 1:
                    print("Error: el número ingresado debe ser mayor o igual a 1.")
                    continue

                # Si llegamos a este punto el número es correcto
                break

            for i in range(herramientas_a_cargar):
                while True:
                    nombre_herramienta = input(
                        f"Ingrese el nombre de la herramienta {i + 1}: "
                    ).strip()

                    if not nombre_herramienta:
                        print("Error: el nombre no puede estar vacio.")
                    elif nombre_herramienta in herramientas:
                        print("Error: la herramienta ya existe en el listado.")
                    else:
                        # Agregar herramienta y stock para mantener sincronizados las listas
                        herramientas.append(nombre_herramienta)
                        existencias.append(0)
                        break

            print(
                f"""
Carga finalizada. 
{herramientas_a_cargar} herramienta/s cargada/s
Total de herramientas: {len(herramientas)}
"""
            )

        case 2:
            # 2) Carga de Existencias
            # Verificar que haya herramientas cargadas
            if not herramientas:
                print(
                    "No hay herramientas cargadas. Realice la carga inicial en la opción < 1 >."
                )
            else:
                print(" Carga de existencias ".center(38, "~"))

                for i in range(len(herramientas)):
                    while True:
                        existencia = input(
                            f"Ingrese el stock para {herramientas[i]}: "
                        ).strip()

                        if not existencia.isdigit():
                            print(
                                "Error: El valor ingresado debe ser un número positivo."
                            )
                            continue

                        existencia = int(existencia)
                        existencias[i] = existencia
                        break

        case 3:
            # 3) Ver Inventario
            # Verificar que haya herramientas cargadas
            if not herramientas:
                print(
                    "No hay herramientas cargadas. Realice la carga inicial en la opción < 1 >."
                )
            else:
                print(" Inventario ".center(38, "~"))
                print(f"{"Producto".center(25)} | {"Stock".center(10)}")

                for i in range(len(herramientas)):
                    herramienta = herramientas[i]
                    stock = str(existencias[i])
                    print(f"{herramienta.ljust(25)} | {stock.rjust(10)}")

        case 4:
            # 4) Consulta de Stock
            # Verificar que haya herramientas cargadas
            if not herramientas:
                print(
                    "No hay herramientas cargadas. Realice la carga inicial en la opción < 1 >."
                )
            else:
                print("Consulta de stock".center(38, "~"))
                while True:
                    herramienta_a_buscar = input("Nombre de la herramienta: ").strip()

                    if not herramienta_a_buscar:
                        print("Error: el nombre no puede estar vacio.")
                        continue

                    break

                if herramienta_a_buscar in herramientas:
                    indice = herramientas.index(herramienta_a_buscar)
                    stock = existencias[indice]

                    print(f"{herramienta_a_buscar} tiene {stock} existencia/s.")
                else:
                    print(f"No se encontró {herramienta_a_buscar} en el listado.")

        case 5:
            # 5) Reporte de Agotados
            # Verificar que haya herramientas cargadas
            if not herramientas:
                print(
                    "No hay herramientas cargadas. Realice la carga inicial en la opción < 1 >."
                )
            else:
                print(" Reporte de mercaderia sin existencias ".center(38, "~"))

                algun_producto_sin_stock = False
                for existencia in existencias:
                    if existencia == 0:
                        algun_producto_sin_stock = True
                        break

                if algun_producto_sin_stock:
                    for i in range(len(existencias)):
                        if existencias[i] == 0:
                            print(f"- {herramientas[i]}")

                else:
                    print("Todos los productos tienen stock.")

        case 6:
            # 6) Alta de Nuevo Producto
            print(" Alta de nuevo producto ".center(38, "~"))
            herramienta_a_cargar = input("Ingrese el nombre del producto: ").strip()
            if not herramienta_a_cargar:
                print("Error: el nombre no puede estar vacio.")
                continue
            elif herramienta_a_cargar in herramientas:
                print("Error: la herramienta ya existe en el listado.")
                continue

            while True:
                existencias_a_cargar = input("Ingrese las existencias: ").strip()
                if existencias_a_cargar.isdigit():
                    existencias_a_cargar = int(existencias_a_cargar)
                    break

                print("Error: El valor ingresado debe ser un número.")

            herramientas.append(herramienta_a_cargar)
            existencias.append(existencias_a_cargar)
            print(f"El producto {herramienta_a_cargar} fue cargado con éxito.")

        case 7:
            # 7) Actualización de Stock (Venta/Ingreso)
            # Verificar que haya herramientas cargadas
            if not herramientas:
                print(
                    "No hay herramientas cargadas. Realice la carga inicial en la opción < 1 >."
                )
            else:
                print(" Actualizar existencias ".center(38, "~"))

                while True:
                    operacion = input(
                        "Ingrese < V > para registrar una Venta o < I > para registrar un Ingreso de mercaderia: "
                    ).strip()

                    if not operacion or operacion.lower() not in ["v", "i"]:
                        print("Error: la opción ingresada no es correcta.")
                        continue

                    break

                operacion = operacion.lower()
                if operacion == "v":
                    herramienta = input("Ingrese el nombre del producto: ").strip()
                    if not herramienta in herramientas:
                        print("Error: la herramienta no existe en el listado.")
                    else:
                        indice = herramientas.index(herramienta)
                        stock_actual = existencias[indice]

                        if stock_actual <= 0:
                            print(
                                f"Error: {herramienta} no tiene existencias disponibles."
                            )
                        else:
                            while True:
                                cantidad_a_vender = input(
                                    f"Ingrese la cantidad a vender (máximo {stock_actual} unidad/es): "
                                ).strip()

                                es_negativo = (
                                    cantidad_a_vender.startswith("-")
                                    and cantidad_a_vender[1:].isdigit()
                                )
                                if es_negativo:
                                    print(
                                        "Error: el número ingresado debe ser mayor o igual a 0."
                                    )
                                    continue
                                elif not cantidad_a_vender.isdigit():
                                    print(
                                        "Error: El valor ingresado debe ser un número."
                                    )
                                    continue

                                cantidad_a_vender = int(cantidad_a_vender)
                                if cantidad_a_vender > stock_actual:
                                    print(
                                        f"Error: no hay suficientes unidades disponibles. Existencias: {stock_actual} unidad/es."
                                    )
                                    continue

                                nuevo_stock = stock_actual - cantidad_a_vender
                                existencias[indice] = nuevo_stock
                                print(
                                    f"Venta registrada correctamente. \nStock actual: {nuevo_stock}"
                                )
                                break

                elif operacion == "i":
                    herramienta = input("Ingrese el nombre del producto: ").strip()
                    if not herramienta in herramientas:
                        print("Error: la herramienta no existe en el listado.")
                    else:
                        indice = herramientas.index(herramienta)

                        while True:
                            cantidad_a_ingresar = input(
                                f"Ingrese la cantidad a ingresar: "
                            ).strip()

                            es_negativo = (
                                cantidad_a_ingresar.startswith("-")
                                and cantidad_a_ingresar[1:].isdigit()
                            )
                            if es_negativo:
                                print(
                                    "Error: el número ingresado debe ser mayor o igual a 0."
                                )
                                continue
                            elif not cantidad_a_ingresar.isdigit():
                                print("Error: El valor ingresado debe ser un número.")
                                continue

                            cantidad_a_ingresar = int(cantidad_a_ingresar)
                            existencias[indice] += cantidad_a_ingresar
                            print(
                                f"Ingreso registrado. \nNuevo stock de {herramienta}: {existencias[indice]}"
                            )

                            break

        case 8:
            # Salir
            print("Gracias por usar el sistema.")
            break
