import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="Contactos", page_icon="👤", layout="wide")

st.title("👤 Contactos Recibidos")
st.markdown("Lista de personas que nos contactaron. Puedes buscar por cualquier campo.")

df = load_data()

col1, col2, col3, col4 = st.columns(4)
with col1:
        f_fecha = st.multiselect("📅 Fecha", options=df['Fecha'].dropna().unique())
    with col2:
            f_ciudad = st.multiselect("📍 Ciudad", options=df['Lugar'].unique())
        with col3:
                f_estado = st.multiselect("📊 Estado", options=df['Estado_Clean'].unique())
            with col4:
                    f_servicio = st.multiselect("🌱 Servicio", options=df['Servicio Solicitado'].unique())

filtered_df = df.copy()
if f_fecha:
        filtered_df = filtered_df[filtered_df['Fecha'].isin(f_fecha)]
    if f_ciudad:
            filtered_df = filtered_df[filtered_df['Lugar'].isin(f_ciudad)]
        if f_estado:
                filtered_df = filtered_df[filtered_df['Estado_Clean'].isin(f_estado)]
            if f_servicio:
                    filtered_df = filtered_df[filtered_df['Servicio Solicitado'].isin(f_servicio)]

# Mostrar solo las columnas relevantes para gerencia
cols_to_show = ['Prospecto', 'Lugar', 'Servicio Solicitado', 'Estado_Clean', 'Monto Presupuestado Num', 'Monto Cerrado Num']
display_df = filtered_df[cols_to_show].copy()

# Formato simple de moneda
display_df['Monto Presupuestado Num'] = display_df['Monto Presupuestado Num'].apply(lambda x: f"₲ {x:,.0f}" if x > 0 else "-")
display_df['Monto Cerrado Num'] = display_df['Monto Cerrado Num'].apply(lambda x: f"₲ {x:,.0f}" if x > 0 else "-")

display_df.columns = ['Nombre', 'Ciudad', 'Servicio Solicitado', 'Estado', 'Presupuestado', 'Cerrado']

st.dataframe(display_df, use_container_width=True, hide_index=True)

st.caption(f"Mostrando {len(display_df)} de {len(df)} contactos totales.")
