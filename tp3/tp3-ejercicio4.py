# Ejercicio 4: Escape Room
import random
import string

# variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

TOTAL_CERRADURAS = 3
cerraduras_forzadas = 0


while True:
    nombre_agente = input("Nombre del agente: ").strip()

    if nombre_agente.isalpha():
        break

    print("Nombre del agente inválido. Ingrese unicamente letras.")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        break

    while True:
        print(f"Cerraduras abiertas: {cerraduras_abiertas}/{TOTAL_CERRADURAS}")
        alarma and print("Alarma ACTIVA")
        opcion = input(
            f"""
Energia disponible: {energia}
Tiempo restante: {tiempo}

Acciones:
1. Forzar cerradura
2. Hackear panel
3. Descansar

Opción: """
        ).strip()

        # Validar número
        if opcion.isdigit() and int(opcion) > 0 and int(opcion) <= 3:
            opcion = int(opcion)
            break

        print("Opción inválida")

    if opcion == 1:
        # Forzar cerradura
        cerraduras_forzadas += 1
        energia -= 20
        tiempo -= 2

        if cerraduras_forzadas == 3:
            print("La cerradura se trabó")
            alarma = True
        elif energia < 40:
            while True:
                numero = input("Riesgo de alarma. Elija un número del 1 al 3: ")

                if numero.isdigit() and int(numero) > 0 and int(numero) <= 3:
                    numero = int(numero)
                    break
                print("Opción inválida")

            if numero == 3:
                alarma = True
                print("Se ha activado la alarma.")
            else:
                cerraduras_abiertas += 1
                print("Se ha abierto la cerradura.")

        elif not alarma:
            cerraduras_abiertas += 1
            print("Se ha abierto la cerradura.")
            print(f"Cerraduras faltantes: {TOTAL_CERRADURAS - cerraduras_abiertas}")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        # Restablecer racha de cerraduras forzadas
        cerraduras_forzadas = 0

        print("Hackeando panel...")
        for i in range(4):
            letra_aleatoria = random.choice(string.ascii_letters)
            codigo_parcial += letra_aleatoria
            caracteres_faltantes = 8 - len(codigo_parcial)

            print(codigo_parcial + "*" * caracteres_faltantes)

        if len(codigo_parcial) >= 8:
            codigo_parcial = ""
            cerraduras_abiertas += 1
            print("Se ha abierto la cerradura.")
            print(f"Cerraduras faltantes: {TOTAL_CERRADURAS - cerraduras_abiertas}")

        else:
            print("No se pudo completar el hackeo.")

    elif opcion == 3:
        energia += 15
        tiempo -= 1
        # Restablecer racha de cerraduras forzadas
        cerraduras_forzadas = 0

        if alarma:
            energia -= 10

        if energia >= 100:
            energia = 100


# Evaluar victoria/derrota
if alarma and cerraduras_abiertas >= 1:
    print("INTRUSO DETECTADO. Sistema bloqueado.")
elif cerraduras_abiertas == 3:
    print("Boveda abierta. ¡Ganaste!")

elif energia <= 0:
    print("No tienes más energia para continuar. Perdiste")

elif tiempo <= 0:
    print("Se terminó el tiempo. Perdiste")
