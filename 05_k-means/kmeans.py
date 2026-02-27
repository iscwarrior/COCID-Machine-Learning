# ================================
# EJEMPLO K-MEANS
# ================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# -------------------------------
# FASE 1: Generar datos sintéticos
# -------------------------------
# Creamos 300 puntos con 3 grupos reales
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

plt.scatter(X[:, 0], X[:, 1])
plt.title("Datos originales (sin etiquetas visibles)")
plt.show()


# -------------------------------
# FASE 2: Elegir número de clusters (K)
# -------------------------------
k = 3


# -------------------------------
# FASE 3: Inicialización y entrenamiento
# -------------------------------
kmeans = KMeans(n_clusters=k, init='random', n_init=1, max_iter=10, random_state=42)

kmeans.fit(X)

# Centroides finales
centroides = kmeans.cluster_centers_

# Etiquetas asignadas
labels = kmeans.labels_


# -------------------------------
# FASE 4: Visualización resultado final
# -------------------------------
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1], 
            c='red', s=200, marker='X', label='Centroides')

plt.title("Resultado Final de K-Means")
plt.legend()
plt.show()


# -------------------------------
# FASE 5: Ver función objetivo (Inercia)
# -------------------------------
print("Inercia (Suma de distancias cuadradas):", kmeans.inertia_)