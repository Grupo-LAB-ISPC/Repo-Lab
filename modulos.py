usuarios = {}
dispositivos = {}
automatizaciones_activas = []

#Gestor de usuarios
 
def menu_sesion():
    while True:
        print("1. Crear usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        print("=====================")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            iniciar_sesion()
        else:
            print("Opcion no valida.\n")

def crear_usuario():
    usuario = input("Crear nuevo nombre de usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe.")
        print("=====================\n")
        return

    contrasena = input("Crear contraseña: ")
    if not usuarios:
        rol = "admin"
        print("Primer usuario registrado. Asignado como ADMIN.")
    else:
        rol = "estandar"

    usuarios[usuario] = {"contrasena": contrasena, "rol": rol}
    print(f"Usuario creado correctamente con rol '{rol}'.")
    print("=====================\n")

def iniciar_sesion():
    while True:
        usuario = input("Nombre de usuario: ")
        if usuario not in usuarios:
            print("Usuario inexistente.")
            print("=====================\n")
            continue
        
        contrasena = input("Contraseña: ")
        if usuarios[usuario] == contrasena:
            print("=====================")
            print("Inicio de sesión exitoso. ¡Bienvenido!\n")
            return True 
        else:
            print("=====================")
            print("Contraseña incorrecta. Intente nuevamente.\n")

def menu_estandar(usuario):
    while True:
        print("=== Menú Usuario Estándar ===")
        print("1. Consultar datos personales")
        print("2. Ejecutar automatización predefinida (modo ahorro)")
        print("3. Consultar dispositivos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        print("=====================")

        if opcion == "1":
            ver_datos_personales(usuario)
        elif opcion == "2":
            modo_ahorro_energia()
        elif opcion == "3":
            mostrar_dispositivos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.\n")


def menu_admin(usuario):
    while True:
        print("=== Menú Admin ===")
        print("1. Gestionar dispositivos")
        print("2. Consultar automatizaciones activas")
        print("3. Modificar rol de un usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        print("=====================")

        if opcion == "1":
            dispositivos_menu()
        elif opcion == "2":
            consultar_automatizaciones()
        elif opcion == "3":
            modificar_rol_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.\n")

#Gestor de dispositivos

def mostrar_dispositivos():
    if not dispositivos:
        print("No hay dispositivos registrados.")
        print("=====================\n")
        return
    
    print("Lista de dispositivos:\n")
    for nombre, datos in dispositivos.items():
        print("=====================")
        print(f"Nombre: {nombre}")
        print(f"  Tipo: {datos['tipo']}")
        print(f"  Esencial: {datos['esencial']}")
        print(f"  Estado: {datos['estado']}")
        print("=====================\n")

def agregar_dispositivo():
    nombre = input("Nombre del dispositivo: ")
    if nombre in dispositivos:
        print("El dispositivo ya existe.")
        print("=====================\n")
        return

    print("Tipos recomendados: (Electrodoméstico, Iluminación, Climatización, Entretenimiento, Computación, Seguridad)")
    tipo = input("Tipo de dispositivo: ")

    esencial = input("¿Es esencial? (sí/no): ").strip().lower()
    while esencial not in ["sí", "si", "no"]:
        esencial = input("Entrada inválida. ¿Es esencial? (sí/no): ").strip().lower()

    estado = input("Estado del dispositivo (prendido/apagado): ").strip().lower()
    while estado not in ["prendido", "apagado"]:
        estado = input("Entrada inválida. Estado (prendido/apagado): ").strip().lower()

    dispositivos[nombre] = {
        "tipo": tipo,
        "esencial": "sí" if esencial in ["sí", "si"] else "no",
        "estado": estado
    }
    print("Dispositivo agregado correctamente.")
    print("=====================\n")

def eliminar_dispositivo():
    if not dispositivos:
        print("No hay dispositivos para eliminar.")
        print("=====================\n")
        return

    print("Dispositivos disponibles:")
    for nombre in dispositivos:
        print(f"- {nombre}")
    
    nombre = input("Nombre del dispositivo a eliminar: ")
    if nombre in dispositivos:
        del dispositivos[nombre]
        print(f"Dispositivo '{nombre}' eliminado correctamente.")
        print("=====================\n")
    else:
        print("El dispositivo no existe.")
        print("=====================\n")

def modo_ahorro_energia():
    if not dispositivos:
        print("No hay dispositivos para aplicar el modo ahorro.")
        print("=====================\n")
        return

    for nombre, datos in dispositivos.items():
        if datos["esencial"] == "sí" and datos["estado"] == "apagado":
            datos["estado"] = "prendido"
            print(f"Dispositivo esencial '{nombre}' encendido.")
        elif datos["esencial"] == "no" and datos["estado"] == "prendido":
            datos["estado"] = "apagado"
            print(f"Dispositivo no esencial '{nombre}' apagado.")
    
    print("Modo ahorro de energía aplicado.")
    print("=====================\n")
    automatizaciones_activas.append("Modo ahorro de energía activado")
    print("Estado actual de los dispositivos: ")
    mostrar_dispositivos()
    print("=====================\n")

def dispositivos_menu():
    while True:
        print("===Gestor de Dispositivos===")
        print("1. Mostrar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Activar modo ahorro de energia")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        print("=====================")

        if opcion == "1":
            mostrar_dispositivos()
        elif opcion == "2":
            agregar_dispositivo()
        elif opcion == "3":
            eliminar_dispositivo()
        elif opcion == "4":
            modo_ahorro_energia()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no valida.\n")
            
def consultar_automatizaciones():
    if not automatizaciones_activas:
        print("No hay automatizaciones activas.")
    else:
        print("Automatizaciones activas:")
        for auto in automatizaciones_activas:
            print(f"- {auto}")
    print("=====================\n")

