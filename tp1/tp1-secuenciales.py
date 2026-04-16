# Ejercicio 1
print("Hola Mundo!")


# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# Ejercicio 3
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre}, tengo {edad} años y vivo en {residencia}")


# Ejercicio 4
import math  # Para poder usar PI sin tener que cargarlo en una variable manualmente

radio = int(input("Ingrese el radio del círculo: "))

area = math.pi * radio**2
perimetro = math.pi * radio * 2

print(f"El área es: {area}")
print(f"El perímetro es: {perimetro}")


# Ejercicio 5
segundos = int(
    input("Ingrese la cantidad de segundos para ver su equivalencia en horas: ")
)

horas = segundos // 3600
minutos = segundos % 3600 // 60

print(f"Equivale a {horas} horas y {minutos} minutos.")


# Ejercicio 6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Si no podria usar `for` usaria 1 `print` por cada número del 0 al 10
for num in range(1, 11):
    resultado = num * numero
    print(f"{numero} × {num} = {resultado}")


# Ejercicio 7
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número (distinto de 0): "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicacion es {multiplicacion}")
print(f"La division es {division}")


# Ejercicio 8
altura = int(input("Ingrese su altura en cm: "))
peso = float(input("Ingrese su peso en kg: "))

imc = peso / ((altura / 100) ** 2)

print(f"Tu IMC es {round(imc, 2)}")


# Ejercicio 9
temperatura = float(input("Ingrese la temperatura en grados Celcius: "))

resultado = (9 / 5) * temperatura + 32

print(f"El equivalente en grados Fahrenheit es {resultado}")


# Ejercicio 10
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
numero3 = float(input("Ingrese un último número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio es: {promedio}")
