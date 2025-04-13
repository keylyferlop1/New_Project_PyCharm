import string
import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")


#Análisis de Tiempo de Entrega
#TAREA 4: Calcular el tiempo medio de entrega para cada tipo de bolígrafo.
#Pasos: Calcular tiempo de entrega = Fecha de entrega - Fecha de compra.
#       Agrupe por artículo y encuentre el tiempo medio de entrega.
#       Traza un gráfico de barras para comparar los tiempos de entrega.
#       Visualización: ⏳ Gráfico de barras (tiempo medio de entrega por tipo de bolígrafo)


#Purchase Date y Delivery Date
print(df_pen_sales["Delivery Date"])
print(df_pen_sales["Purchase Date"])

df_pen_sales["Purchase Date"] = pd.to_datetime(df_pen_sales["Purchase Date"])
df_pen_sales["Delivery Date"] = pd.to_datetime(df_pen_sales["Delivery Date"])

tiempo_de_entrega = (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date"]).dt.days
df_pen_sales["Tiempo de entrega"] = tiempo_de_entrega
tiempo_medio_de_entrega = df_pen_sales.groupby("Item")["Tiempo de entrega"].mean().sort_values()

plt.figure(figsize = (10, 5))
tiempo_medio_de_entrega.plot(kind="bar", color = 'm')
plt.title("Tiempo medio de entregas de  Productos")
plt.xlabel("Tipo de Productos")
plt.ylabel("Tiempo medio de entrega de Productos")
plt.xticks(rotation=45, ha="right")
plt.show()

print(tiempo_medio_de_entrega)