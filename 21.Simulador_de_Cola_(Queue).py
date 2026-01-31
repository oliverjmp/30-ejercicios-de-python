# =============================================================
# MEGA PROYECTO — EJERCICIO 21: SISTEMA COMPLETO DE COLAS (QUEUE)
# Autor: Oliver Javier Morales Pérez
# Descripción:
#   Este archivo contiene:
#       ✔ Ejercicio base (cola FIFO)
#       ✔ Cola con capacidad máxima
#       ✔ Cola circular optimizada
#       ✔ Cola de prioridad
#       ✔ Simulación de supermercado
#       ✔ Interfaz gráfica (GUI)
#       ✔ Menú para elegir variante
#
#   Cada variante está documentada con comentarios profesionales
#   explicando para qué sirve y dónde se usa en la vida real.
# =============================================================


# =============================================================
# VARIANTE BASE — COLA FIFO CLÁSICA
# =============================================================
# Esta es la implementación básica de una cola (queue).
# FIFO = First In, First Out.
# Se usa en:
#   - Procesos de sistemas operativos
#   - Impresoras
#   - Atención al cliente
#   - Simulaciones
# =============================================================

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        self.items.append(elemento)
        print(f"'{elemento}' agregado a la cola.")

    def dequeue(self):
        if self.is_empty():
            return "La cola está vacía."
        return f"Elemento eliminado: {self.items.pop(0)}"

    def peek(self):
        if self.is_empty():
            return "La cola está vacía."
        return f"Primer elemento: {self.items[0]}"

    def is_empty(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Cola actual:", self.items if self.items else "Vacía")



# =============================================================
# VARIANTE 1 — COLA CON CAPACIDAD MÁXIMA
# =============================================================
# Simula colas reales con límite:
#   - Estacionamientos
#   - Buffers de red
#   - Colas de impresión
# Practicas:
#   - Validación
#   - Manejo de errores
#   - Diseño robusto
# =============================================================

class ColaLimitada:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad

    def enqueue(self, elemento):
        if len(self.items) >= self.capacidad:
            print("La cola está llena.")
        else:
            self.items.append(elemento)
            print(f"'{elemento}' agregado.")

    def dequeue(self):
        if not self.items:
            print("La cola está vacía.")
        else:
            print("Eliminado:", self.items.pop(0))

    def mostrar(self):
        print("Cola:", self.items)



# =============================================================
# VARIANTE 2 — COLA CIRCULAR (OPTIMIZADA)
# =============================================================
# Evita usar pop(0), que es lento.
# Se usa en:
#   - Sistemas operativos
#   - Buffers de audio/video
#   - Hardware
# Practicas:
#   - Optimización
#   - Índices modulares
# =============================================================

class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamano = 0

    def enqueue(self, elemento):
        if self.tamano == self.capacidad:
            print("Cola llena.")
            return
        self.items[self.final] = elemento
        self.final = (self.final + 1) % self.capacidad
        self.tamano += 1
        print(f"'{elemento}' agregado.")

    def dequeue(self):
        if self.tamano == 0:
            print("Cola vacía.")
            return
        elemento = self.items[self.frente]
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        print("Eliminado:", elemento)

    def mostrar(self):
        print("Cola circular:", self.items)



# =============================================================
# VARIANTE 3 — COLA DE PRIORIDAD
# =============================================================
# El elemento con mayor prioridad sale primero.
# Se usa en:
#   - Hospitales
#   - Algoritmos de búsqueda (A*, Dijkstra)
#   - Planificación de procesos
# Practicas:
#   - Ordenamiento dinámico
#   - Estructuras avanzadas
# =============================================================

class ColaPrioridad:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento, prioridad):
        self.items.append((elemento, prioridad))
        self.items.sort(key=lambda x: x[1], reverse=True)
        print(f"'{elemento}' agregado con prioridad {prioridad}.")

    def dequeue(self):
        if not self.items:
            print("Cola vacía.")
        else:
            print("Eliminado:", self.items.pop(0))

    def mostrar(self):
        print("Cola de prioridad:", self.items)



# =============================================================
# VARIANTE 4 — SIMULACIÓN DE SUPERMERCADO
# =============================================================
# Simula un sistema real:
#   - Tiempos de espera
#   - Clientes atendidos
#   - Congestión
# Practicas:
#   - Modelado de sistemas
#   - Simulación por eventos
#   - Estadística básica
# =============================================================

import random
import time

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiempo = random.randint(2, 6)

class Supermercado:
    def __init__(self):
        self.cola = []

    def llega_cliente(self, nombre):
        cliente = Cliente(nombre)
        self.cola.append(cliente)
        print(f"Llega {nombre} (tiempo: {cliente.tiempo}s)")

    def atender(self):
        if not self.cola:
            print("No hay clientes.")
            return
        cliente = self.cola.pop(0)
        print(f"Atendiendo a {cliente.nombre}...")
        time.sleep(cliente.tiempo)
        print(f"{cliente.nombre} atendido.")



# =============================================================
# VARIANTE 5 — INTERFAZ GRÁFICA (GUI)
# =============================================================
# Convierte la cola en una aplicación visual.
# Practicas:
#   - Tkinter
#   - Eventos
#   - Visualización de estructuras
# =============================================================

import tkinter as tk

class ColaGUI:
    def __init__(self):
        self.cola = []
        self.ventana = tk.Tk()
        self.ventana.title("Cola GUI")

        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        tk.Button(self.ventana, text="Enqueue", command=self.enqueue).pack()
        tk.Button(self.ventana, text="Dequeue", command=self.dequeue).pack()

        self.lista = tk.Label(self.ventana, text="")
        self.lista.pack()

        self.ventana.mainloop()

    def enqueue(self):
        elemento = self.entrada.get()
        self.cola.append(elemento)
        self.actualizar()

    def dequeue(self):
        if self.cola:
            self.cola.pop(0)
        self.actualizar()

    def actualizar(self):
        self.lista.config(text=str(self.cola))



# =============================================================
# MENÚ PRINCIPAL — ELEGIR VARIANTE
# =============================================================

def menu():
    while True:
        print("\n=== SISTEMA DE COLAS — MEGA PROYECTO ===")
        print("1. Cola FIFO básica")
        print("2. Cola con capacidad máxima")
        print("3. Cola circular optimizada")
        print("4. Cola de prioridad")
        print("5. Simulación de supermercado")
        print("6. Interfaz gráfica (GUI)")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cola = Cola()
            cola.enqueue("A")
            cola.enqueue("B")
            cola.mostrar()
            print(cola.dequeue())

        elif opcion == "2":
            cola = ColaLimitada(3)
            cola.enqueue("A")
            cola.enqueue("B")
            cola.enqueue("C")
            cola.enqueue("D")
            cola.mostrar()

        elif opcion == "3":
            cola = ColaCircular(3)
            cola.enqueue("A")
            cola.enqueue("B")
            cola.enqueue("C")
            cola.dequeue()
            cola.enqueue("D")
            cola.mostrar()

        elif opcion == "4":
            cola = ColaPrioridad()
            cola.enqueue("Paciente normal", 1)
            cola.enqueue("Emergencia", 10)
            cola.enqueue("Urgencia", 5)
            cola.mostrar()
            cola.dequeue()

        elif opcion == "5":
            market = Supermercado()
            market.llega_cliente("Ana")
            market.llega_cliente("Luis")
            market.atender()
            market.atender()

        elif opcion == "6":
            ColaGUI()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

menu()

