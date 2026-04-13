import random

# 1. Crear una lista con las notas de 10 estudiantes.
notas = [7.5, 8, 4.5, 9, 6, 5.5, 10, 3, 8.5, 7]

# Mostrar la lista completa.
print("Lista de notas:")
for nota in notas:
    print(nota)

# Calcular y mostrar el promedio.
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

# Indicar la nota más alta y la más baja.
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)


# 2. Pedir al usuario que cargue 5 productos en una lista
lista_productos = []
while len(lista_productos) < 5:
    producto = input("Ingrese un producto para agregar a la lista: ")
    lista_productos.append(producto)

# Mostrar la lista ordenada alfabéticamente.
lista_productos_ordenada = sorted(lista_productos)
indice = 0
for producto in lista_productos_ordenada:
    indice += 1
    print(f"{indice} - {producto}")


desea_eliminar = False
while True:
    input_desea_eliminar = input("¿Desea eliminar algún producto (Si/No)? ").strip()
    input_desea_eliminar = input_desea_eliminar.lower()
    if input_desea_eliminar == "si" or input_desea_eliminar == "s":
        desea_eliminar = True
        break
    elif input_desea_eliminar == "no" or input_desea_eliminar == "n":
        break


while desea_eliminar:
    while True:
        indice_eliminar = input("Ingrese el número de producto a eliminar: ")
        if indice_eliminar.isdigit():
            break

        print("Error: Ingrese únicamente números.")

    indice_eliminar = int(indice_eliminar)

    if indice_eliminar <= len(lista_productos_ordenada):
        producto_eliminado = lista_productos_ordenada.pop(indice_eliminar - 1)
        print(f"El producto {producto_eliminado} fue eliminado.")
    else:
        print("Índice inválido.")
        continue

    # Mostrar productos restantes
    indice = 0
    for producto in lista_productos_ordenada:
        indice += 1
        print(f"{indice} - {producto}")

    # Parar la ejecución del bucle si selecciona 'No'
    while True:
        input_desea_eliminar = input("¿Desea eliminar otro producto (Si/No)? ").strip()
        input_desea_eliminar = input_desea_eliminar.lower()
        if input_desea_eliminar == "si" or input_desea_eliminar == "s":
            break
        elif input_desea_eliminar == "no" or input_desea_eliminar == "n":
            desea_eliminar = False
            break

# 3. Generar una lista con 15 números enteros al azar entre 1 y 100.
lista = []
for _ in range(15):
    lista.append(random.randint(1, 100))

print("Números generados:")
for num in lista:
    print(num, end=" ")

print()

lista_pares = []
lista_impares = []
# Crear una lista con los pares y otra con los impares
for num in lista:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

# Mostrar cuántos números tiene cada lista
print(f"Total números pares: {len(lista_pares)}")
print(f"Total números impares: {len(lista_impares)}")


# 4. Crear lista sin elementos repedidos sin usar set
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
nueva_lista = []

for dato in datos:
    if dato not in nueva_lista:
        nueva_lista.append(dato)

# Resultado
for dato in nueva_lista:
    print(dato, end=" ")
print()


# 5. Crear una lista con los nombres de 8 estudiantes presentes en clase.
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía", "Jorge", "Lucía", "Diego"]

# Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
while True:
    print("== Listado de estudiantes ==")
    for estudiante in estudiantes:
        print(" - ", estudiante)
    print("")

    print("Seleccione una opción: ")
    print("1 - Agregar nuevo estudiante")
    print("2 - Eliminar estudiante")
    print("Presiona otra tecla para salir.")
    opcion = input("Opción: ")

    if opcion == "1":
        estudiante_a_agregar = input("Nombre del estudiante: ")
        estudiantes.append(estudiante_a_agregar)
    elif opcion == "2":
        estudiante_a_eliminar = input("Nombre del estudiante a eliminar: ")
        if estudiante_a_eliminar not in estudiantes:
            print("Estudiante no encontrado.")
            continue

        estudiantes.remove(estudiante_a_eliminar)
    else:
        break

print("== Listado de estudiantes ==")
for estudiante in estudiantes:
    print(" - ", estudiante)

# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
lista = list(range(1, 8))

# Rotar elementos
nueva_lista = [lista[-1]]
nueva_lista.extend(lista[0:-1])

print("Lista original: ")
for num in lista:
    print(num, end=" ")

print("\nNueva lista: ")
# Resultado
for num in nueva_lista:
    print(num, end=" ")


# 7. Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
temperaturas = [[20, 30], [25, 35], [22, 34], [20, 35], [21, 31], [17, 27], [20, 33]]

