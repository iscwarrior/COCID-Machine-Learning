# =========================
# 1. Importar librerías
# =========================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =========================
# 2. Crear datos ficticios
# =========================

# Años de 2000 a 2025
years = np.arange(2000, 2026)

# Generamos crecimiento lineal desde 17000 hasta 31000
deaths = np.linspace(17000, 31000, len(years))

# Convertimos a formato columna (requerido por sklearn)
X = years.reshape(-1, 1)
y = deaths

# =========================
# 3. Crear y entrenar modelo
# =========================
model = LinearRegression()
model.fit(X, y)

# =========================
# 4. Obtener ecuación
# =========================
slope = model.coef_[0]
intercept = model.intercept_

print("Ecuación del modelo:\n")
print(f"Defunciones = {intercept:.2f} + ({slope:.2f} * Año)")

# =========================
# 5. Predicción para 2030
# =========================
year_2030 = np.array([[2030]])
prediction_2030 = model.predict(year_2030)

print("\nPredicción para 2030:")
print(f"{prediction_2030[0]:,.0f} defunciones")

# =========================
# 6. Graficar resultados
# =========================

# Generamos línea extendida hasta 2030
years_extended = np.arange(2000, 2031).reshape(-1,1)
predictions_extended = model.predict(years_extended)

plt.figure()
plt.scatter(years, deaths)
plt.plot(years_extended, predictions_extended)
plt.xlabel("Año")
plt.ylabel("Número de defunciones")
plt.title("Regresión Lineal - Defunciones por Cáncer de Mama")
plt.show()