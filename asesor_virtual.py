import streamlit as st
import pandas as pd

st.set_page_config(page_title="Asistente Virtual Comercial", page_icon="🧥")

st.title("🧥 Asistente Virtual Comercial - Prueba de Concepto")

# Cargar datos desde el Excel
@st.cache_data
def cargar_datos():
    xls = pd.ExcelFile("Base_Asistente_Imagenes_Estructuradas.xlsx")
    avatares_df = pd.read_excel(xls, sheet_name="Avatares")
    prendas_df = pd.read_excel(xls, sheet_name="Prendas")
    return avatares_df, prendas_df

avatares_df, prendas_df = cargar_datos()

# Input para email
email = st.text_input("📧 Introduce tu correo electrónico para comenzar").strip().lower()

if email:
    cliente = avatares_df[avatares_df["Email"].str.lower() == email]

    if not cliente.empty:
        nombre = cliente.iloc[0]["Nombre"]
        ciudad = cliente.iloc[0]["Ciudad"]
        estilo = cliente.iloc[0]["Estilo preferido"]
        ultima_compra = cliente.iloc[0]["Artículo comprado"]

        st.markdown(f"### 👋 ¡Qué alegría verte por aquí otra vez, {nombre}!")
        st.write(f"Veo que estás en **{ciudad}**, tu estilo favorito es **{estilo}** y la última vez te llevaste un artículo como este: **{ultima_compra}** 💫")

        st.markdown("¿Qué estás buscando hoy? ¿Es para una ocasión especial o simplemente para renovar tu clóset? 👗👕")

        st.markdown("Mientras me lo cuentas, aquí te dejo algunas sugerencias que combinan con tu estilo:")

        recomendaciones = prendas_df[prendas_df["Estilo"].str.lower() == estilo.lower()]
        if recomendaciones.empty:
            recomendaciones = prendas_df.sample(5)

        for _, prenda in recomendaciones.iterrows():
            st.markdown(f"**{prenda['Descripción']}**")
            st.markdown(f"➡️ [Ver imagen]({prenda['URL imgur']})")

        st.markdown("¿Te gustaría que te reserve alguna para que la tengas lista en el probador? 😉")

    else:
        st.warning("No encontramos tu email en la base de datos. ¿Te gustaría registrarte?")
