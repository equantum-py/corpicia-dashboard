import streamlit as st

st.set_page_config(page_title="SEO Orgánico", page_icon="🔎", layout="wide")

st.title("🔎 ¿Cómo funciona Google Orgánico?")
st.markdown("Tráfico gratuito sin pagar publicidad.")

st.markdown("""
<style>
.seo-box {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #E5E7EB;
    border-left: 5px solid #10B981;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('''
<div class="seo-box">
    <h3>🌱 Gente que nos encuentra gratis</h3>
    <p>Aproximadamente el <strong>33% de los clientes</strong> que entran a nuestra web lo hacen buscando en Google de forma normal, sin que nosotros paguemos por ese clic.</p>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="seo-box">
    <h3>🏆 Lo que más atrae (Páginas de interés)</h3>
    <p>El posicionamiento gratuito funciona muy bien, especialmente para las búsquedas sobre:</p>
    <ul>
        <li>Césped Natural</li>
        <li>Jardinería general</li>
    </ul>
    <p><strong>Conclusión:</strong> El sitio está muy bien posicionado. Es tráfico gratuito que nos permite ahorrar en publicidad todos los meses. Deberíamos subir más fotos y contenidos de nuestros trabajos para que este número siga creciendo solo.</p>
</div>
''', unsafe_allow_html=True)
