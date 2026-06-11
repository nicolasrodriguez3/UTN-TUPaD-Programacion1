# Ejercicio 1
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}


def ejercicio1():
    precios_frutas["Naranja"] = 1200
    precios_frutas["Manzana"] = 1500
    precios_frutas["Pera"] = 2300


# Ejercicio 2
def ejercicio2():
    precios_frutas["Banana"] = 1330
    precios_frutas["Manzana"] = 1700
    precios_frutas["Melón"] = 2800


# Ejercicio 3
def ejercicio3():
    return list(precios_frutas.keys())


# Ejercicio 4
def ejercicio4():
    MAX_CONTACTOS = 5
    print("Guardar contactos")
    contactos = {}

    contador = 1
    while contador <= MAX_CONTACTOS:
        print(f"Contacto {contador}/{MAX_CONTACTOS}")
        nombre = input(f"Nombre: ")
        if not nombre.isalpha():
            print("Nombre inválido. Por favor, ingrese solo letras.")
            continue
        if nombre in contactos:
            print("Este contacto ya existe. Por favor, ingrese un nombre diferente.")
            continue

        telefono = input("Teléfono: ")
        if not telefono.isdigit():
            print("Número de teléfono inválido. Por favor, ingrese solo números.")
            continue

        contactos[nombre] = telefono
        print(f"Contacto guardado: {nombre}")
        contador += 1

    while True:
        print("\nBuscar contacto")
        nombre_busqueda = input("Ingrese el nombre a buscar o 'salir' para terminar: ")
        if not nombre_busqueda.isalpha():
            print("Nombre inválido. Por favor, ingrese solo letras.")
            continue

        if nombre_busqueda.lower() == "salir":
            print("Gracias por usar el programa.")
            break

        if nombre_busqueda in contactos:
            print(f"Teléfono de {nombre_busqueda}: {contactos[nombre_busqueda]}")
        else:
            print(f"Contacto no encontrado: {nombre_busqueda}")


# Ejercicio 5
def ejercicio5():
    frase = input("Ingrese una frase: ").strip()
    if not frase:
        print("No se ha ingresado ninguna frase.")
        return

    palabras = frase.split()
    palabras_unicas = set(palabras)
    conteo_palabras = {}

    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1

    print(f"Palabras únicas: {palabras_unicas}")
    print(f"Conteo de palabras: {conteo_palabras}")


# Ejercicio 6
def ejercicio6():
    alumnos = {}

    for i in range(1, 4):
        while True:
            nombre_alumno = input(f"Ingrese el nombre del alumno {i}: ")
            if not nombre_alumno.isalpha():
                print("El nombre del alumno debe ser unicamente letras.")
                continue
            break

        notas = []
        while len(notas) < 3:
            nota = input(
                f"  Ingrese la nota {len(notas) +1} del alumno {nombre_alumno}: "
            )
            if not nota.isdigit():
                print("Las notas deben ser números positivos.")
                continue

            if int(nota) > 10:
                print("Las notas no pueden superar el 10.")
                continue

            notas.append(int(nota))

        alumnos[nombre_alumno] = tuple(notas)

    print("\n~~~ Promedios ~~~")
    for alumno, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{alumno} | {promedio:.2f}")


# Ejercicio 7
def ejercicio7(asistencias):
    print("~~~ Asistencias ~~~")
    print(asistencias)

    nombres_unicos = set(asistencias)
    print("Empleados que asistieron:")
    for nombre in nombres_unicos:
        print(f"  - {nombre}")

    conteo_asistencias = {}
    for nombre in asistencias:
        if nombre in conteo_asistencias:
            conteo_asistencias[nombre] += 1
        else:
            conteo_asistencias[nombre] = 1

    print("Conteo de asistencias:")
    for nombre, cantidad in conteo_asistencias.items():
        print(f"  - {nombre}: {cantidad}")


# Ejercicio 8
def ejercicio8():
    stock = {"Mouse": 10, "Teclado": 5, "Monitor": 3, "Impresora": 2, "CPU": 4}

    # Menú
    while True:
        print("\n~~~ Menú ~~~")
        print("1. Consultar stock")
        print("2. Agregar unidades al stock")
        print("3. Agregar nuevo producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            producto = input("Ingrese el nombre del producto a consultar: ")
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]} unidad/es")
            else:
                print(f"Producto no encontrado: {producto}")
                print("Productos disponibles:")
                for prod in stock.keys():
                    print(f"  - {prod}")

        elif opcion == "2":
            producto = input("Ingrese el nombre del producto para agregar unidades: ")
            if producto in stock:
                while True:
                    cantidad = input("Ingrese la cantidad a agregar: ")
                    if not cantidad.isdigit():
                        print(
                            "Cantidad inválida. Por favor, ingrese un número positivo."
                        )
                        continue
                    stock[producto] += int(cantidad)
                    print(
                        f"Stock actualizado de {producto}: {stock[producto]} unidad/es"
                    )
                    break
            else:
                print(f"Producto no encontrado: {producto}")

        elif opcion == "3":
            nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
            if nuevo_producto in stock:
                print(f"El producto {nuevo_producto} ya existe en el stock.")
            else:
                while True:
                    cantidad_inicial = input(
                        "Ingrese la cantidad inicial para el nuevo producto: "
                    )
                    if not cantidad_inicial.isdigit():
                        print(
                            "Cantidad inválida. Por favor, ingrese un número positivo."
                        )
                        continue
                    stock[nuevo_producto] = int(cantidad_inicial)
                    print(
                        f"Producto agregado: {nuevo_producto} con {stock[nuevo_producto]} unidad/es"
                    )
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")


# Ejercicio 9
def ejercicio9():
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "14:00"): "Clase de inglés",
        ("miércoles", "16:00"): "Gimnasio",
        ("jueves", "18:00"): "Cena con amigos",
        ("viernes", "20:00"): "Película",
    }

    dia = input("Ingrese el día de la semana: ").lower()
    hora = input("Ingrese la hora (formato HH:MM): ")
    evento = agenda.get((dia, hora))
    if evento:
        print(f"En {dia} a las {hora} tienes: {evento}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")


# Ejercicio 10
def ejercicio10():
    paises = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Chile": "Santiago",
        "Colombia": "Bogotá",
        "Perú": "Lima",
    }

    invertido = {}
    for pais, capital in paises.items():
        invertido[capital] = pais

    print("Original: ")
    print(paises)

    print("\nInvertido: ")
    print(invertido)


while True:
    print("\n~~~ Menú de Ejercicios ~~~")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Salir")

    opcion = input("Seleccione un ejercicio para ejecutar: ")
    if opcion == "1":
        ejercicio1()
        for fruta, precio in precios_frutas.items():
            print(f"{fruta}: ${precio}")
    elif opcion == "2":
        ejercicio2()
        for fruta, precio in precios_frutas.items():
            print(f"{fruta}: ${precio}")
    elif opcion == "3":
        claves = ejercicio3()
        for clave in claves:
            print(clave)
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]
        ejercicio7(asistencias)
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()
    elif opcion == "11":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")
