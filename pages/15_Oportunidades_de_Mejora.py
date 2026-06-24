import streamlit as st

st.set_page_config(page_title="Oportunidades de Mejora", layout="wide")

st.title("🚀 Oportunidades de Mejora")
st.markdown("Plan de acción táctico y estratégico.")

col1, col2 = st.columns(2)

with col1:
    st.error("🔴 Urgencias (Corto Plazo)")
    st.markdown("""
    1. **Configurar Conversiones en Ads:** 
       - Importar el evento `whatsapp_click` de GA4 a Google Ads.
       - Esto permitirá que el algoritmo de Google optimice por clientes potenciales reales.
    2. **Mejorar Tiempos de Respuesta Comercial:**
       - El análisis de pérdidas indica que los clientes se enfrían ("por entregar tarde presupuesto").
    3. **Corregir Merchant Center:**
       - Actualizar la imagen del producto rechazado para reactivar su visibilidad.
    """)

with col2:
    st.warning("🟡 Mejoras de Proceso (Medio Plazo)")
    st.markdown("""
    1. **Implementar Flujo CRM:**
       - Formalizar los estados (Lead, Relevamiento, Presupuesto, Negociación).
       - Sistematizar el seguimiento (recordatorios a las 24h y 48h).
    2. **Filtro de Calidad (Palabras Negativas):**
       - Agregar palabras clave negativas en Google Ads para depurar aún más la calidad de los prospectos.
    3. **Landing Pages:**
       - Optimizar el diseño de las páginas de destino para incentivar directamente el formulario o el chat.
    """)

st.divider()
st.success("🟢 Proyección Estratégica: El Futuro CRM eQuantum")
st.markdown("""
La base de este dashboard evidencia la necesidad de un **CRM integral (eQuantum)** que conecte:
- **Captura automatizada:** Que cada clic en WhatsApp cree automáticamente un Lead en la base de datos.
- **Trazabilidad:** Que se sepa exactamente de qué campaña provino cada venta de ₲ 10.000.000.
- **Alertas de Seguimiento:** Que el vendedor reciba un ping cuando un presupuesto lleva 3 días sin respuesta.
""")
