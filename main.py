from modulos import *

def menu_principal():
    while True:
        print("=== Menú Principal ===")
        print("1. Crear usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        print("=====================")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            if iniciar_sesion():
                dispositivos_menu()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción no valida.\n")


if __name__ == "__main__":
    menu_principal()
