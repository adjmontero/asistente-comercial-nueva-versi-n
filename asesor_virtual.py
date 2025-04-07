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

# Ejecutar la carga
avatares_df, prendas_df = cargar_datos()

# Input del cliente
email = st.text_input("📧 Introduce tu correo electrónico para comenzar").strip().lower()

if email:
    cliente = avatares_df[avatares_df["Email"].str.lower() == email]

    if not cliente.empty:
        nombre = cliente.iloc[0]["Nombre"]
        st.markdown(f"### 👋 ¡Qué alegría verte por aquí otra vez, {nombre}!")
        st.markdown("¿Qué estás buscando hoy? Elige entre nuestras prendas disponibles:")

        for _, prenda in prendas_df.iterrows():
            nombre_prenda = prenda.get("Descripción", "Prenda sin nombre")
            imagen_url = prenda.get("URL Imgur", None)

            st.markdown(f"**{nombre_prenda}**")
            if imagen_url:
                st.image(imagen_url, width=250)

        st.markdown("🔜 Muy pronto podrás ver cómo te queda directamente sobre tu avatar 😉")

    else:
        st.warning("No encontramos tu email en la base de datos. ¿Te gustaría registrarte?")
