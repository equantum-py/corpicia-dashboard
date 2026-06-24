import streamlit as st
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="CRM Pipeline", layout="wide")

st.title("🗂️ CRM Pipeline (Base eQuantum)")
st.markdown("Visualización de prospectos en formato de flujo de ventas.")

df = load_data()

# Mapeo heurístico de los estados y avances al nuevo pipeline CRM
def map_to_pipeline(row):
    estado = row['Estado_Clean']
    avance = str(row['Avance']).lower()
    
    if estado == 'Ganado':
        return '5. Ganado'
    elif estado == 'Perdido':
        return '6. Perdido'
    
    # Pendientes
    if 'relevamiento' in avance or 'visita' in avance:
        return '2. Relevamiento'
    elif 'presupuesto' in avance:
        return '3. Presupuesto'
    elif 'seguimiento' in avance or 'dialogo' in avance or 'diálogo' in avance:
        return '4. Seguimiento'
    else:
        return '1. Nuevo Lead'

df['Etapa_CRM'] = df.apply(map_to_pipeline, axis=1)

etapas = ['1. Nuevo Lead', '2. Relevamiento', '3. Presupuesto', '4. Seguimiento', '5. Ganado', '6. Perdido']

st.markdown("""
<style>
.kanban-col {
    background-color: #1E2127;
    border-radius: 8px;
    padding: 10px;
    min-height: 400px;
}
.kanban-card {
    background-color: #2D3748;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    border-left: 4px solid #3182CE;
}
.card-title {
    font-weight: bold;
    font-size: 14px;
    color: white;
}
.card-subtitle {
    font-size: 12px;
    color: #A0AEC0;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(len(etapas))

colors = {
    '1. Nuevo Lead': '#3182CE',
    '2. Relevamiento': '#805AD5',
    '3. Presupuesto': '#D69E2E',
    '4. Seguimiento': '#DD6B20',
    '5. Ganado': '#00C853',
    '6. Perdido': '#E53E3E'
}

for idx, etapa in enumerate(etapas):
    with cols[idx]:
        st.markdown(f"**{etapa}**", unsafe_allow_html=True)
        st.markdown(f'<div class="kanban-col">', unsafe_allow_html=True)
        
        subset = df[df['Etapa_CRM'] == etapa]
        for _, row in subset.iterrows():
            cliente = row['Prospecto']
            servicio = row['Servicio Solicitado']
            color = colors.get(etapa, '#3182CE')
            
            st.markdown(f'''
            <div class="kanban-card" style="border-left-color: {color};">
                <div class="card-title">{cliente}</div>
                <div class="card-subtitle">{servicio}</div>
            </div>
            ''', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.info("💡 Este tablero es una vista previa estática. En el CRM final, las tarjetas podrán arrastrarse y soltarse (Drag & Drop) y tendrán alertas automáticas.")
