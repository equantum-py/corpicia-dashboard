import streamlit as st
import plotly.express as px
from data_loader import load_data
import pandas as pd

st.set_page_config(page_title="Análisis Geográfico", layout="wide")

st.title("🗺️ Análisis Geográfico")
st.markdown("Distribución de la demanda y generación de negocio por ciudad.")

df = load_data()

# Clean some common geo names if needed (this is basic)
df['Ciudad_Clean'] = df['Lugar'].str.title().str.strip()
df.loc[df['Ciudad_Clean'].str.contains('Asunci', na=False), 'Ciudad_Clean'] = 'Asunción'

# Group by location for total prospects
geo_prospectos = df['Ciudad_Clean'].value_counts().reset_index()
geo_prospectos.columns = ['Ciudad', 'Prospectos']

# Group by location for won deals
geo_ventas = df[df['Estado_Clean'] == 'Ganado'].groupby('Ciudad_Clean')['Monto Cerrado Num'].sum().reset_index()
geo_ventas.columns = ['Ciudad', 'Ingreso_Total']

geo_merged = pd.merge(geo_prospectos, geo_ventas, on='Ciudad', how='left').fillna(0)

col1, col2 = st.columns(2)

with col1:
    fig_pros = px.bar(
        geo_merged.sort_values(by='Prospectos', ascending=True).tail(10), 
        x='Prospectos', 
        y='Ciudad', 
        orientation='h', 
        title='Top Ciudades por Generación de Prospectos',
        template="plotly_dark",
        color='Prospectos',
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig_pros, use_container_width=True)

with col2:
    fig_ventas = px.bar(
        geo_merged.sort_values(by='Ingreso_Total', ascending=True).tail(10), 
        x='Ingreso_Total', 
        y='Ciudad', 
        orientation='h', 
        title='Top Ciudades por Volumen de Ventas (₲)',
        template="plotly_dark",
        color='Ingreso_Total',
        color_continuous_scale="Greens"
    )
    st.plotly_chart(fig_ventas, use_container_width=True)

st.info("💡 Observación: Integrar mapas requeriría coordenadas exactas. El gráfico de barras horizontales es ideal para comparar rendimiento a nivel macro entre municipios.")
