# Actividades
# 1) Identifica los errores del código usando comentarios (#) en las líneas afectadas.
# Indica el tipo de error y una breve explicación de por qué ocurre.
# Ejemplo: c = a / b # Error: TypeError. 'b' es un string y no permite la división.

a = 10
b = input("Introduce un número: ")
result = a / b  # Error: TypeError. 'b' es un string y no permite la división.
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[5])  # Error: IndexError. El índice 5 está fuera del rango de la lista.


# 2) Utilizando el código del ejercicio 1, arreglar los errores para que la
# ejecución del programa sea correcta sin necesidad de usar excepciones.
a = 10
b = int(input("Introduce un número: "))
result = a / b
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[2])


# 3) Utilizando el código del ejercicio 1, mantener el código con los errores
# originales e incluir bloques try-except para que la ejecución del programa
# no se frene al encontrar los errores.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b  # Error: TypeError. 'b' es un string y no permite la división.
    print(f"Resultado: {result}")
except TypeError:
    print("No se puede dividir por un string. Intente nuevamente")

try:
    numbers = [1, 2, 3]
    print(
        numbers[5]
    )  # Error: IndexError. El índice 5 está fuera del rango de la lista.
except IndexError:
    print("El valor solicitado está fuera de rango.")


# 4) Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión
# a los tipos de errores detectados.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b  # Error: TypeError. 'b' es un string y no permite la división.
    print(f"Resultado: {result}")
except TypeError:
    print("No se puede dividir por un string. Intente nuevamente")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except:
    print("Error desconocido, intente nuevamente.")

try:
    numbers = [1, 2, 3]
    print(
        numbers[5]
    )  # Error: IndexError. El índice 5 está fuera del rango de la lista.
except IndexError:
    print("El valor solicitado está fuera de rango.")
except:
    print("Error desconocido, intente nuevamente.")


# 5) Repetir el ejercicio 4, pero esta vez incluyendo bloques else y finally.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b  # Error: TypeError. 'b' es un string y no permite la división.
    print(f"Resultado: {result}")
except TypeError:
    print("No se puede dividir por un string. Intente nuevamente")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except:
    print("Error desconocido, intente nuevamente.")
else:
    print("El código fue ejecutado correctamente.")
finally:
    print("Gracias por usar el programa.")

try:
    numbers = [1, 2, 3]
    print(
        numbers[5]
    )  # Error: IndexError. El índice 5 está fuera del rango de la lista.
except IndexError:
    print("El valor solicitado está fuera de rango.")
except:
    print("Error desconocido, intente nuevamente.")
else:
    print("El código fue ejecutado correctamente.")
finally:
    print("Gracias por usar el programa.")


# 6) Escribir un programa que pida al usuario un número, y:
# Si el valor ingresado es válido, lo imprima por pantalla.
# Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un
# número válido”.
# Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error
# inesperado” junto con el error que surgió.

try:
    valor = int(input("Ingrese un número: "))
    print(valor)
except ValueError:
    print("Debe ingresar un número válido.")
except Exception as e:
    print("Se produjo un error inesperado", type(e).__name__)


# 7) Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente
# ingresar un nuevo número luego de encontrar un error.

while True:
    try:
        valor = int(input("Ingrese un número: "))
        print(valor)
        break
    except ValueError:
        print("Debe ingresar un número válido.")
    except Exception as e:
        print("Se produjo un error inesperado", type(e).__name__)
