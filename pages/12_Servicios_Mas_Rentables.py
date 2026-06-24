import streamlit as st
import plotly.express as px
from data_loader import load_data

st.set_page_config(page_title="Servicios Más Rentables", layout="wide")

st.title("💼 Servicios Más Rentables")
st.markdown("Identificando dónde está el mayor retorno.")

df = load_data()
df_ganados = df[df['Estado_Clean'] == 'Ganado']

# Agrupar por servicio
rentabilidad = df_ganados.groupby('Servicio Solicitado').agg(
    Cantidad_Ventas=('ID', 'count'),
    Ingreso_Total=('Monto Cerrado Num', 'sum')
).reset_index()

rentabilidad = rentabilidad.sort_values(by='Ingreso_Total', ascending=False)

col1, col2 = st.columns(2)

with col1:
    fig_ingresos = px.bar(
        rentabilidad, 
        x='Servicio Solicitado', 
        y='Ingreso_Total', 
        title='Ingresos Totales por Servicio',
        template="plotly_dark",
        color='Ingreso_Total',
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_ingresos, use_container_width=True)

with col2:
    fig_cantidad = px.pie(
        rentabilidad, 
        values='Cantidad_Ventas', 
        names='Servicio Solicitado', 
        title='Volumen de Ventas por Servicio',
        template="plotly_dark",
        hole=0.4
    )
    st.plotly_chart(fig_cantidad, use_container_width=True)

st.subheader("Tabla de Rentabilidad")
# Formatting the currency for display
rentabilidad_display = rentabilidad.copy()
rentabilidad_display['Ingreso_Total'] = rentabilidad_display['Ingreso_Total'].apply(lambda x: f"₲ {x:,.0f}")
st.dataframe(rentabilidad_display, use_container_width=True)
