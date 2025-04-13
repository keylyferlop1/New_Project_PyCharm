import string
import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")


# Analisis de Costos de envio
#TAREA 2: Evalue como varian los costos de envios entre pedidos
#Pasos: Calcular la distribucion del costo de environ
#       Agrupe por articulo y calcule el costo promedio de envio
#       Cree un Grafico de barras que compare los costos de envio por tipo de boligrafo
#       Visualzacion Graficos de barras(Costos Promedios de envios por articulos)

print(df_pen_sales.dtypes)

df_avg_pen_costs = df_pen_sales.groupby("Item")["Shipping Cost"].mean()
print(df_avg_pen_costs)

df_avg_pen_costs_sorted = df_avg_pen_costs.sort_values(ascending=True)

plt.figure(figsize = (10, 5))
df_avg_pen_costs.plot(kind="barh", color = 'green')
plt.title("Costo del envio Promedio por Producto")
plt.xlabel("Costo medio del envio de los Productos")
plt.ylabel("Tipo de Producto")
plt.show()