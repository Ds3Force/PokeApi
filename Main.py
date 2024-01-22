import functions
def main():
    iniciar = input("¿Desea iniciar la aventura?: ")
    if iniciar.lower() == "si":
        mostrar_menu()
    else:
        print("Programa finalizado.")


def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Listar todos los Pokémon")
        print("2. Consultar información de un Pokémon")
        print("3. Comparar información de múltiples Pokémon")
        print("4. Calcular estadísticas de un Pokémon")
        print("5. Salir")

        opcion = input("Ingrese el número de opción que desea ejecutar: ")

        if opcion == "1":
            functions.listar_pokemon()
        elif opcion == "2":
            functions.consultar_pokemon()
        elif opcion == "3":
            functions.comparar_pokemon()
        elif opcion == "4":
            functions.calcular_estadisticas_multiples_pokemon()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número de opción válido.")


if __name__ == "__main__":
    main()

