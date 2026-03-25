# Ejercicio 5: La arena del gladiador

# Paso 1: Nombre del jugador
print("--- BIENVENIDO A LA ARENA ---")
while True:
    nombre_jugador = input("Nombre del jugador: ").strip()

    if nombre_jugador.isalpha():
        break

    print("Error: Solo se permiten letras")

# Paso 2: Inicialización de Estadísticas
vida_jugador = 100
vida_enemigo = 100
pociones_jugador = 3
danio_base_jugador = 15
danio_base_enemigo = 12

turno_jugador = True
numero_turno = 0
# Paso 3: Combate
print("=== INICIO DEL COMBATE === ")
while vida_jugador > 0 and vida_enemigo > 0:
    numero_turno += 1
    print(f"Turno número {numero_turno}")
    if turno_jugador:
        # Menú
        print(
            f"""
Vida: {vida_jugador}
Pociones restantes: {pociones_jugador}
Vida del enemigo: {vida_enemigo}"""
        )
        while True:
            opcion = input(
                f"""
Acciones:
1. Ataque pesado
2. Ráfaga veloz
3. Curar

Opción: """
            ).strip()

            # Validar número
            if opcion.isdigit() and int(opcion) > 0 and int(opcion) <= 3:
                opcion = int(opcion)
                break

            print("Opción inválida")

        if opcion == 1:
            if vida_enemigo < 20:
                # Golpe crítico
                print("¡Golpe crítico!")
                danio = danio_base_jugador * 1.5
            else:
                danio = danio_base_jugador

            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

        elif opcion == 2:
            print("¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones_jugador > 0:
                pociones_jugador -= 1
                vida_jugador += 30

                if vida_jugador >= 100:
                    vida_jugador = 100
            else:
                print("¡No quedan pociones!")

    else:
        print(f"¡El enemigo te atacó por {danio_base_enemigo} puntos de daño!")
        vida_jugador -= danio_base_enemigo

    turno_jugador = not turno_jugador

# Fin del juego
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_jugador.capitalize()} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
