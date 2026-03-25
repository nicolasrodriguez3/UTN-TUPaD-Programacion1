# Ejercicio 2 - Campus y Menú Seguro
# Imports
from random import choice

# Constantes
DEV_PHRASES = [
    "Si no lo entendés, explicalo.",
    "Leer código es parte del trabajo.",
    "Debuggear también es programar.",
    "Googlear bien es una skill.",
    "Si funciona pero no entendés, no terminaste.",
    "Primero que funcione, después que sea lindo.",
]
USERNAME = "alumno"
PASSWORD = "python123"
MAX_FAILED_ATTEMPTS = 3

attempts = 0
login_successful = False
while attempts < MAX_FAILED_ATTEMPTS:
    attempts += 1

    username_input = input("Usuario: ")
    password_input = input("Contraseña: ")

    if username_input == USERNAME and password_input == PASSWORD:
        login_successful = True
        break

    # Intento fallido
    print(
        f"Datos inválidos, intente nuevamente.\nIntentos restantes: {MAX_FAILED_ATTEMPTS - attempts}"
    )
else:
    print("Cuenta bloqueada. Contacte con administración")

# Logueo exitoso
if login_successful:
    print(f"Bienvenido, {USERNAME.capitalize()}")
    # Menú
    while True:
        option = input("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir\n").strip()

        if not option.isdigit():
            print("Solo se permiten números.")
            continue

        option = int(option)
        if option < 0 or option > 4:
            print("Opción inválida.")
            continue

        if option == 4:
            # Salir
            break
        elif option == 1:
            print("Estado: Inscripto")
        elif option == 2:
            while True:
                new_password = input("Ingrese una nueva clave: ").strip()
                confirmation_password = input("Ingrese nuevamente: ").strip()

                if len(new_password) < 6:
                    print("La contraseña debe tener mínimo 6 caracteres. ")
                elif new_password != confirmation_password:
                    print("Las contraseñas no coinciden. Intente nuevamente. ")
                else:
                    print("Contraseña actualizada.")
                    break

        elif option == 3:
            print(choice(DEV_PHRASES))

        else:
            print("Opción inválida.")
