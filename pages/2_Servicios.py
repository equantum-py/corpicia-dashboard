import streamlit as st
from data_loader import load_data
import plotly.express as px

st.set_page_config(page_title="Servicios Solicitados", page_icon="🌱", layout="wide")

st.title("🌱 ¿Qué están pidiendo los clientes?")
st.markdown("Un resumen rápido de los servicios que más nos solicitan.")

df = load_data()
servicios_count = df['Servicio Solicitado'].value_counts().reset_index()
servicios_count.columns = ['Servicio', 'Cantidad de Pedidos']

fig = px.bar(
            servicios_count,
            x='Cantidad de Pedidos',
            y='Servicio',
            orientation='h',
            template='plotly_white',
            color_discrete_sequence=['#00C853']
)
fig.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### Resumen en palabras:
* **Sistemas de Riego y Empastados** son el servicio estrella. Generan el mayor interés del público.
* Servicios secundarios como **Jardinería** y mantenimientos básicos son menos solicitados pero se venden.
""")
