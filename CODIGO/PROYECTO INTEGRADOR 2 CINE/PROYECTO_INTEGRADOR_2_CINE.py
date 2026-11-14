asientos = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def mostrar_sala():
    print("\n=======================================")
    print("           PANTALLA DEL CINE")
    print("=======================================")
    print("       Col 0  Col 1  Col 2  Col 3  Col 4")
    
    for indice_fila in range(len(asientos)):
        fila_visual = f"Fila {indice_fila} "
        for asiento in asientos[indice_fila]:
            if asiento == 0:
                fila_visual += "[ L ]  "
            else:
                fila_visual += "[ X ]  "
        print(fila_visual)
    print("\nL = Libre  |  X = Ocupado")
    print("=======================================")

def reservar_asiento():
    print("\n--- RESERVAR UN ASIENTO ---")
    try:
        fila = int(input("Ingresa el número de fila (0-4): "))
        columna = int(input("Ingresa el número de columna (0-4): "))
        
        if 0 <= fila <= 4 and 0 <= columna <= 4:
            if asientos[fila][columna] == 0:
                asientos[fila][columna] = 1 
                print("Exito: Asiento reservado")
            else:
                print("Error: Asiento ocupado")
        else:
            print("Error: Las coordenadas están fuera de rango.")
    except ValueError:
        print("Error: Debes ingresar números enteros.")

def liberar_asiento():
    print("\n--- LIBERAR UN ASIENTO ---")
    try:
        fila = int(input("Ingresa el número de fila (0-4): "))
        columna = int(input("Ingresa el número de columna (0-4): "))
        
        if 0 <= fila <= 4 and 0 <= columna <= 4:
            if asientos[fila][columna] == 1:
                asientos[fila][columna] = 0
                print("Exito: Liberado con éxito.")
            else:
                print("Aviso: El asiento ya estaba libre.")
        else:
            print("Error: Las coordenadas están fuera de rango.")
    except ValueError:
        print("Error: Debes ingresar números enteros.")

def consultar_disponibilidad():
    print("\n--- CONSULTAR DISPONIBILIDAD ---")
    try:
        fila = int(input("Ingresa el número de fila (0-4): "))
        columna = int(input("Ingresa el número de columna (0-4): "))
        
        if 0 <= fila <= 4 and 0 <= columna <= 4:
            if asientos[fila][columna] == 0:
                print(f"El asiento en la fila {fila}, columna {columna} está LIBRE.")
            else:
                print(f"El asiento en la fila {fila}, columna {columna} está OCUPADO.")
        else:
            print("Error: Las coordenadas están fuera de rango.")
    except ValueError:
        print("Error: Debes ingresar números enteros.")

def ver_estadisticas():
    print("\n--- REPORTE DE OCUPACIÓN ---")
    libres = 0
    ocupados = 0
    total_asientos = 25

    for fila in asientos:
        for asiento in fila:
            if asiento == 0:
                libres += 1
            else:
                ocupados += 1

    porcentaje_ocupacion = (ocupados / total_asientos) * 100

    print(f"Asientos Disponibles: {libres}")
    print(f"Asientos Ocupados: {ocupados}")
    print(f"Porcentaje de Ocupación: {porcentaje_ocupacion}%")

def menu_principal():
    opcion = 0
    while opcion != 6:
        print("\n-----------------------------------")
        print("   SISTEMA DE TAQUILLA - CINE")
        print("-----------------------------------")
        print("1. Mostrar pantalla de la sala")
        print("2. Reservar un asiento")
        print("3. Cancelar / Liberar asiento")
        print("4. Consultar estado de un asiento")
        print("5. Ver reporte de ocupación")
        print("6. Salir del sistema")
        print("-----------------------------------")
        
        try:
            opcion = int(input("Elige una opción (1-6): "))
            
            if opcion == 1:
                mostrar_sala()
            elif opcion == 2:
                reservar_asiento()
            elif opcion == 3:
                liberar_asiento()
            elif opcion == 4:
                consultar_disponibilidad()
            elif opcion == 5:
                ver_estadisticas()
            elif opcion == 6:
                print("\nSaliendo del sistema. ¡Hasta luego!")
            else:
                print("Opción no válida. Elige un número del 1 al 6.")
        except ValueError:
            print("Error: Ingresa solo valores numéricos.")

if __name__ == "__main__":
    menu_principal()