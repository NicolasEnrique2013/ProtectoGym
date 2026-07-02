# 2. MODULARIZACIÓN (Las funciones del sistema)
def registrar_socio():
    print("--- Registrar Socio ---")
    # Acá van las validaciones (que el DNI sea número, etc.)
    pass

def registrar_asistencia():
    print("--- Control de Asistencia ---")
    pass

def mostrar_estadisticas():
    print("--- Estadísticas ---")
    pass
# MENÚ PRINCIPAL (Estructuras de Control)
def menu_principal():
    while True:
        print("\n--- GESTIÓN DE GIMNASIO ---")
        print("1. Registrar Socio")
        print("2. Control de Asistencia")
        print("3. Ver Estadísticas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_socio()
        elif opcion == "2":
            registrar_asistencia()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break  # Rompe el bucle while y cierra el programa
        else:
            print("Opción inválida. Intente de nuevo.")

# Para que el programa empiece a correr
menu_principal()