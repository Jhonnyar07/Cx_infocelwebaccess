import streamlit as st
import pandas as pd

# Leer el archivo Excel
df = pd.read_excel("BD.xlsx")

st.title("Buscador de equipos por palabra clave")

# Entrada de búsqueda
busqueda = st.text_input("Escribe palabra clave de ID del equipo o Cliente:")

if busqueda:
    # Filtrar coincidencias parciales en 'ID del equipo' o 'Cliente'
    resultados = df[
        df['ID del equipo'].astype(str).str.contains(busqueda, case=False, na=False) |
        df['Cliente'].str.contains(busqueda, case=False, na=False)
    ]

    if not resultados.empty:
        st.subheader(f"Se encontraron {len(resultados)} coincidencias:")
        # Mostrar solo las columnas relevantes
        st.dataframe(resultados[['ID del equipo', 'Cliente', 'Usuario', 'Contraseña', 'Tipo']])
    else:
        st.warning("No se encontró ningún registro con esa palabra clave.")
