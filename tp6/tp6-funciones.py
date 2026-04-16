import math


# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla
# el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa
# principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como
# parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si
# se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al
# usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


# 3. Crear una función llamada informacion_personal(nombre, apellido, edad,
# residencia) que reciba cuatro parámetros e imprima: “Soy [nombre]
# [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al
# usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio)
# que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una
# cantidad de segundos como parámetro y devuelva la cantidad de horas
# correspondientes. Solicitar al usuario los segundos y mostrar el resultado
# usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número
# como parámetro y imprima la tabla de multiplicar de ese número del 1 al
# 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos
# números como parámetros y devuelva una tupla con el resultado de
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de
# forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = "No se puede dividir por cero"
    if b != 0:
        division = a / b

    return suma, resta, multiplicacion, division


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en
# kilogramos y la altura en metros, y devuelva el índice de masa corporal
# (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el
# resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return round(imc, 2)


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una
# temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la
# función.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres
# números como parámetros y devuelva el promedio de ellos. Solicitar los
# números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal
while True:
    print(
        """
Seleccione una opción:
1. Imprimir "Hola Mundo!"
2. Saludar al usuario
3. Mostrar información personal
4. Calcular área y perímetro de un círculo
5. Convertir segundos a horas
6. Mostrar tabla de multiplicar
7. Realizar operaciones básicas
8. Calcular IMC
9. Convertir Celsius a Fahrenheit
10. Calcular promedio
11. Salir
          """
    )
    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            imprimir_hola_mundo()
        case "2":
            nombre_usuario = input("Ingrese su nombre: ")
            saludar_usuario(nombre_usuario)
        case "3":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            edad = input("Ingrese su edad: ")
            residencia = input("Ingrese su lugar de residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)

        case "4":
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")
            print(f"El perímetro del círculo es: {perimetro:.2f}")

        case "5":
            segundos = int(input("Ingrese la cantidad de segundos: "))
            horas = segundos_a_horas(segundos)
            print(f"{segundos} segundos equivalen a {horas:.2f} horas")

        case "6":
            numero = int(
                input("Ingrese un número para mostrar su tabla de multiplicar: ")
            )
            tabla_multiplicar(numero)

        case "7":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultados = operaciones_basicas(num1, num2)
            print(f"Suma: {resultados[0]}")
            print(f"Resta: {resultados[1]}")
            print(f"Multiplicación: {resultados[2]}")
            print(f"División: {resultados[3]}")

        case "8":
            peso = float(input("Ingrese su peso en kilogramos: "))
            altura = float(input("Ingrese su altura en metros: "))
            imc = calcular_imc(peso, altura)
            print(f"Su Índice de Masa Corporal (IMC) es: {imc}")

        case "9":
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C equivalen a {fahrenheit}°F")

        case "10":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            num3 = float(input("Ingrese el tercer número: "))
            promedio = calcular_promedio(num1, num2, num3)
            print(f"El promedio de los tres números es: {promedio}")

        case "11":
            print("¡Gracias por usar el programa!")
            break

        case _:
            print("Opción no válida. Por favor, intente nuevamente.")
