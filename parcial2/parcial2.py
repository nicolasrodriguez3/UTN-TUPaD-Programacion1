def menu():
    print("1. Carga de herramientas")
    print("2. Visualizar inventario")
    print("3. Consulta de stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualización de stock")
    print("7. Salir")

    input_usuario = input("Ingrese una opción: ")
    return input_usuario

def main():
    inventario = {}

    while True:
        opcion = menu()

        if opcion == "1":
            # Carga de herramientas
            pass
        elif opcion == "2":
            # Visualizar inventario
            pass
        elif opcion == "3":
            # Consulta de stock
            pass
        elif opcion == "4":
            # Reporte de agotados
            pass
        elif opcion == "5":
            # Alta de nuevo producto
            pass
        elif opcion == "6":
            # Actualización de stock
            pass
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")