# =============================================================
# MEGA PROYECTO — EJERCICIO 23: SISTEMA COMPLETO DE CONJUNTOS (SET)
# Autor: Oliver Javier Morales Pérez
# Descripción:
#   Este archivo contiene:
#       ✔ Ejercicio base (operaciones de conjuntos)
#       ✔ Conjuntos numéricos con validación
#       ✔ Conjuntos múltiples (entrada por lotes)
#       ✔ Conjuntos aleatorios
#       ✔ Diagramas de Venn (requiere matplotlib)
#       ✔ Guardar y cargar conjuntos desde archivo
#       ✔ Menú para elegir variante
#
#   Cada variante está documentada con comentarios profesionales
#   explicando para qué sirve y dónde se usa en la vida real.
# =============================================================


# =============================================================
# VARIANTE BASE — OPERACIONES CLÁSICAS DE CONJUNTOS
# =============================================================

class ConjuntosBase:
    def __init__(self):
        self.A = set()
        self.B = set()

    def agregar_A(self, elemento):
        self.A.add(elemento)
        print(f"'{elemento}' agregado a A.")

    def agregar_B(self, elemento):
        self.B.add(elemento)
        print(f"'{elemento}' agregado a B.")

    def mostrar(self):
        print("Conjunto A:", self.A)
        print("Conjunto B:", self.B)

    def union(self):
        print("A ∪ B =", self.A.union(self.B))

    def interseccion(self):
        print("A ∩ B =", self.A.intersection(self.B))

    def diferencia(self):
        print("A - B =", self.A.difference(self.B))

    def diferencia_simetrica(self):
        print("A Δ B =", self.A.symmetric_difference(self.B))

    def subconjunto(self):
        print("¿A es subconjunto de B?:", self.A.issubset(self.B))



# =============================================================
# VARIANTE 1 — CONJUNTOS NUMÉRICOS CON VALIDACIÓN
# =============================================================

class ConjuntosNumericos:
    def __init__(self):
        self.A = set()
        self.B = set()

    def agregar(self, conjunto, valor):
        try:
            numero = float(valor)
            if conjunto == "A":
                self.A.add(numero)
            else:
                self.B.add(numero)
            print(f"{numero} agregado a {conjunto}.")
        except:
            print("Error: solo se permiten números.")

    def mostrar(self):
        print("A:", self.A)
        print("B:", self.B)



# =============================================================
# VARIANTE 2 — AGREGAR MÚLTIPLES ELEMENTOS (ENTRADA POR LOTES)
# =============================================================

class ConjuntosMultiples:
    def __init__(self):
        self.A = set()
        self.B = set()

    def agregar_lote(self, conjunto, texto):
        elementos = [e.strip() for e in texto.split(",")]
        if conjunto == "A":
            self.A.update(elementos)
        else:
            self.B.update(elementos)
        print("Elementos agregados correctamente.")

    def mostrar(self):
        print("A:", self.A)
        print("B:", self.B)



# =============================================================
# VARIANTE 3 — CONJUNTOS ALEATORIOS
# =============================================================

import random

class ConjuntosAleatorios:
    def __init__(self):
        self.A = set()
        self.B = set()

    def generar(self, tamA, tamB):
        self.A = {random.randint(1, 50) for _ in range(tamA)}
        self.B = {random.randint(1, 50) for _ in range(tamB)}
        print("Conjuntos generados.")

    def mostrar(self):
        print("A:", self.A)
        print("B:", self.B)



# =============================================================
# VARIANTE 4 — DIAGRAMA DE VENN (REQUIERE MATPLOTLIB)
# =============================================================

try:
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn2

    class DiagramaVenn:
        def __init__(self):
            self.A = set()
            self.B = set()

        def agregar_A(self, elemento):
            self.A.add(elemento)

        def agregar_B(self, elemento):
            self.B.add(elemento)

        def mostrar(self):
            venn2([self.A, self.B], set_labels=("A", "B"))
            plt.show()

except:
    DiagramaVenn = None



# =============================================================
# VARIANTE 5 — GUARDAR Y CARGAR CONJUNTOS DESDE ARCHIVO
# =============================================================

class ConjuntosArchivo:
    def __init__(self):
        self.A = set()
        self.B = set()

    def guardar(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(",".join(self.A) + "\n")
            f.write(",".join(self.B))
        print("Conjuntos guardados.")

    def cargar(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                lineas = f.readlines()
                self.A = set(lineas[0].strip().split(","))
                self.B = set(lineas[1].strip().split(","))
            print("Conjuntos cargados.")
        except:
            print("Error al cargar archivo.")

    def mostrar(self):
        print("A:", self.A)
        print("B:", self.B)



# =============================================================
# MENÚ PRINCIPAL — ELEGIR VARIANTE
# =============================================================

def menu():
    while True:
        print("\n=== SISTEMA DE CONJUNTOS — MEGA PROYECTO ===")
        print("1. Conjuntos base")
        print("2. Conjuntos numéricos")
        print("3. Agregar múltiples elementos")
        print("4. Conjuntos aleatorios")
        print("5. Diagrama de Venn")
        print("6. Guardar y cargar conjuntos")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            c = ConjuntosBase()
            c.agregar_A("a")
            c.agregar_A("b")
            c.agregar_B("b")
            c.agregar_B("c")
            c.mostrar()
            c.union()
            c.interseccion()
            c.diferencia()
            c.diferencia_simetrica()
            c.subconjunto()

        elif opcion == "2":
            c = ConjuntosNumericos()
            c.agregar("A", "10")
            c.agregar("A", "5.5")
            c.agregar("B", "3")
            c.agregar("B", "hola")
            c.mostrar()

        elif opcion == "3":
            c = ConjuntosMultiples()
            c.agregar_lote("A", "a, b, c, d")
            c.agregar_lote("B", "c, d, e")
            c.mostrar()

        elif opcion == "4":
            c = ConjuntosAleatorios()
            c.generar(5, 5)
            c.mostrar()

        elif opcion == "5":
            if DiagramaVenn is None:
                print("Matplotlib o matplotlib_venn no están instalados.")
            else:
                c = DiagramaVenn()
                c.agregar_A("a")
                c.agregar_A("b")
                c.agregar_B("b")
                c.agregar_B("c")
                c.mostrar()

        elif opcion == "6":
            c = ConjuntosArchivo()
            c.A = {"a", "b", "c"}
            c.B = {"c", "d"}
            c.guardar("conjuntos.txt")
            c.cargar("conjuntos.txt")
            c.mostrar()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

menu()
