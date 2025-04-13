import string
import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

#Ranking de popularidad de bolígrafos
#TAREA 3: Identificar el tipo de bolígrafo que se compra con más frecuencia.
#Pasos: Cuente el número de compras por artículo.
#       Ordenar en orden descendente.
#       Traza un gráfico de barras horizontales para mayor claridad.
#       Visualización: 📊 Gráfico de barras horizontales (bolígrafos más vendidos)

conteo_de_Productos = df_pen_sales.groupby("Item").value_counts()
print(conteo_de_Productos)
plt.figure(figsize = (10, 5))
conteo_de_Productos.plot(kind="barh", color= 'r')
plt.title("ranking de Popularidad de los Productos")
plt.xlabel("Cantidad de ventas de Los Productos")
plt.ylabel("Tipo de Producto")
plt.gca().invert_yaxis()
plt.show()
