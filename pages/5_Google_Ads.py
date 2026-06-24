import streamlit as st

st.set_page_config(page_title="Google Ads", page_icon="📢", layout="wide")

st.title("📢 ¿Cómo está funcionando la publicidad?")
st.markdown("Revisión rápida de lo que estamos pagando en Google.")

st.markdown("""
<style>
.ads-box {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #E5E7EB;
    border-left: 5px solid #3B82F6;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    <div class="ads-box">
        <h3>👀 Personas Alcanzadas</h3>
        <p>El anuncio apareció en la pantalla de <strong>3,653 personas</strong>.</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="ads-box">
        <h3>👆 Clics Recibidos</h3>
        <p><strong>200 personas</strong> le dieron clic al anuncio para entrar a la web. Esto es muy bueno, significa que el anuncio llama la atención (CTR del 5,47%).</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="ads-box">
        <h3>💸 Inversión y Costo</h3>
        <p>Invertimos <strong>USD 96,10</strong>. Cada clic nos costó en promedio <strong>USD 0,48</strong> (muy económico).</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="ads-box">
        <h3>⚠️ Conclusión Automática</h3>
        <p style="color: #DC2626;"><strong>La publicidad atrae gente interesada y a buen precio, pero actualmente no se están midiendo correctamente todos los contactos que escriben por WhatsApp. Google cree que la campaña no funciona porque no le avisamos cuando alguien nos manda un mensaje. Hay que corregir eso.</strong></p>
    </div>
    ''', unsafe_allow_html=True)
