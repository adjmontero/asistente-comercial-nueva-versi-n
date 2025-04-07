import streamlit as st
import pandas as pd

# Título
st.title("🧥 Asistente Virtual Comercial - Prueba de Concepto")

# Cargar datos desde el Excel
@st.cache_data
def cargar_datos():
    xls = pd.ExcelFile("Base_Asistente_Imagenes_Estructuradas.xlsx")

    # Mostrar qué hojas tiene el archivo (debug)
    st.write("🧾 Hojas disponibles en el archivo Excel:", xls.sheet_names)

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
        st.markdown(f"### 👋 ¡Qué alegría verte por aquí otra vez, {nombre}!")

        st.markdown("¿Qué estás buscando hoy? Elige entre nuestras prendas disponibles:")
        
        for _, prenda in prendas_df.iterrows():
            st.markdown(f"**{prenda['Nombre']}**")
            st.image(prenda["URL Imagen"], width=250)

        st.markdown("🔜 En futuras versiones podrás verte con estas prendas directamente sobre tu avatar.")
    else:
        st.warning("No encontramos tu email en la base de datos. ¿Te gustaría registrarte?")
