import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="Contactos", page_icon="👤", layout="wide")

# Estilos CSS para mejor UX
st.markdown("""
<style>
    .contact-card {
            background-color: #FFFFFF;
                    padding: 15px;
                            border-radius: 8px;
                                    border: 1px solid #E5E7EB;
                                            margin-bottom: 10px;
                                                }

                                                        .status-ganado {
                                                                background-color: #DCFCE7;
                                                                        color: #15803D;
                                                                                padding: 4px 8px;
                                                                                        border-radius: 4px;
                                                                                                font-size: 12px;
                                                                                                        font-weight: 600;
                                                                                                            }
                                                                                                                
                                                                                                                    .status-pendiente {
                                                                                                                            background-color: #FEF3C7;
                                                                                                                                    color: #92400E;
                                                                                                                                            padding: 4px 8px;
                                                                                                                                                    border-radius: 4px;
                                                                                                                                                            font-size: 12px;
                                                                                                                                                                    font-weight: 600;
                                                                                                                                                                        }
                                                                                                                                                                            
                                                                                                                                                                                .status-perdido {
                                                                                                                                                                                        background-color: #FEE2E2;
                                                                                                                                                                                                color: #991B1B;
                                                                                                                                                                                                        padding: 4px 8px;
                                                                                                                                                                                                                border-radius: 4px;
                                                                                                                                                                                                                        font-size: 12px;
                                                                                                                                                                                                                                font-weight: 600;
                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                    </style>
                                                                                                                                                                                                                                    """, unsafe_allow_html=True)

st.title("👤 Gestión de Contactos")
st.markdown("CRM simple para administrar prospectospor estado, ubicación, servicio y fecha.")

df = load_data()

# SECCIÓN DE BÚSQUEDA Y FILTROS
st.markdown("### 🔍 Buscar y Filtrar")

col1, col2 = st.columns([2, 1])
with col1:
        search = st.text_input("🔎 Buscar por nombre o ciudad", placeholder="Ej: María García, Asunción")

with col2:
        st.markdown("")
        st.markdown("")
        if st.button("🔄 Limpiar búsqueda"):
                    st.rerun()

    # FILTROS AVANZADOS
    with st.expander("⚙️ Filtros Avanzados", expanded=False):
            col1, col2, col3, col4 = st.columns(4)

    with col1:
                f_estado = st.multiselect(
                                "Estado",
                                options=df['Estado_Clean'].unique(),
                                default=None
                )

    with col2:
                f_ciudad = st.multiselect(
                                "Ciudad",
                                options=sorted(df['Lugar'].unique()),
                                default=None
                )

    with col3:
                f_servicio = st.multiselect(
                                "Servicio",
                                options=sorted(df['Servicio Solicitado'].unique()),
                                default=None
                )

    with col4:
                f_fecha = st.multiselect(
                                "Fecha",
                                options=sorted(df['Fecha'].dropna().unique(), reverse=True),
                                default=None
                )

# APLICAR FILTROS
filtered_df = df.copy()

if search:
        search_lower = search.lower()
        filtered_df = filtered_df[
            filtered_df['Prospecto'].str.lower().str.contains(search_lower, na=False) |
            filtered_df['Lugar'].str.lower().str.contains(search_lower, na=False)
    ]

if f_estado:
        filtered_df = filtered_df[filtered_df['Estado_Clean'].isin(f_estado)]

if f_ciudad:
        filtered_df = filtered_df[filtered_df['Lugar'].isin(f_ciudad)]

if f_servicio:
        filtered_df = filtered_df[filtered_df['Servicio Solicitado'].isin(f_servicio)]

if f_fecha:
        filtered_df = filtered_df[filtered_df['Fecha'].isin(f_fecha)]

# RESUMEN DE RESULTADOS
st.markdown("### 📊 Resultados")
col1, col2, col3, col4 = st.columns(4)

with col1:
        st.metric("Total Contactos", len(filtered_df))

with col2:
        ganados = len(filtered_df[filtered_df['Estado_Clean'] == 'Ganado'])
        st.metric("Ganados", ganados)

with col3:
        pendientes = len(filtered_df[filtered_df['Estado_Clean'] == 'Pendiente'])
        st.metric("Pendientes", pendientes)

with col4:
        monto = filtered_df[filtered_df['Estado_Clean'] == 'Ganado']['Monto Cerrado Num'].sum()
        st.metric("Dinero Ganado", f"₲ {monto:,.0f}")

# TABLA PRINCIPAL
st.markdown("### 📋 Listado de Contactos")

if len(filtered_df) > 0:
        # Preparar datos para mostrar
        display_df = filtered_df[['Prospecto', 'Fecha', 'Lugar', 'Servicio Solicitado', 'Estado_Clean', 'Monto Presupuestado Num', 'Monto Cerrado Num']].copy()
        display_df.columns = ['Nombre', 'Fecha', 'Ciudad', 'Servicio', 'Estado', 'Presupuestado', 'Cerrado']

    # Formatear moneda
        display_df['Presupuestado'] = display_df['Presupuestado'].apply(lambda x: f"₲ {x:,.0f}" if x > 0 else "-")
        display_df['Cerrado'] = display_df['Cerrado'].apply(lambda x: f"₲ {x:,.0f}" if x > 0 else "-")

    # Mostrar tabla
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Estado": st.column_config.Column(width="medium")
            }
        )
else:
        st.info("No se encontraron contactos con los filtros seleccionados.")

# FOOTER
st.divider()
st.caption(f"Mostrando {len(filtered_df)} de {len(df)} contactos totales.")