# Calcular el promedio de las mínimas y el de las máximas
sumatoria_minimas = 0
sumatoria_maximas = 0

for minima, maxima in temperaturas:
    sumatoria_minimas += minima
    sumatoria_maximas += maxima

promedio_minimas = sumatoria_minimas / len(temperaturas)
promedio_maximas = sumatoria_maximas / len(temperaturas)

print(f"El promedio de temperaturas mínimas es de: {promedio_minimas:.2f}")
print(f"El promedio de temperaturas máximas es de: {promedio_maximas:.2f}")

# Mostrar en qué día se registró la mayor amplitud térmica.
amplitud = 0
dia = 0
for dia_actual in temperaturas:
    amplitud_dia = dia_actual[1] - dia_actual[0]
    if amplitud_dia > amplitud:
        amplitud = amplitud_dia
        dia = temperaturas.index(dia_actual)

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print(
    f"El día con mayor amplitud térmica fue el día {dias[dia]} con una amplitud de {amplitud} grados. (mín: {temperaturas[dia][0]}°C, máx: {temperaturas[dia][1]}°C)"
)


# Crear una matriz con las notas de 5 estudiantes en 3 materias.
notas = [[7, 8, 5], [9, 8, 5.5], [10, 5, 2], [7, 8.5, 9], [6, 8, 10]]

# Mostrar el promedio de cada estudiante.
print("\nPromedio de estudiante: ")
for estudiante in notas:
    promedio = sum(estudiante) / len(estudiante)
    print(round(promedio, 2))

# Mostrar el promedio de cada materia.
sumatoria_notas = [0] * len(notas[0])
for estudiante in notas:
    for i in range(len(estudiante)):
        sumatoria_notas[i] += estudiante[i]

total_estudiantes = len(notas)
promedios = [nota / total_estudiantes for nota in sumatoria_notas]

print("\nEl promedio de cada materia es: ")
for materia in promedios:
    print(round(materia, 2))


# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializarlo con guiones "-" representando casillas vacías.
VACIO = "-"
tablero = [[VACIO] * 3 for _ in range(3)]

# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
esX = True
while True:
    print(f"\n===== JUGADOR {"1" if esX else "2"} =====")
    print(f"Ingrese la posición para colocar {"una ×" if esX else "un ○"}")

    while True:
        posicion_input = input(
            f"Ingrese la fila y columna separadas por un espacio (ejemplo: 2 2): "
        ).strip()

        posicion = posicion_input.split()
        if len(posicion) != 2:
            print("Error: Ingrese ambas posiciones. Intente nuevamente.")
            continue

        if not posicion[0].isdigit() or not posicion[1].isdigit():
            print("Error: ingrese la fila y columna como números. Intente nuevamente.")
            continue

        # Restamos 1 para usarlo de índice en el array
        fila = int(posicion[0]) - 1
        columna = int(posicion[1]) - 1
        if fila < 0 or fila > 2 or columna < 0 or columna > 2:
            print("Error: fila o columna fuera de rango. Intente nuevamente.")
            continue

        celda = tablero[fila][columna]
        if celda != VACIO:
            print("La celda ya está ocupada. Ingrese otra.")
            continue

        # Si llega aca es porque las validaciones fueron correctas
        break

    # Completar el tablero
    tablero[fila][columna] = "×" if esX else "○"

    # Cambiar turno al otro jugador
    esX = not esX

    # Mostrar tablero
    print("-" * (13))
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")
        print("-" * 13)

    hay_espacio_disponible = False
    for fila in tablero:
        if VACIO in fila:
            hay_espacio_disponible = True
            break

    if not hay_espacio_disponible:
        print("No hay más celdas disponibles")
        break


# 10. Una tienda registra las ventas de 4 productos durante 7 dias

productos = [
    # D, L, M, X, J, V, S
    [10, 12, 8, 15, 20, 18, 25],
    [5, 7, 6, 10, 12, 9, 14],
    [20, 25, 22, 30, 35, 28, 40],
    [8, 10, 9, 12, 15, 11, 18],
]

# Mostrar el total vendido por cada producto.
indice = 0
for producto in productos:
    indice += 1
    suma = sum(producto)

    print(f"Total vendido producto n°. {indice}: ${suma:.2f}")

# Mostrar el día con mayores ventas totales.
ventas_por_dia = []
for i in range(len(productos[0])):
    nueva_fila = []
    for j in range(len(productos)):
        nueva_fila.append(productos[j][i])
    ventas_por_dia.append(nueva_fila)


