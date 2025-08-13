import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Buscador Accesos Infocel",
    page_icon=":smile:",
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
st.markdown("<h1 style='text-align: center;'>Accesos INFOCEL</h1>", unsafe_allow_html=True)

# Campo de búsqueda (por ID del equipo o por Cliente)
busqueda = st.text_input("Escribe el ID del equipo o el nombre del Cliente:")

if busqueda:
    # Filtrar coincidencias parciales en ID o Cliente
    resultados = df[
        df['ID del equipo'].astype(str).str.contains(busqueda, case=False, na=False) |
        df['Cliente'].str.contains(busqueda, case=False, na=False)
    ]

    if not resultados.empty:
        st.subheader(f"Se encontraron {len(resultados)} coincidencias:")
        
        # Mostrar cada coincidencia en un expander
        for i, fila in resultados.iterrows():
            with st.expander(f"{fila['ID del equipo']} - {fila['Cliente']}"):
                st.write(f"**ID del equipo:** {fila['ID del equipo']}")
                st.write(f"**Cliente:** {fila['Cliente']}")
                st.write(f"**Enlace Web:** {fila['Enlace Web']}")
                st.write(f"**Usuario:** {fila['Usuario']}")
                st.write(f"**Contraseña:** {fila['Contraseña']}")
                st.write(f"**Tipo:** {fila['Tipo']}")
    else:
        st.error("No se encontró ningún registro con esos datos.")
