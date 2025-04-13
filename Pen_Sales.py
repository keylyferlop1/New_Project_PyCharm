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

plt.figure(figsize = (10, 5))
df_avg_pen_costs.plot(kind="barh", color = 'green')
plt.title("Costo del envio Promedio por Producto")
plt.xlabel("Costo medio del envio de los Productos")
plt.ylabel("Tipo de Producto")
plt.show()


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

tiempo_de_entrega = (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date "]).dt.days
df_pen_sales["Tiempo de entrega"] = tiempo_de_entrega
tiempo_medio_de_entrega = df_pen_sales.groupby("Item")["Tiempo de entrega"].mean().sort_values()

plt.figure(figsize = (10, 5))
tiempo_medio_de_entrega.plot(kind="barh", color = 'm')
plt.title("Tiempo medio de entregas de  Productos")
plt.xlabel("Tipo de Productos")
plt.ylabel("Tiempo medio de entrega de Productos")
plt.xticks(rotation=45, ha="right")
plt.show()

print(tiempo_medio_de_entrega)


#Análisis de sentimiento de las reseñasq
#TAREA 5: Extraer el sentimiento de las opiniones de los clientes.
#Pasos: Divida la columna Revisar para separar el nombre del revisor y el comentario.
#       Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
#       Genere una nube de palabras o un gráfico circular de sentimienAtos.
#       Visualización: 🥧 Gráfico de pastel o circular (críticas positivas vs. negativas)
#       Nombre de la Persona | No me Gusto por tal cosa.....


df_pen_sales["Review"] = df_pen_sales["Review"].fillna("")
positive_words = ["love", "great", "good", "amazing", "excellent", "best"]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

def preprocess_text(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return text.split()

pos, neg = 0, 0
for review in df_pen_sales["Review"]:
    words = preprocess_text(review)
    pos += sum(w in positive_words for w in words)
    neg += sum(w in negative_words for w in words)

plt.figure(figsize=(8, 8))
plt.pie([pos, neg], labels=["Positive", "Negative"], colors=['#FF5733','#8E44AD'],
        explode=(0.1,0), autopct="%1.1f%%", startangle=140)
plt.title("Sentiment Analysis")
plt.show()