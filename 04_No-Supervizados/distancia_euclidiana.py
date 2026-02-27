# =========================================
# DISTANCIA EUCLIDIANA PASO A PASO
# Script didáctico para Google Colab
# =========================================

# Importar librerías necesarias
import math
import numpy as np
import matplotlib.pyplot as plt

# =========================================
# FASE 1: Definir los puntos
# =========================================
# Punto A
x1, y1 = 1, 2

# Punto B
x2, y2 = 7, 6

print("FASE 1: Definición de puntos")
print("Punto A =", (x1, y1))
print("Punto B =", (x2, y2))
print()

# =========================================
# FASE 2: Calcular diferencias
# =========================================
dx = x2 - x1
dy = y2 - y1

print("FASE 2: Diferencias")
print("Δx =", dx)
print("Δy =", dy)
print()

# =========================================
# FASE 3: Elevar al cuadrado
# =========================================
dx2 = dx**2
dy2 = dy**2

print("FASE 3: Cuadrados")
print("Δx² =", dx2)
print("Δy² =", dy2)
print()

# =========================================
# FASE 4: Sumar cuadrados
# =========================================
suma = dx2 + dy2
print("FASE 4: Suma de cuadrados =", suma)
print()

# =========================================
# FASE 5: Raíz cuadrada (Distancia Euclidiana)
# =========================================
distancia = math.sqrt(suma)
print("FASE 5: Distancia Euclidiana =", round(distancia, 4))
print()

# =========================================
# FASE 6: Calcular pendiente
# =========================================
pendiente = dy / dx
print("Pendiente de la recta =", round(pendiente, 4))
print()

# =========================================
# FASE 7: Graficar
# =========================================

# Generar valores para la recta
x_vals = np.linspace(x1, x2, 100)
y_vals = y1 + pendiente * (x_vals - x1)

plt.figure()
plt.plot(x_vals, y_vals)
plt.scatter([x1, x2], [y1, y2])

plt.title("Distancia Euclidiana entre dos puntos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)

plt.show()