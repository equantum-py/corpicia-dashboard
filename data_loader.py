import streamlit as st
import pandas as pd
import numpy as np
import re
import os

@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'PROSPECTOS_CORPICIA.xlsx')
    df = pd.read_excel(file_path)
    
    # Renombrar columnas para facilitar manejo
    df.columns = ['ID', 'Fecha', 'Prospecto', 'Celular', 'Servicio Solicitado', 'Lugar', 'Avance', 'Estado', 'Monto Presupuestado', 'Monto Cerrado', 'Observaciones']
    
    # Rellenar nulos en categoras importantes
    df['Estado'] = df['Estado'].fillna('Pendiente').str.strip()
    df['Lugar'] = df['Lugar'].fillna('Desconocido').str.strip()
    df['Servicio Solicitado'] = df['Servicio Solicitado'].fillna('Sin Especificar').str.strip()
    df['Observaciones'] = df['Observaciones'].fillna('')
    df['Avance'] = df['Avance'].fillna('Sin avance registrado')
    
    def clean_money(val):
        if pd.isna(val):
            return 0.0
        if isinstance(val, (int, float)):
            return float(val)
        val = str(val).upper().replace('GS.', '').replace('GS', '').replace('.', '').replace(',', '').replace(' ', '')
        nums = re.findall(r'-?\d+', val)
        if nums:
            return float(''.join(nums))
        return 0.0
        
    df['Monto Presupuestado Num'] = df['Monto Presupuestado'].apply(clean_money)
    df['Monto Cerrado Num'] = df['Monto Cerrado'].apply(clean_money)
    
    # Normalizar el estado: Cerrado, Perdido, Pendiente (u otros asumiendolos como pendientes)
    # A veces en Excel dice "Ganado" en vez de "Cerrado"
    df['Estado_Clean'] = df['Estado'].apply(lambda x: 'Ganado' if 'cerra' in x.lower() or 'ganad' in x.lower() else ('Perdido' if 'perdi' in x.lower() else 'Pendiente'))
    
    return df
