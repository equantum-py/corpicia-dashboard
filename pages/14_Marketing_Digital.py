import streamlit as st
import plotly.express as px
from data_loader import load_data

st.set_page_config(page_title="Marketing Digital", layout="wide")

st.title("🌐 Impacto de Marketing Digital")
st.markdown("Auditoría visual del ecosistema y embudo de adquisición.")

df = load_data()
ganados = len(df[df['Estado_Clean'] == 'Ganado'])
prospectos = len(df)

st.subheader("1. Embudo Completo de Adquisición (Full Funnel)")

# Datos auditados y extraídos
funnel_data = dict(
    number=[3653, 200, 215, 60, prospectos, ganados], # WhatsApp es un estimado conceptual para graficar el quiebre
    stage=["1. Impresiones (Google Ads)", "2. Clics (Ads)", "3. Usuarios Activos (GA4)", "4. Clics WhatsApp (Estimado)", "5. Prospectos Reales", "6. Ventas Cerradas"]
)

fig_funnel = px.funnel(funnel_data, x='number', y='stage', title='Funnel de Adquisición (Del Anuncio a la Venta)', template="plotly_dark")
fig_funnel.update_traces(marker=dict(color=['#718096', '#4A5568', '#2D3748', '#38B2AC', '#3182CE', '#00C853']))
st.plotly_chart(fig_funnel, use_container_width=True)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 Google Ads")
    st.markdown("""
    - **Impresiones:** 3.653
    - **Clics:** 200
    - **CTR:** 5,47% (Excelente)
    - **CPC:** USD 0,48
    - **Inversión:** USD 96,10
    
    > **Problema:** Google Ads reporta 0 conversiones. La falta de medición impide optimizar campañas.
    """)

with col2:
    st.markdown("### 📈 Google Analytics (GA4)")
    st.markdown("""
    - **Usuarios Activos:** 215
    - **Eventos:** 1.300
    - **Tráfico:** 52% Ads, 33% SEO, 10% Directo.
    - **WhatsApp:** El evento `whatsapp_click` existe y registra.
    
    > **Problema:** El evento de WhatsApp no está marcado como conversión ni vinculado de vuelta a Ads.
    """)

with col3:
    st.markdown("### 🛍️ Merchant Center & SEO")
    st.markdown("""
    - **SEO:** 33% del tráfico es orgánico, posicionamiento altamente funcional.
    - **Merchant Center:** 13 productos aprobados, 1 rechazado.
    
    > **Oportunidad:** Aumentar captación SEO y corregir el producto rechazado para maximizar visualización gratuita.
    """)

st.info("💡 **Diagnóstico General:** El marketing genera la demanda, pero la desconexión tecnológica (tracking) y la gestión comercial (seguimiento) rompen el embudo.")
