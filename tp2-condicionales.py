# Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")


# Ejercicio 2
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad >= 30:
    print("Adulto")
elif edad >= 18:
    print("Adulto joven")
elif edad >= 12:
    print("Adolescente")
else:
    print("Niño/a")


# Ejercicio 5
password = input("Ingrese su contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6
electric_consumption = int(input("Ingrese su consumo electrico: "))

if electric_consumption < 150:
    print("Consumo bajo")
elif electric_consumption <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")
    if electric_consumption > 500:
        print("Considere medidas de ahorro energético")


# Ejercicio 7
user_input = input("Ingrese una palabra o frase: ")

vocals = "aeiouAEIOU"
if user_input[-1] in vocals:
    print(f"{user_input}!")
else:
    print(user_input)


# Ejercicio 8
name = input("Ingrese su nombre: ")
option = int(
    input(
        """Ingrese su opción:
1. Transformar a mayúsculas
2. Transformar a minúsculas
3. Poner la primer letra en mayúscula
"""
    )
)

if option == 1:
    print(name.upper())
elif option == 2:
    print(name.lower())
elif option == 3:
    print(name.capitalize())
else:
    print("Por favor, ingrese una opción válida")


# Ejercicio 9
earthquake_magnitude = int(input("Ingrese la magnitud del terremoto: "))

if earthquake_magnitude < 3:
    print("Muy leve")
elif earthquake_magnitude < 4:
    print("Leve")
elif earthquake_magnitude < 5:
    print("Moderado")
elif earthquake_magnitude < 6:
    print("Fuerte")
elif earthquake_magnitude < 7:
    print("Muy fuerte")
else:
    print("Extremadamente fuerte")


# Ejercicio 10
day = int(input("Ingrese el dia del mes: "))
month = int(input("Ingrese el mes: "))
hemisphere = input("Ingrese el hemisferio (Norte/Sur): ")
hemisphere = hemisphere[0].lower()

if hemisphere == "n":
    if (
        (month == 12 and day >= 21)
        or (month == 1 or month == 2)
        or (month == 3 and day <= 20)
    ):
        print("Invierno")
    elif (
        (month == 3 and day >= 21)
        or (month == 4 or month == 5)
        or (month == 6 and day <= 20)
    ):
        print("Primavera")
    elif (
        (month == 6 and day >= 21)
        or (month == 7 or month == 8)
        or (month == 9 and day <= 22)
    ):
        print("Verano")
    elif (
        (month == 9 and day >= 23)
        or (month == 10 or month == 11)
        or (month == 12 and day <= 20)
    ):
        print("Otoño")
    else:
        print("Por favor, ingrese un dia y mes validos")
elif hemisphere == "s":
    if (
        (month == 6 and day >= 21)
        or (month == 7 or month == 8)
        or (month == 9 and day <= 22)
    ):
        print("Invierno")
    elif (
        (month == 9 and day >= 23)
        or (month == 10 or month == 11)
        or (month == 12 and day <= 20)
    ):
        print("Primavera")
    elif (
        (month == 12 and day >= 21)
        or (month == 1 or month == 2)
        or (month == 3 and day <= 20)
    ):
        print("Verano")
    elif (
        (month == 3 and day >= 21)
        or (month == 4 or month == 5)
        or (month == 6 and day <= 20)
    ):
        print("Otoño")
    else:
        print("Por favor, ingrese un dia y mes validos")

else:
    print("Por favor, ingrese un hemisferio valido")
