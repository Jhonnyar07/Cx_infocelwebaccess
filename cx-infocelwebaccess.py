import streamlit as st
import pandas as pd
import os

#im = chart_with_upwards_trend
st.set_page_config(
    page_title="Buscador Accesos Infocel",
    page_icon = ":magnifying_glass_tilted_right:",
)

# Nombre del archivo
archivo_excel = "BD.xlsx"

# Verificar que el archivo existe
if not os.path.exists(archivo_excel):
    st.error(f"No se encontró el archivo {archivo_excel}")
else:
    # Leer el Excel
    df = pd.read_excel(archivo_excel)

    st.title("Buscador de Accesos INFOCEL")

    # Campo de búsqueda
    busqueda = st.text_input("Escribe texto para buscar en la base de datos")

    if busqueda:
        # Filtrar por coincidencia parcial en cualquier columna
        filtro = df.apply(lambda fila: fila.astype(str).str.contains(busqueda, case=False, na=False), axis=1)
        resultados = df[filtro.any(axis=1)]

        st.write(f"Resultados encontrados: {len(resultados)}")
        st.dataframe(resultados)
