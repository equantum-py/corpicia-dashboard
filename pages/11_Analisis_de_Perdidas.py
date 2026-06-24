import streamlit as st
import plotly.express as px
from data_loader import load_data

st.set_page_config(page_title="Análisis de Pérdidas", layout="wide")

st.title("📉 Análisis de Pérdidas")
st.markdown("Entendiendo por qué no se cierran las ventas.")

df = load_data()
df_perdidos = df[df['Estado_Clean'] == 'Perdido']

st.metric("Total de Prospectos Perdidos", len(df_perdidos))

# Categorize reasons from 'Observaciones' conceptually
def categorize_reason(obs):
    obs = str(obs).lower()
    if 'seguimiento' in obs or 'contesta' in obs or 'clavo' in obs or 'respondio' in obs or 'respondio mas' in obs:
        return 'Falta de Seguimiento / No Contesta'
    elif 'precio' in obs or 'caro' in obs or 'presupuesto' in obs:
        return 'Precio / Presupuesto'
    elif 'zona' in obs or 'lejos' in obs:
        return 'Zona Fuera de Rango'
    elif 'tarde' in obs or 'tiempo' in obs:
        return 'Demora en Respuesta'
    else:
        return 'Otros / No Especificado'

df_perdidos['Motivo Principal'] = df_perdidos['Observaciones'].apply(categorize_reason)
motivos_count = df_perdidos['Motivo Principal'].value_counts().reset_index()
motivos_count.columns = ['Motivo', 'Cantidad']

fig = px.pie(motivos_count, values='Cantidad', names='Motivo', title='Motivos de Pérdida de Clientes', hole=0.4, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Detalle de Observaciones (Perdidos)")
st.dataframe(df_perdidos[['Prospecto', 'Celular', 'Observaciones', 'Motivo Principal']], use_container_width=True)