dia_numero = 0
maximo_ventas = 0
for i in range(len(ventas_por_dia)):
    total_del_dia = sum(ventas_por_dia[i])
    if total_del_dia > maximo_ventas:
        maximo_ventas = total_del_dia
        dia_numero = i + 1


print(f"El día con más ventas fue el día {dia_numero} con ${maximo_ventas:.2f}.")

# Indicar cuál fue el producto más vendido en la semana.
producto_numero = 0
total_producto_mas_vendido = 0
for i in range(len(productos)):
    suma = sum(productos[i])

    if suma > total_producto_mas_vendido:
        total_producto_mas_vendido = suma
        producto_numero = i + 1


print(
    f"El producto más vendido de la semana es el producto n° {producto_numero} por un total de ${total_producto_mas_vendido:.2f}."
)


# 11. Crear una lista con los nombres de 10 estudiantes.
estudiantes = [
    "Ana",
    "Luis",
    "María",
    "Carlos",
    "Sofía",
    "Jorge",
    "Lucía",
    "Diego",
    "Marta",
    "Pedro",
]

# Solicitar al usuario que ingrese un nombre a buscar
nombre_a_buscar = input("Ingrese el nombre de un estudiante a buscar: ")

# Indicar si el nombre se encuentra en la lista.
if nombre_a_buscar in estudiantes:
    print("El nombre está en la lista", end=" ")

    # Mostrar la posición en la que aparece.
    print(f"en la posición n°. {estudiantes.index(nombre_a_buscar) + 1}")

# Si no se encuentra, informar que no está en la lista.
else:
    print("El nombre no está en la lista.")


# 12. Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
numeros = []
while len(numeros) < 8:
    numero = input("Ingrese un número para guardarlo en la lista: ")

    if not numero.isdigit():
        print("Error: Solo se permiten números")
        continue

    numeros.append(int(numero))

# Mostrar la lista original.
print("Los números ingresados son: ")
for numero in numeros:
    print(numero, end=" ")
print("\n")


# Mostrar la lista ordenada de menor a mayor.
# Usando sorted (función)
print("Ordenados con sorted()")
print("De menor a mayor: ")
lista_menor_a_mayor = sorted(numeros)
for numero in lista_menor_a_mayor:
    print(numero, end=" ")
print("\n")

# Mostrar la lista ordenada de mayor a menor.
print("Mayor a menor: ")
lista_mayor_a_menor = sorted(numeros, reverse=True)
for numero in lista_mayor_a_menor:
    print(numero, end=" ")
print("\n")

# Usando sort (método). Se puede observar que modifica la lista original
numeros_copia = numeros[:]
# Menor a mayor
print("Ordenados con .sort()")
print("De menor a mayor: ")
numeros_copia.sort()
for numero in numeros_copia:
    print(numero, end=" ")
print("\n")

# Mayor a menor
print("Mayor a menor: ")
numeros_copia.sort(reverse=True)
for numero in numeros_copia:
    print(numero, end=" ")
print()


# 13. Dada la siguiente lista de puntajes de un videojuego
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Mostrar el puntaje más alto y el más bajo.
mayor_puntaje = max(puntajes)
print(
    f"El puntaje más alto es {mayor_puntaje} del jugador n°. {puntajes.index(mayor_puntaje) + 1}"
)
menor_puntaje = min(puntajes)
print(
    f"El puntaje más bajo es {menor_puntaje} del jugador n°. {puntajes.index(menor_puntaje) + 1}"
)

# Mostrar la lista ordenada de mayor a menor (ranking).
ranking = sorted(puntajes, reverse=True)
posicion = 0
for puntaje in ranking:
    posicion += 1
    print(f"{posicion}° puesto: {puntaje}")
print()

# Ordenar con bubble sort para precticar:
largo_lista = len(puntajes)
# Recorrer la lista hasta la anteúltima posición
for i in range(largo_lista - 1):
    # Flag para marcar si hubo intercambios, de esta manera no recorremos una lista que ya está ordenada
    intercambio = False

    # Por cada elemento, recorrer la lista nuevamente y vamos disminuyendo los recorridos
    for j in range(largo_lista - 1 - i):
        # Revisar si el elemento actual es mayor al siguiente
        if puntajes[j] < puntajes[j + 1]:
            # Intercambiar los elementos
            puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j]
            intercambio = True

    # Si luego del primer recorrido no hubo intercambios, la lista está ordenada
    if not intercambio:
        break

print("Lista ordenada con bubble sort:", puntajes)

# Indicar en qué posición del ranking se encuentra el puntaje 990.
print(
    f"La puntuación 990 se encuentra en el ranking en la posición {ranking.index(990) + 1}."
)
