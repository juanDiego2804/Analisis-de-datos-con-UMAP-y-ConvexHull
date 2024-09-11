**Análisis de datos con UMAP y Convex Hull**

Miembros del equipo:
- Juan Diego Castro Mariscal
- José Antonio Castro Mariscal

Descripción:
Descargar y analizar datos de expresión genética de diferentes tipos de células cerebrales. Visualizar los datos utilizando proyecciones UMAP y aplicar un algoritmo de convex hull (mediante fuerza bruta) para identificar y resaltar los clusters. 

Se usara la librería anndata para cargar y explorar los datos genéticos.
Se van a extraer las coordenadas UMAP junto con el identificador de cluster (cluster_id) de las observaciones en los datos.
Implementar la técnica de hull convexo sobre las coordenadas UMAP para cada cluster.
Visualizar los resultados en un gráfico donde cada cluster esté representado por un color único, y el hull convexo tenga un tono más suave del mismo color.
Generar y analizar la proyección UMAP junto con los hulls convexos.

Descargar la base de datos:
Los datos de coordenadas UMAP serán descargados de una base de datos de expresión genética que contiene información sobre diferentes tipos de células cerebrales.
ir al link: https://cellxgene.cziscience.com/collections/283d65eb-dd53-496d-adb7-7570c7caa443 y descargar el "Supercluster: Committed oligodendrocyte precursor", que viene al final de la página. Descargarlo en formato h5ad.

Este codigo esta pensado para que funcione directamente en Google Colab.
En tu Google Drive, en la misma carpeta debes tener el codigo y la base de datos descargada anteriormente, y en el codigo cambiaas la parte de:
rutaDB = '/content/drive/MyDrive/nombre_de_tu_carpeta/nombre_del_archivo_de_base_de_datos.h5ad'
