import streamlit as st
import pandas as pd
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Buscador Accesos Infocel",
    page_icon="static/bd.ico",
)

# --- LOGIN ---
USUARIOS = {
    "admin": "1234",
    "usuario": "abcd"
}

if "logueado" not in st.session_state:
    st.session_state.logueado = False

# Si no está logueado, mostrar pantalla de login
if not st.session_state.logueado:
    st.markdown("<h2 style='text-align: center;'>Login de Acceso</h2>", unsafe_allow_html=True)
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Login automático al llenar ambos campos
    if username and password:
        if username in USUARIOS and password == USUARIOS[username]:
            st.session_state.logueado = True
            st.experimental_rerun()  # recarga la app mostrando la pantalla principal
        else:
            st.error("Usuario o contraseña incorrectos")

# --- PANTALLA PRINCIPAL SOLO SI ESTÁ LOGUEADO ---
if st.session_state.logueado:
    archivo_excel = "BD.xlsx"

    if not os.path.exists(archivo_excel):
        st.error(f"No se encontró el archivo {archivo_excel}")
    else:
        df = pd.read_excel(archivo_excel)

        st.image("https://i.imgur.com/NwOV7Ob.jpg")
        st.markdown("<h2 style='text-align: center;'>Accesos INFOCEL</h2>", unsafe_allow_html=True)

        st.markdown("<p style='text-align: center;'>Introduce el ID del equipo o Nombre del cliente</p>", unsafe_allow_html=True)
        busqueda = st.text_input("")

        if busqueda:
            resultados = df[
                df['ID del equipo'].astype(str).str.contains(busqueda, case=False, na=False) |
                df['Cliente'].str.contains(busqueda, case=False, na=False)
            ]

            if not resultados.empty:
                if len(resultados) > 1:
                    st.subheader(f"Se encontraron {len(resultados)} coincidencias:")
                elif len(resultados) == 1:
                    st.subheader(f"Se encontró {len(resultados)} coincidencia:")

                for i, fila in resultados.iterrows():
                    with st.expander(f"{fila['ID del equipo']} - {fila['Cliente']}"):
                        st.write(f"**ID del equipo:** {fila['ID del equipo']}")
                        st.write(f"**Cliente:** {fila['Cliente']}")
                        st.write(f"**Enlace Web:** {fila['Enlace Web']}")
                        st.write(f"**Usuario:** {fila['Usuario']}")
                        st.write(f"**Contraseña:** {fila['Contraseña']}")
            else:
                st.error("No se encontró ningún registro con esos datos.")

        st.write("----------------------------------------------------------------------------------------------------")
        st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2025 PID Medioambiental, S.L. <br> J. Aguilar <br> Rev. 1.01 </p>", unsafe_allow_html=True)
