import streamlit as st
import datetime
from data_loader import load_data

st.set_page_config(page_title="Compartir Informe", page_icon="📤", layout="wide")

st.title("📤 Informe Gerencial Corpicia")
st.caption(f"Generado el: {datetime.date.today().strftime('%d/%m/%Y')}")

try:
    df = load_data()
except Exception as e:
    st.error("Error cargando datos.")
    st.stop()

total_prospectos = len(df)
ganados = len(df[df['Estado_Clean'] == 'Ganado'])
monto_cerrado = df[df['Estado_Clean'] == 'Ganado']['Monto Cerrado Num'].sum()

# Calcular el servicio más solicitado
servicio_top = df['Servicio Solicitado'].value_counts().index[0] if not df.empty else "N/A"

st.markdown("""
<style>
.share-box {
    background-color: #F0FDF4;
    border: 1px solid #86EFAC;
    padding: 25px;
    border-radius: 12px;
    color: #166534;
    font-size: 18px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="share-box">
<strong>Resumen Rápido del Negocio:</strong><br><br>
En este último período hemos recibido el contacto de <strong>{total_prospectos} clientes potenciales</strong>.<br>
De esos contactos, hemos logrado cerrar exitosamente <strong>{ganados} ventas</strong>, lo que representa un ingreso total de <strong>₲ {monto_cerrado:,.0f}</strong>.<br><br>
El servicio que más nos están solicitando en este momento es: <strong>{servicio_top}</strong>.<br><br>
<em>El ecosistema digital sigue activo. Nuestro objetivo actual debe centrarse en no perder los clientes que nos contactan y aún no han recibido seguimiento.</em>
</div>
""", unsafe_allow_html=True)

st.divider()
st.info("💡 Tip: Toma una captura de pantalla de este resumen para enviarlo directamente por WhatsApp al grupo directivo.")
