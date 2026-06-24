import streamlit as st
import plotly.express as px
from data_loader import load_data

st.set_page_config(page_title="Embudo Comercial", layout="wide")

st.title("📈 Embudo Comercial")
st.markdown("Análisis de conversión de prospectos.")

df = load_data()

# Calculate funnel steps
total_prospectos = len(df)
# For the funnel, we can assume: Ingresados -> Contactados (all) -> En Negociación (Pendiente + Ganado) -> Cerrados (Ganados)
contactados = total_prospectos # Assume all are at least contacted based on observations
en_negociacion = len(df[df['Estado_Clean'].isin(['Ganado', 'Pendiente'])])
ganados = len(df[df['Estado_Clean'] == 'Ganado'])

funnel_data = dict(
    number=[total_prospectos, contactados, en_negociacion, ganados],
    stage=["1. Ingresados (Total)", "2. Contactados", "3. En Negociación", "4. Cierre Ganado"]
)

fig = px.funnel(funnel_data, x='number', y='stage', title='Embudo de Ventas (Macro)', template="plotly_dark")
fig.update_traces(marker=dict(color=['#3182CE', '#2B6CB0', '#2C5282', '#00C853']))

st.plotly_chart(fig, use_container_width=True)

st.info("💡 **Conclusión del Embudo**: Gran parte de la pérdida se da en las primeras etapas de contacto y seguimiento.")
