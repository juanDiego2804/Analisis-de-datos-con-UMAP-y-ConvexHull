
#Codigo que funciona en google colab
!pip install -U loompy
!pip install anndata
!pip install anndata umap-learn scipy matplotlib
!pip install  umap-learn scipy matplotlib
!pip install anndata umap-learn scipy matplotlib
# Importación de las librerías necesarias

import anndata
import umap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.spatial
from scipy.spatial import ConvexHull
from google.colab import drive
drive.mount('/content/drive')

import anndata as ad

# Cargar el archivo .h5ad

rutaDB = '/content/drive/MyDrive/analisis_con_convexhull/base_datos_exp_gen.h5ad'
adata = ad.read_h5ad(rutaDB)

# Inspeccionar las claves disponibles en obsm y obs
#print("Claves en obsm:", adata.obsm.keys())
#print("Claves en obs:", adata.obs.keys())



# Función para dibujar el hull convexo
def plot_convex_hull(ax, points, color, alpha=0.3):
    if len(points) < 3:
        return
    hull = ConvexHull(points)
    for simplex in hull.simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], color=color, alpha=alpha)



# Extraer las coordenadas UMAP y el identificador de cluster
umap_coords = adata.obsm['X_UMAP']  
cluster_ids = adata.obs['cluster_id']

# Crear una figura para la visualización
fig, ax = plt.subplots(figsize=(10, 8))

# Obtener los identificadores de clúster únicos
unique_clusters = np.unique(cluster_ids)

# Asignar un color único para cada clúster
colors = cm.get_cmap('viridis')(np.linspace(0, 1, len(unique_clusters)))

for cluster_id, color in zip(unique_clusters, colors):
    # Seleccionar puntos del clúster actual
    cluster_points = umap_coords[cluster_ids == cluster_id]

    # Dibujar puntos del clúster
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], color=color, label=f'Cluster {cluster_id}', s=10)

    # Dibujar el hull convexo para el clúster
    plot_convex_hull(ax, cluster_points, color=color)

# Configurar el gráfico
ax.set_title('Proyección UMAP con Hulls Convexos')
ax.set_xlabel('UMAP 1')
ax.set_ylabel('UMAP 2')
ax.legend()
plt.show()
