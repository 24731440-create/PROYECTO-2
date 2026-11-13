# Sistema de Administración de Asientos de Cine
# Proyecto Integrador - Módulo de Captura

# 1. Implementación del arreglo (Matriz 5x5)
# Inicializamos todos los asientos en 0 (Disponibles)
asientos = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def mostrar_sala():
    """Recorre la matriz y muestra el estado visual de los asientos."""
    print("\n=======================================")
    print("           PANTALLA DEL CINE")
    print("=======================================")
    print("       Col 0  Col 1  Col 2  Col 3  Col 4")
    
    for indice_fila in range(len(asientos)):
        fila_visual = f"Fila {indice_fila} "
        for asiento in asientos[indice_fila]:
            if asiento == 0:
                fila_visual += "[ L ]  " # Libre
            else:
                fila_visual += "[ X ]  " # Ocupado
        print(fila_visual)
    print("\nL = Libre  |  X = Ocupado")
    print("=======================================")

def reservar_asiento():
    """Captura datos para reservar y valida que las coordenadas sean correctas."""
    print("\n--- RESERVAR UN ASIENTO ---")
    try:
        fila = int(input("Ingresa el número de fila (0-4): "))
        columna = int(input("Ingresa el número de columna (0-4): "))
        
        if 0 <= fila <= 4 and 0 <= columna <= 4:
            if asientos[fila][columna] == 0:
                asientos[fila][columna] = 1
                print(" Éxito: Asiento reservado.")
            else:
                print(" Error: El asiento ya está ocupado.")
        else:
            print(" Error: Las coordenadas están fuera de rango (deben ser de 0 a 4).")
    except ValueError:
        print(" Error: Debes ingresar números enteros válidos.")

def liberar_asiento():
    """Captura datos para liberar un asiento y valida la acción."""
    print("\n--- LIBERAR UN ASIENTO ---")
    try:
        fila = int(input("Ingresa el número de fila (0-4): "))
        columna = int(input("Ingresa el número de columna (0-4): "))
        
        # Validación de rango
        if 0 <= fila <= 4 and 0 <= columna <= 4:
            if asientos[fila][columna] == 1:
                asientos[fila][columna] = 0 # Cambiamos de Ocupado a Libre
                print(" Éxito: Asiento liberado con éxito.")
            else:
                print(" Aviso: El asiento ya estaba libre.")
        else:
            print(" Error: Las coordenadas están fuera de rango (deben ser de 0 a 4).")
    except ValueError:
        print(" Error: Debes ingresar números enteros válidos.")

def menu_principal():
    """Menú interactivo principal del sistema."""
    opcion = 0
    while opcion != 5:
        print("\n-----------------------------------")
        print("   SISTEMA DE TAQUILLA - CINE")
        print("-----------------------------------")
        print("1. Ver asientos disponibles")
        print("2. Reservar un asiento")
        print("3. Cancelar / Liberar asiento")
        print("4. Ver reporte de ocupación ")
        print("5. Salir del sistema")
        print("-----------------------------------")
        
        try:
            opcion = int(input("Elige una opción (1-5): "))
            
            if opcion == 1:
                mostrar_sala()
            elif opcion == 2:
                reservar_asiento()
            elif opcion == 3:
                liberar_asiento()
            elif opcion == 4:
                print("\nEn desarrollo... (Módulo de estadísticas)")
            elif opcion == 5:
                print("\nSaliendo del sistema. ¡Hasta luego!")
            else:
                print(" Opción no válida. Elige un número del 1 al 5.")
        except ValueError:
            print(" Error: Ingresa solo valores numéricos.")

# Punto de inicio del programa
if __name__ == "__main__":
    menu_principal()
