import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="Resumen Financiero", page_icon="💰", layout="wide")

st.title("💰 Resumen Financiero")
st.markdown("El estado del dinero de forma clara y sencilla.")

df = load_data()

monto_cerrado = df[df['Estado_Clean'] == 'Ganado']['Monto Cerrado Num'].sum()
monto_pendiente = df[df['Estado_Clean'] == 'Pendiente']['Monto Presupuestado Num'].sum() # Estimado de plata en la mesa
monto_presupuestado_total = df['Monto Presupuestado Num'].sum()

# Ticket promedio solo sobre los cerrados (o presupuestados si cerrado es 0)
cerrados_con_monto = df[(df['Estado_Clean'] == 'Ganado') & (df['Monto Cerrado Num'] > 0)]
ticket_promedio = cerrados_con_monto['Monto Cerrado Num'].mean() if not cerrados_con_monto.empty else 0

st.markdown("""
<style>
.finance-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #E5E7EB;
    border-left: 5px solid #00C853;
    margin-bottom: 20px;
}
.finance-title {
    color: #6B7280;
    font-size: 14px;
    text-transform: uppercase;
}
.finance-value {
    color: #111827;
    font-size: 32px;
    font-weight: bold;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'''
    <div class="finance-card">
        <div class="finance-title">Dinero Ganado (Cerrado)</div>
        <div class="finance-value">₲ {monto_cerrado:,.0f}</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'''
    <div class="finance-card" style="border-left-color: #F59E0B;">
        <div class="finance-title">Dinero Pendiente (En Seguimiento)</div>
        <div class="finance-value">₲ {monto_pendiente:,.0f}</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div class="finance-card" style="border-left-color: #3B82F6;">
        <div class="finance-title">Ticket Promedio (Venta Media)</div>
        <div class="finance-value">₲ {ticket_promedio:,.0f}</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("### ¿Qué significa esto?")
st.write("Has asegurado **₲ " + f"{monto_cerrado:,.0f}" + "** en ingresos recientes. Aún hay **₲ " + f"{monto_pendiente:,.0f}" + "** en presupuestos enviados que la gente todavía no ha respondido o están pensando. Si mejoramos el seguimiento a esos clientes, podríamos recuperar gran parte de ese dinero que hoy está 'en el aire'. Cada cliente que cierra, gasta en promedio **₲ " + f"{ticket_promedio:,.0f}" + "**.")
