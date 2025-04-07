
import streamlit as st
import pandas as pd

# Título
st.title("🧥 Asistente Virtual Comercial - Prueba de Concepto")

# Cargar datos desde el Excel
@st.cache_data
def cargar_datos():
    xls = pd.ExcelFile("Base_Asistente_Imagenes_Estructuradas.xlsx")
    avatares_df = pd.read_excel(xls, sheet_name="Avatares")
    prendas_df = pd.read_excel(xls, sheet_name="Prendas")
    return avatares_df, prendas_df

# Ejecutar la carga de datos
avatares_df, prendas_df = cargar_datos()

# Campo para email
email = st.text_input("📧 Introduce tu correo electrónico para comenzar").strip().lower()

if email:
    cliente = avatares_df[avatares_df["Email"].str.lower() == email]
    if not cliente.empty:
        nombre = cliente.iloc[0]["Nombre"]
        ciudad = cliente.iloc[0]["Ciudad"]
        estilo = cliente.iloc[0]["Estilo"]
        ultima_compra = cliente.iloc[0]["Última compra"]
        st.markdown(f"### 👋 ¡Qué alegría verte por aquí otra vez, {nombre}!")
        st.markdown(f"Veo que estás en **{ciudad}**, tu estilo favorito es **{estilo}** y la última vez te llevaste una **{ultima_compra}**. 😎")

        st.markdown("¿Qué estás buscando hoy? Elige entre nuestras prendas disponibles:")
        for _, prenda in prendas_df.iterrows():
            st.markdown(f"**{prenda['Descripción']}**")
            st.image(prenda["URL imgur"], width=250)

        st.markdown("🧵 ¿Te gustaría que te reserve alguna para el probador?")
    else:
        st.warning("No encontramos tu email en la base de datos. ¿Te gustaría registrarte?")
