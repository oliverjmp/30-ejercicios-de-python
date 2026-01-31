# =============================================================
# MEGA PROYECTO — EJERCICIO 22: SISTEMA COMPLETO DE PILAS (STACK)
# Autor: Oliver Javier Morales Pérez
# Descripción:
#   Este archivo contiene:
#       ✔ Ejercicio base (pila LIFO)
#       ✔ Pila con capacidad máxima
#       ✔ Pila Undo/Redo (deshacer/rehacer)
#       ✔ Pila para validar paréntesis
#       ✔ Pila para evaluar expresiones matemáticas (postfija)
#       ✔ Interfaz gráfica (GUI)
#       ✔ Menú para elegir variante
#
#   Cada variante está documentada con comentarios profesionales
#   explicando para qué sirve y dónde se usa en la vida real.
# =============================================================


# =============================================================
# VARIANTE BASE — PILA LIFO CLÁSICA
# =============================================================
# Esta es la implementación básica de una pila (stack).
# LIFO = Last In, First Out.
# Se usa en:
#   - Navegadores (historial)
#   - Deshacer/rehacer
#   - Recursión
#   - Evaluación de expresiones
# =============================================================

class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)
        print(f"'{elemento}' agregado a la pila.")

    def pop(self):
        if self.is_empty():
            return "La pila está vacía."
        return f"Elemento eliminado: {self.items.pop()}"

    def peek(self):
        if self.is_empty():
            return "La pila está vacía."
        return f"Elemento superior: {self.items[-1]}"

    def is_empty(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Pila actual:", self.items if self.items else "Vacía")



# =============================================================
# VARIANTE 1 — PILA CON CAPACIDAD MÁXIMA
# =============================================================
# Simula memoria limitada.
# Se usa en:
#   - Sistemas embebidos
#   - Buffers
#   - Control de recursos
# =============================================================

class PilaLimitada:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad

    def push(self, elemento):
        if len(self.items) >= self.capacidad:
            print("La pila está llena.")
        else:
            self.items.append(elemento)
            print(f"'{elemento}' agregado.")

    def pop(self):
        if not self.items:
            print("La pila está vacía.")
        else:
            print("Eliminado:", self.items.pop())

    def mostrar(self):
        print("Pila:", self.items)



# =============================================================
# VARIANTE 2 — PILA UNDO/REDO (DESHACER/REHACER)
# =============================================================
# Simula el comportamiento de editores de texto.
# Se usa en:
#   - Word, Photoshop, VSCode
#   - Sistemas de edición
# Practicas:
#   - Manejo de dos pilas
#   - Estados reversibles
# =============================================================

class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def hacer(self, accion):
        self.undo_stack.append(accion)
        self.redo_stack.clear()
        print(f"Acción realizada: {accion}")

    def deshacer(self):
        if not self.undo_stack:
            print("Nada que deshacer.")
            return
        accion = self.undo_stack.pop()
        self.redo_stack.append(accion)
        print(f"Deshacer: {accion}")

    def rehacer(self):
        if not self.redo_stack:
            print("Nada que rehacer.")
            return
        accion = self.redo_stack.pop()
        self.undo_stack.append(accion)
        print(f"Rehacer: {accion}")

    def mostrar(self):
        print("Undo:", self.undo_stack)
        print("Redo:", self.redo_stack)



# =============================================================
# VARIANTE 3 — VALIDACIÓN DE PARÉNTESIS
# =============================================================
# Verifica si una expresión tiene paréntesis balanceados.
# Ejemplo:
#   ((a+b)*c) → válido
#   (a+b)) → inválido
# Se usa en:
#   - Compiladores
#   - Validación de código
#   - Análisis sintáctico
# =============================================================

class ValidadorParentesis:
    def validar(self, expresion):
        pila = []
        pares = {')': '(', ']': '[', '}': '{'}

        for char in expresion:
            if char in "([{":
                pila.append(char)
            elif char in ")]}":
                if not pila or pila.pop() != pares[char]:
                    return "Expresión inválida."
        return "Expresión válida." if not pila else "Expresión inválida."



# =============================================================
# VARIANTE 4 — EVALUACIÓN DE EXPRESIONES POSTFIJAS (RPN)
# =============================================================
# Ejemplo:
#   Entrada:  "5 1 2 + 4 * + 3 -"
#   Resultado: 14
# Se usa en:
#   - Calculadoras antiguas
#   - Compiladores
#   - Máquinas de pila
# Practicas:
#   - Operaciones con pila
#   - Parsing de expresiones
# =============================================================

class EvaluadorPostfijo:
    def evaluar(self, expresion):
        pila = []
        tokens = expresion.split()

        for token in tokens:
            if token.isdigit():
                pila.append(int(token))
            else:
                b = pila.pop()
                a = pila.pop()
                if token == '+': pila.append(a + b)
                elif token == '-': pila.append(a - b)
                elif token == '*': pila.append(a * b)
                elif token == '/': pila.append(a / b)

        return pila.pop()



# =============================================================
# VARIANTE 5 — INTERFAZ GRÁFICA (GUI)
# =============================================================
# Visualiza la pila en una ventana.
# Practicas:
#   - Tkinter
#   - Eventos
#   - Diseño visual
# =============================================================

import tkinter as tk

class PilaGUI:
    def __init__(self):
        self.pila = []
        self.ventana = tk.Tk()
        self.ventana.title("Pila GUI")

        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        tk.Button(self.ventana, text="Push", command=self.push).pack()
        tk.Button(self.ventana, text="Pop", command=self.pop).pack()

        self.lista = tk.Label(self.ventana, text="")
        self.lista.pack()

        self.ventana.mainloop()

    def push(self):
        elemento = self.entrada.get()
        self.pila.append(elemento)
        self.actualizar()

    def pop(self):
        if self.pila:
            self.pila.pop()
        self.actualizar()

    def actualizar(self):
        self.lista.config(text=str(self.pila))



# =============================================================
# MENÚ PRINCIPAL — ELEGIR VARIANTE
# =============================================================

def menu():
    while True:
        print("\n=== SISTEMA DE PILAS — MEGA PROYECTO ===")
        print("1. Pila LIFO básica")
        print("2. Pila con capacidad máxima")
        print("3. Sistema Undo/Redo")
        print("4. Validador de paréntesis")
        print("5. Evaluador de expresiones postfijas")
        print("6. Interfaz gráfica (GUI)")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            pila = Pila()
            pila.push("A")
            pila.push("B")
            pila.mostrar()
            print(pila.pop())

        elif opcion == "2":
            pila = PilaLimitada(2)
            pila.push("A")
            pila.push("B")
            pila.push("C")
            pila.mostrar()

        elif opcion == "3":
            sistema = UndoRedo()
            sistema.hacer("Escribir texto")
            sistema.hacer("Borrar palabra")
            sistema.deshacer()
            sistema.rehacer()
            sistema.mostrar()

        elif opcion == "4":
            val = ValidadorParentesis()
            print(val.validar("(a+b)*(c+d)"))
            print(val.validar("(a+b))"))

        elif opcion == "5":
            ev = EvaluadorPostfijo()
            print("Resultado:", ev.evaluar("5 1 2 + 4 * + 3 -"))

        elif opcion == "6":
            PilaGUI()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

menu()
