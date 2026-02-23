# =========================
# 1. Importar librerías
# =========================
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# =========================
# 2. Crear dataset de ejemplo
# =========================
# Representación one-hot de comida
# [tacos, pizza, hotdog, hamburguesa]

X = np.array([
    [1,0,0,0],  # Tacos
    [0,1,0,0],  # Pizza
    [0,0,1,0],  # Hotdog
    [0,0,0,1],  # Hamburguesa
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
])

# Etiquetas numéricas
# 0 = Tacos
# 1 = Pizza
# 2 = Hotdog
# 3 = Hamburguesa
y = np.array([0,1,2,3,0,1,2,3])

# =========================
# 3. Dividir datos
# =========================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =========================
# 4. Crear modelo
# =========================
modelo = LogisticRegression()

# =========================
# 5. Entrenar modelo
# =========================
modelo.fit(X_train, y_train)


# =========================
# 6. Evaluar modelo
# =========================
y_pred = modelo.predict(X_test)
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))

# =========================
# 7. Probar con nueva entrada
# =========================

# Cambia aquí el arreglo para probar
comida = np.array([[1,0,0,0]])

prediccion = modelo.predict(comida)[0]

# Diccionario para traducir número a comida
clases = {
    0: "Tacos al pastor",
    1: "Pizza",
    2: "Hotdog",
    3: "Hamburguesa"
}

print("\nLa comida predicha es:", clases[prediccion])