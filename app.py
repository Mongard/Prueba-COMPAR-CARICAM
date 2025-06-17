import streamlit as st
import pandas as pd

@st.cache_data(ttl=300)
def cargar_datos():
    url_csv_publico = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEXAMPLELINK/pub?gid=0&single=true&output=csv"
    return pd.read_csv(url_csv_publico)

df = cargar_datos()

st.title("📱 Comparador de Celulares")

# Filtros por país y cliente
paises = df["País"].dropna().unique()
clientes = df["Cliente"].dropna().unique()

pais_seleccionado = st.selectbox("Selecciona el país:", sorted(paises))
cliente_seleccionado = st.selectbox("Selecciona el cliente:", sorted(clientes))

df_filtrado = df[(df["País"] == pais_seleccionado) & (df["Cliente"] == cliente_seleccionado)]

# Filtros por marca (máx 5)
marcas = df_filtrado["Marca"].dropna().unique()
marcas_seleccionadas = st.multiselect("Selecciona hasta 5 marcas:", sorted(marcas), max_selections=5)

df_filtrado = df_filtrado[df_filtrado["Marca"].isin(marcas_seleccionadas)]

# Filtros por modelo (máx 10)
modelos = df_filtrado["Modelo"].dropna().unique()
modelos_seleccionados = st.multiselect("Selecciona hasta 10 modelos:", sorted(modelos), max_selections=10)

df_filtrado = df_filtrado[df_filtrado["Modelo"].isin(modelos_seleccionados)]

# Mostrar resultado
columnas = ["Marca", "Modelo", "Pantalla", "Procesador", "RAM", "Almacenamiento",
            "Cámara", "Batería", "Certificación", "Sistema Operativo", "Precio", "Precio promoción"]
st.dataframe(df_filtrado[columnas].reset_index(drop=True), use_container_width=True)
