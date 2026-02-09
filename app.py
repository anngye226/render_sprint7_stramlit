import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
# encabezado de la aplicación
st.header('Analisis exploratorio de datos  de Vehículos')


# Botón para crear un histograma
if st.button("construir histograma"):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    if'odometer' in car_data.columns:
         fig = px.histogram(car_data, x="odometer",title=f'Histograma de odómetro') 
    else:
         fig = px.histogram(car_data, x=car_data.columns[0],title=f'Histograma de {car_data.columns[0]}')

    st.plotly_chart(fig, use_container_width=True)

#boton para construir  un grafico de dispersión
if st.button("construir grafico de dispersion"):
   st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
   if 'price' in car_data.columns and 'odometer' in car_data.columns:
       fig = px.scatter(car_data, x="odometer", y="price", title=f'Gráfico de dispersión de precio vs odómetro')
       st.plotly_chart(fig, use_container_width=True)
   else:
        st.write("Las columnas 'price' y 'odometer' no están disponibles en el conjunto de datos.")