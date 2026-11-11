# PROYECTO 2 

 DIA 1 : Análisis del problema.Identificación de entradas, procesos y salidas.
  Sistema de Administración de Asientos de Cine

  Descripción del Proyecto
Este proyecto es un sistema interactivo diseñado para automatizar y gestionar la reserva, liberación y disponibilidad de asientos en una sala de cine mediante una estructura de datos matricial. El objetivo principal es evitar la duplicidad de reservaciones y proveer estadísticas de ocupación en tiempo real.

---
  Integrantes del Equipo
[PABLO JOSEPH RENTERIA HERNANDEZ]** - 24731440 / Usuario GitHub: `@[24731440]`
[ISAAC CATALAN GUTIERREZ]** - 24725649 / Usuario GitHub: `@[24725649]`

---

 Tecnologías Utilizadas
Lenguaje de Programación:** [C / C++ / Java / Python / C#] (Especificar la versión, ej. Python 3.10)
Entorno de Desarrollo (IDE):** [Visual Studio Code / NetBeans / CLion]
Control de Versiones:** Git & GitHub

# DIA NUMERO 2 : Diseño del sistema. Creación de diagramas de flujo y pseudocódigo.
  Sistema de Administración de Asientos de Cine
  Descripción del Proyecto
  Algoritmo Cine
    Definir Asientos[5][5] Como Entero // Una matriz de 5x5
    Llenar Asientos con 0 // 0 = Disponible, 1 = Ocupado
    
    Repetir
        Imprimir "--- MENÚ CINE ---"
        Imprimir "1. Mostrar asientos"
        Imprimir "2. Reservar asiento"
        Imprimir "3. Liberar asiento"
        Imprimir "4. Estadísticas"
        Imprimir "5. Salir"
        Leer Opcion
        
        Segun Opcion Hacer
            Caso 1:
                Llamar a MostrarMatriz()
            Caso 2:
                Imprimir "Dime fila y columna a reservar:"
                Leer fila, columna
                Si Asientos[fila][columna] == 0 Entonces
                    Asientos[fila][columna] = 1
                    Imprimir "Reservado con éxito"
                Sino
                    Imprimir "Ya está ocupado"
                Fin Si
            // ... (Se hace la misma lógica para el caso 3 y 4)
        Fin Segun
    Hasta Que Opcion == 5