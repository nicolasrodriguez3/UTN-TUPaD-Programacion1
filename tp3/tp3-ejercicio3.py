# Ejercicio 3 - Agenda de turnos con nombres
# constantes
MONDAY_MAX_APPOINTMENTS = 4
TUESDAY_MAX_APPOINTMENTS = 4

# variables para los turnos
monday1 = ""
monday2 = ""
monday3 = ""
monday4 = ""
tuesday1 = ""
tuesday2 = ""
tuesday3 = ""

while True:
    name = input("Operador: ").strip()
    if name and name.isalpha():
        break

    print("Error: ingrese unicamente letras.")


print(f"\nBienvenido, {name.capitalize()}")
# Menú
while True:
    option = input(
        """
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema

Opción: """
    ).strip()

    match option:
        # Agendar turno
        case "1":
            while True:
                day = input("Elegir día (1=Lunes, 2=Martes): ").strip()
                if day == "1" or day == "2":
                    break

                print("Ingrese una opción válida")

            while True:
                patient_name = input("Ingrese el nombre del paciente: ").strip()

                if patient_name.isalpha():
                    break

                print("Nombre del paciente inválido. Ingrese unicamente letras.")

            if day == "1":
                # Verificar si el paciente ya tiene turno
                if patient_name in (monday1, monday2, monday3, monday4):
                    print("El paciente ya tiene un turno registrado.")
                elif monday1 == "":
                    monday1 = patient_name
                    print("Turno nro. 1 registrado para el dia lunes.")
                elif monday2 == "":
                    monday2 = patient_name
                    print("Turno nro. 2 registrado para el dia lunes.")
                elif monday3 == "":
                    monday3 = patient_name
                    print("Turno nro. 3 registrado para el dia lunes.")
                elif monday4 == "":
                    monday4 = patient_name
                    print("Turno nro. 4 registrado para el dia lunes.")
                else:
                    print("No quedan turnos disponibles el dia lunes.")

            elif day == "2":
                # Verificar si el paciente ya tiene turno
                if patient_name in (tuesday1, tuesday2, tuesday3):
                    print("El paciente ya tiene un turno registrado.")
                elif tuesday1 == "":
                    tuesday1 = patient_name
                    print("Turno nro. 1 registrado para el dia martes.")
                elif tuesday2 == "":
                    tuesday2 = patient_name
                    print("Turno nro. 2 registrado para el dia martes.")
                elif tuesday3 == "":
                    tuesday3 = patient_name
                    print("Turno nro. 3 registrado para el dia martes.")
                else:
                    print("No quedan turnos disponibles el dia martes.")

        # Cancelar turno
        case "2":
            while True:
                day = input("Elegir día (1=Lunes, 2=Martes): ").strip()
                if day == "1" or day == "2":
                    break

                print("Ingrese una opción válida")

            while True:
                patient_name = input("Ingrese el nombre del paciente: ").strip()

                if patient_name.isalpha():
                    break

                print("Nombre del paciente inválido. Ingrese unicamente letras.")

            if day == "1":
                if monday1 == patient_name:
                    monday1 = ""
                elif monday2 == patient_name:
                    monday2 = ""
                elif monday3 == patient_name:
                    monday3 = ""
                elif monday4 == patient_name:
                    monday4 = ""
                else:
                    print("El paciente no tiene turno registrado el dia lunes.")
                    continue

                print("Turno cancelado")
            elif day == "2":
                if tuesday1 == patient_name:
                    tuesday1 = ""
                elif tuesday2 == patient_name:
                    tuesday2 = ""
                elif tuesday3 == patient_name:
                    tuesday3 = ""
                else:
                    print("El paciente no tiene turno registrado el dia martes.")
                    continue

                print("Turno cancelado")

        # Agenda del dia
        case "3":
            while True:
                day = input("Elegir día (1=Lunes, 2=Martes): ").strip()
                if day == "1" or day == "2":
                    break

                print("Ingrese una opción válida")

            if day == "1":
                print(
                    f"""
Agenda día lunes:
 - Turno 1: {monday1 if monday1 != "" else "libre"}
 - Turno 2: {monday2 if monday2 != "" else "libre"}
 - Turno 3: {monday3 if monday3 != "" else "libre"}
 - Turno 4: {monday4 if monday4 != "" else "libre"}
"""
                )
            elif day == "2":
                print(
                    f"""
Agenda día martes:
 - Turno 1: {tuesday1 if tuesday1 != "" else "libre"}
 - Turno 2: {tuesday2 if tuesday2 != "" else "libre"}
 - Turno 3: {tuesday3 if tuesday3 != "" else "libre"}
"""
                )

        # Resumen general
        case "4":
            appointments_monday = 0
            appointments_tuesday = 0

            appointments_monday += 1 if monday1 != "" else 0
            appointments_monday += 1 if monday2 != "" else 0
            appointments_monday += 1 if monday3 != "" else 0
            appointments_monday += 1 if monday4 != "" else 0

            appointments_tuesday += 1 if tuesday1 != "" else 0
            appointments_tuesday += 1 if tuesday2 != "" else 0
            appointments_tuesday += 1 if tuesday3 != "" else 0

            available_appts_monday = MONDAY_MAX_APPOINTMENTS - appointments_monday
            available_appts_tuesday = TUESDAY_MAX_APPOINTMENTS - appointments_tuesday

            print(
                f"Lunes: {appointments_monday} {"turno ocupado" if appointments_monday == 1 else "turnos ocupados"} - {available_appts_monday} {"turno libre" if available_appts_monday == 1 else "turnos libres"}"
            )
            print(
                f"Martes: {appointments_tuesday} {"turno" if appointments_tuesday == 1 else "turnos"} ocupados - {available_appts_tuesday} {"turno" if available_appts_tuesday == 1 else "turnos"} libres"
            )
            if appointments_monday > appointments_tuesday:
                print("El lunes es el día con más turnos.")
            elif appointments_monday < appointments_tuesday:
                print("El martes es el día con más turnos.")
            else:
                print(
                    f"Ambos dias con la misma cantidad de turnos ({appointments_monday})."
                )

        # Salir
        case "5":
            print("Gracias por usar nuestro sistema.")
            break

        case _:
            print("Opcion inválida. Intente nuevamente.")
