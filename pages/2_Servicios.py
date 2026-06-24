import streamlit as st
from data_loader import load_data
import plotly.express as px

st.set_page_config(page_title="Servicios", page_icon="🌱", layout="wide")

st.title("🌱 ¿Qué están pidiendo nuestros clientes?")
st.markdown("Demanda de servicios por volumen de solicitudes.")

df = load_data()
servicios_count = df['Servicio Solicitado'].value_counts().reset_index()
servicios_count.columns = ['Servicio', 'Cantidad de Pedidos']

# Gráfico principal
fig = px.bar(
        servicios_count,
        x='Cantidad de Pedidos',
        y='Servicio',
        orientation='h',
        template='plotly_white',
        color_discrete_sequence=['#00C853'],
        labels={'Cantidad de Pedidos': 'Número de solicitudes'}
)
fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        showlegend=False,
        height=400,
        margin=dict(l=200)
)
st.plotly_chart(fig, use_container_width=True)

# SECCIÓN DE INSIGHTS
st.markdown("### 📊 Análisis de Demanda")

if len(servicios_count) > 0:
        top1 = servicios_count.iloc[0]
        top1_servicio = top1['Servicio']
        top1_cantidad = top1['Cantidad de Pedidos']

    # Calcular el porcentaje
        total_solicitudes = servicios_count['Cantidad de Pedidos'].sum()
        porcentaje_top1 = (top1_cantidad / total_solicitudes * 100)

    insight_html = f"""
        <div style="
        background-color: #FFFFFF;
                padding: 25px;
                        border-radius: 12px;
                                border-left: 5px solid #00C853;
                                        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                                            ">
                                                    <h3 style="margin-top: 0; color: #111827;">Servicio Estrella</h3>
                                                            <p style="color: #374151; font-size: 16px; line-height: 1.6;">
                                                                        <strong>{top1_servicio}</strong> es el servicio más solicitado con <strong>{top1_cantidad} solicitudes</strong> 
                                                                                    ({porcentaje_top1:.1f}% del total).
                                                                                            </p>
                                                                                                    
                                                                                                            <h3 style="color: #111827;">Recomendaciones</h3>
                                                                                                                    <ul style="color: #374151; font-size: 16px;">
                                                                                                                                <li>Priorizar recursos para {top1_servicio.lower()}</li>
                                                                                                                                            <li>Desarrollar ofertas especiales o paquetes promocionales</li>
                                                                                                                                                        <li>Capacitar el equipo comercial en esta especialidad</li>
                                                                                                                                                                    <li>Crear material de marketing enfocado en este servicio</li>
                                                                                                                                                                            </ul>
                                                                                                                                                                                </div>
                                                                                                                                                                                    """

    st.markdown(insight_html, unsafe_allow_html=True)
else:
    st.info("No hay datos de servicios disponibles.")

# TABLA DE DETALLES
st.markdown("### 📋 Detalles por Servicio")

display_servicios = servicios_count.copy()
display_servicios['Porcentaje'] = (display_servicios['Cantidad de Pedidos'] / display_servicios['Cantidad de Pedidos'].sum() * 100).round(1).astype(str) + '%'

st.dataframe(
        display_servicios,
        use_container_width=True,
        hide_index=True,
        column_config={
                    "Cantidad de Pedidos": st.column_config.NumberColumn(format="%d")
        }
)
