import streamlit as st
import pandas as pd

# Título
st.title("🧥 Asistente Virtual Comercial - Prueba de Concepto")

# Cargar datos desde Google Sheets
@st.cache_data
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/1My_J5iKx2F5RvQ3KEHgNV_7i94GTe3mXpliPaESwb50/export?format=xlsx"
    xls = pd.ExcelFile(url)
    clientes = pd.read_excel(xls, sheet_name="Clientes")
    prendas = pd.read_excel(xls, sheet_name="Prendas")
    avatares = pd.read_excel(xls, sheet_name="Avatares")
    return clientes, prendas, avatares

clientes_df, prendas_df, avatares_df = cargar_datos()

# Campo para email
email = st.text_input("📧 Introduce tu correo electrónico para comenzar").strip().lower()

if email:
    cliente = clientes_df[clientes_df["Email"].str.lower() == email]
    if not cliente.empty:
        nombre = cliente.iloc[0]["Nombre"]
        st.markdown(f"### 👋 ¡Qué alegría verte por aquí otra vez, {nombre}!")

        st.markdown("¿Qué estás buscando hoy? Elige entre nuestras prendas disponibles:")
        
        for _, prenda in prendas_df.iterrows():
            st.markdown(f"**{prenda['Nombre']}**")
            st.image(prenda["URL Imagen"], width=250)

        st.markdown("🔜 En futuras versiones podrás verte con estas prendas directamente sobre tu avatar.")

    else:
        st.warning("No encontramos tu email en la base de datos. ¿Te gustaría registrarte?")
