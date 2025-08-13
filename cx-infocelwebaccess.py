import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Buscador Accesos Infocel",
    page_icon="static/bd.ico",
)

# Nombre del archivo
archivo_excel = "BD.xlsx"

# Verificar que el archivo existe
if not os.path.exists(archivo_excel):
    st.error(f"No se encontró el archivo {archivo_excel}")
else:
    # Leer el Excel
    df = pd.read_excel(archivo_excel)

st.image("https://i.imgur.com/NwOV7Ob.jpg")
st.markdown("<h2 style='text-align: center;'>Accesos INFOCEL</h2>", unsafe_allow_html=True)

# Campo de búsqueda (por ID del equipo o por Cliente)
st.markdown("<p style='text-align: center;'>Introduce el ID del equipo o Nombre del cliente</p>", unsafe_allow_html=True)
busqueda = st.text_input("")

if busqueda:
    # Filtrar coincidencias parciales en ID o Cliente
    resultados = df[
        df['ID del equipo'].astype(str).str.contains(busqueda, case=False, na=False) |
        df['Cliente'].str.contains(busqueda, case=False, na=False)
    ]

    if not resultados.empty:
        if len(resultados) > 1:
            st.subheader(f"Se encontraron {len(resultados)} coincidencias:")
        elif len(resultados) == 1:
            st.subheader(f"Se encontró {len(resultados)} coincidencia:")
        
        # Mostrar cada coincidencia en un expander
        for i, fila in resultados.iterrows():
            with st.expander(f"{fila['ID del equipo']} - {fila['Cliente']}"):
                st.write(f"**ID del equipo:** {fila['ID del equipo']}")
                st.write(f"**Cliente:** {fila['Cliente']}")
                st.write(f"**Enlace Web:** {fila['Enlace Web']}")
                st.write(f"**Usuario:** {fila['Usuario']}")
                st.write(f"**Contraseña:** {fila['Contraseña']}")
    else:
        st.error("No se encontró ningún registro con esos datos.")
