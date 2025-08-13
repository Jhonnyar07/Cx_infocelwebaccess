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

st.title("Buscador de equipos")

# Campo de búsqueda (por ID del equipo o por Cliente)
busqueda = st.text_input("Escribe el ID del equipo o el Cliente:")

if busqueda:
    # Filtrar por coincidencia exacta (ignorando mayúsculas/minúsculas)
    resultados = df[
        (df['ID del equipo'].astype(str).str.lower() == busqueda.lower()) |
        (df['Cliente'].str.lower() == busqueda.lower())
    ]

    if not resultados.empty:
        # Mostrar solo la primera coincidencia
        fila = resultados.iloc[0]
        st.subheader("Resultado encontrado:")
        st.write(f"**ID del equipo:** {fila['ID del equipo']}")
        st.write(f"**Cliente:** {fila['Cliente']}")
        st.write(f"**Enlace Web:** {fila['Enlace Web']}")
        st.write(f"**Usuario:** {fila['Usuario']}")
        st.write(f"**Contraseña:** {fila['Contraseña']}")
        st.write(f"**Tipo:** {fila['Tipo']}")
    else:
        st.error("No se encontró ningún registro con esos datos.")
