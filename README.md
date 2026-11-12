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
# DIA 3 
    Diseñar la "Pantalla" de Asientos 
    ===================================
          PANTALLA DEL CINE 
    ===================================
      Col 0  Col 1  Col 2  Col 3  Col 4
Fila 0 [ L ]  [ L ]  [ L ]  [ L ]  [ L ]
Fila 1 [ L ]  [ X ]  [ X ]  [ L ]  [ L ]
Fila 2 [ L ]  [ L ]  [ L ]  [ L ]  [ L ]
Fila 3 [ L ]  [ X ]  [ X ]  [ X ]  [ L ]
Fila 4 [ L ]  [ L ]  [ L ]  [ L ]  [ L ]

L = Libre  |  X = Ocupado
=======================================
# Menú Principal
-----------------------------------
   SISTEMA DE TAQUILLA - CINE
-----------------------------------
1. Ver asientos disponibles
2. Reservar un asiento
3. Cancelar / Liberar asiento
4. Ver reporte de ocupación (%)
5. Salir del sistema
-----------------------------------
Elige una opción (1-5): _
Los Mensajes y Preguntas (Interacción)
Cuando elige reservar (Opción 2):

Programa dice: Ingresa el número de fila (0-4):

Programa dice: Ingresa el número de columna (0-4):

Respuesta de Éxito: Asiento reservado exitosamente.

Respuesta de Error: asiento ya está ocupado.

Cuando elige ver estadísticas (Opción 4):

Programa dice:
REPORTE DE ESTADÍSTICAS:
Asientos ocupados: 5
Asientos libres: 20
Ocupación de la sala: 20.0%
