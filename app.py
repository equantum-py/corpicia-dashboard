import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="Resumen del Negocio", page_icon="🌱", layout="wide")

# Estilos limpios globales (Light Theme base)
st.markdown("""
<style>
.report-text {
font-size: 20px;
line-height: 1.8;
color: #374151;
background-color: #F9FAFB;
padding: 30px;
border-radius: 12px;
border-left: 6px solid #00C853;
box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

import datetime

st.title("Corpicia Dashboard Ejecutivo")
st.caption(f"Última actualización: {datetime.date.today().strftime('%d/%m/%Y')}")
st.markdown("### Hola José. Aquí tienes el estado actual de Corpicia:")

try:
        df = load_data()
except Exception as e:
        st.error(f"Error cargando datos: {e}")
        st.stop()

total_prospectos = len(df)
ganados = len(df[df['Estado_Clean'] == 'Ganado'])
pendientes = len(df[df['Estado_Clean'] == 'Pendiente'])
monto_cerrado = df[df['Estado_Clean'] == 'Ganado']['Monto Cerrado Num'].sum()

st.markdown(f"""
<div class="report-text">
Durante este período Corpicia recibió <strong>{total_prospectos} consultas comerciales</strong>.<br><br>
Se concretaron <strong>{ganados} ventas</strong> por un valor total de <strong>₲ {monto_cerrado:,.0f}</strong>.<br><br>
Actualmente existen <strong>{pendientes} oportunidades pendientes</strong> de seguimiento.<br><br>
La principal causa de pérdida de clientes es la <strong>falta de seguimiento comercial</strong>.<br><br>
Los servicios más solicitados son <strong>sistemas de riego y empastados</strong>.<br><br>
Google Ads y el sitio web continúan generando oportunidades de negocio de manera estable.
</div>
""", unsafe_allow_html=True)
