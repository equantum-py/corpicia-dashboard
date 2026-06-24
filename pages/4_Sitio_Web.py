import streamlit as st

st.set_page_config(page_title="Sitio Web", page_icon="🌐", layout="wide")

st.title("🌐 ¿Cómo está funcionando la página web?")
st.markdown("Resumen simple de las visitas a la web.")

st.markdown("""
<style>
.web-box {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #E5E7EB;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    <div class="web-box">
        <h3>👥 ¿Cuánta gente nos visita?</h3>
        <p>Recibimos a <strong>215 personas</strong> en la página recientemente.</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="web-box">
        <h3>🔍 ¿Qué es lo que más miran?</h3>
        <ul>
            <li>Césped natural y jardinería</li>
            <li>Césped Esmeralda</li>
            <li>Césped Siempre Verde</li>
        </ul>
        <p><em>(La gente entra buscando pasto directamente)</em></p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="web-box">
        <h3>📍 ¿Desde qué ciudades?</h3>
        <p>Nuestros clientes web están principalmente en:</p>
        <ol>
            <li>Asunción</li>
            <li>Ciudad del Este</li>
            <li>Limpio</li>
        </ol>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="web-box">
        <h3>🚪 ¿Por dónde entran?</h3>
        <p>Más de la mitad (52%) llega porque vieron nuestro anuncio de Google. Un buen 33% nos encuentra gratis buscando en Google normalmente.</p>
    </div>
    ''', unsafe_allow_html=True)
