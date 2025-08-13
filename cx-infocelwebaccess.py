import streamlit as st
import pandas as pd
import numpy as np
import math
from PIL import Image

#@st.cache

#im = chart_with_upwards_trend
st.set_page_config(
    page_title="Buscador de accesos de clientes"
)

st.image("https://i.imgur.com/NwOV7Ob.jpg")

df_infocelaccessDB = pd.read_excel('BD.xlsx')
print(df_infocelaccessDB)
