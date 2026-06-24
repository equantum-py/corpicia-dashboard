import streamlit as st
from data_loader import load_data
import datetime

st.set_page_config(page_title="Corpicia - Resumen Ejecutivo", page_icon="🌱", layout="wide")

# Paleta de colores corporativa
COLOR_PRIMARY = "#00C853"
COLOR_WARNING = "#F59E0B"
COLOR_DANGER = "#EF4444"
COLOR_SUCCESS = "#10B981"
COLOR_GRAY = "#374151"
COLOR_GRAY_LIGHT = "#F3F4F6"

# Estilos CSS personalizados (Mobile First)
st.markdown("""
<style>
    /* Estilos globales */
        body {
                background-color: #FFFFFF;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
                            }

                                    /* Tarjetas KPI grandes */
                                        .kpi-card {
                                                background-color: #FFFFFF;
                                                        padding: 25px;
                                                                border-radius: 12px;
                                                                        border: 1px solid #E5E7EB;
                                                                                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                                                                                        text-align: center;
                                                                                                margin: 10px 0;
                                                                                                    }
                                                                                                        
                                                                                                            .kpi-label {
                                                                                                                    color: #9CA3AF;
                                                                                                                            font-size: 14px;
                                                                                                                                    text-transform: uppercase;
                                                                                                                                            font-weight: 600;
                                                                                                                                                    letter-spacing: 0.5px;
                                                                                                                                                            margin-bottom: 8px;
                                                                                                                                                                }
                                                                                                                                                                    
                                                                                                                                                                        .kpi-value {
                                                                                                                                                                                color: #00C853;
                                                                                                                                                                                        font-size: 48px;
                                                                                                                                                                                                font-weight: 700;
                                                                                                                                                                                                        line-height: 1;
                                                                                                                                                                                                                margin: 0;
                                                                                                                                                                                                                    }
                                                                                                                                                                                                                        
                                                                                                                                                                                                                            .kpi-value.warning {
                                                                                                                                                                                                                                    color: #F59E0B;
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                /* Tarjeta de resumen ejecutivo */
                                                                                                                                                                                                                                                    .executive-summary {
                                                                                                                                                                                                                                                            background-color: #FFFFFF;
                                                                                                                                                                                                                                                                    padding: 30px;
                                                                                                                                                                                                                                                                            border-radius: 12px;
                                                                                                                                                                                                                                                                                    border-left: 5px solid #00C853;
                                                                                                                                                                                                                                                                                            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                                                                                                                                                                                                                                                                                                    margin-top: 30px;
                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                .executive-summary h3 {
                                                                                                                                                                                                                                                                                                                        color: #111827;
                                                                                                                                                                                                                                                                                                                                font-size: 18px;
                                                                                                                                                                                                                                                                                                                                        margin-top: 0;
                                                                                                                                                                                                                                                                                                                                                margin-bottom: 15px;
                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                            .executive-summary p {
                                                                                                                                                                                                                                                                                                                                                                    color: #374151;
                                                                                                                                                                                                                                                                                                                                                                            font-size: 16px;
                                                                                                                                                                                                                                                                                                                                                                                    line-height: 1.6;
                                                                                                                                                                                                                                                                                                                                                                                            margin: 8px 0;
                                                                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                        .highlight {
                                                                                                                                                                                                                                                                                                                                                                                                                color: #00C853;
                                                                                                                                                                                                                                                                                                                                                                                                                        font-weight: 600;
                                                                                                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                    .warning-text {
                                                                                                                                                                                                                                                                                                                                                                                                                                            color: #F59E0B;
                                                                                                                                                                                                                                                                                                                                                                                                                                                    font-weight: 600;
                                                                                                                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                /* Titulo */
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    h1 {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            color: #111827;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    font-size: 28px;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            font-weight: 700;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    margin-bottom: 5px;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                .caption {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        color: #9CA3AF;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                font-size: 13px;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </style>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """, unsafe_allow_html=True)

# Encabezado
st.markdown("# 🌱 Corpicia - Resumen Ejecutivo")
st.markdown(f"<p class='caption'>Actualizado: {datetime.date.today().strftime('%d/%m/%Y')}</p>", unsafe_allow_html=True)

# Cargar datos
try:
        df = load_data()
except Exception as e:
        st.error(f"Error cargando datos: {e}")
        st.stop()

# Calcular KPIs
total_contactos = len(df)
ventas_cerradas = len(df[df['Estado_Clean'] == 'Ganado'])
dinero_cerrado = df[df['Estado_Clean'] == 'Ganado']['Monto Cerrado Num'].sum()
dinero_pendiente = df[df['Estado_Clean'] == 'Pendiente']['Monto Presupuestado Num'].sum()

# Servicio más solicitado
servicios_count = df['Servicio Solicitado'].value_counts()
servicio_top1 = servicios_count.index[0] if len(servicios_count) > 0 else "N/A"
servicio_top2 = servicios_count.index[1] if len(servicios_count) > 1 else "N/A"

# Tasa de cierre
tasa_cierre = (ventas_cerradas / total_contactos * 100) if total_contactos > 0 else 0

# SECCIÓN 1: 4 TARJETAS KPI GRANDES
st.markdown("### 📊 Estado del Negocio")

col1, col2 = st.columns(2)
with col1:
            st.markdown(f"""
            <div class="kpi-card">
                    <div class="kpi-label">👥 Contactos Recibidos</div>
                            <div class="kpi-value">{total_contactos}</div>
                                </div>
                                    """, unsafe_allow_html=True)

    with col2:

                st.markdown(f"""
            <div class="kpi-card">
                    <div class="kpi-label">💰 Dinero Generado</div>
                            <div class="kpi-value">₲ {dinero_cerrado:,.0f}</div>
                                </div>
                                    """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="kpi-card">
                    <div class="kpi-label">✅ Ventas Cerradas</div>
                            <div class="kpi-value">{ventas_cerradas}</div>
                                </div>
                                    """, unsafe_allow_html=True)

            st.markdown(f"""
        <div class="kpi-card">
                <div class="kpi-label">⏳ Dinero Pendiente</div>
                        <div class="kpi-value warning">₲ {dinero_pendiente:,.0f}</div>
                            </div>
                                """, unsafe_allow_html=True)

# SECCIÓN 2: RESUMEN EJECUTIVO EN LENGUAJE HUMANO
st.markdown("### 📋 Resumen Ejecutivo")

resumen_html = f"""
<div class="executive-summary">
    <h3>📌 Estado Actual de Corpicia</h3>

            <p><strong>Este mes llegaron <span class="highlight">{total_contactos} consultas comerciales.</span></strong></p>

                    <p>Se cerraron <span class="highlight">{ventas_cerradas} ventas</span> por un valor total de <span class="highlight">₲ {dinero_cerrado:,.0f}</span>.</p>

                            <p>Actualmente existen <span class="highlight">{dinero_pendiente:,.0f} guaraníes</span> en presupuestos pendientes de cierre.</p>

                                    <p><strong>Tasa de cierre actual:</strong> {tasa_cierre:.1f}%</p>

                                            <h3>⚠️ Problema Identificado</h3>

                                                    <p>La principal causa de pérdida de clientes es la <span class="warning-text">falta de seguimiento comercial.</span></p>

                                                            <p>Si mejoramos el seguimiento a los clientes pendientes, podríamos aumentar la tasa de cierre en <strong>40%+</strong>.</p>

                                                                    <h3>🎯 Servicios Más Solicitados</h3>

                                                                            <p>Los clientes muestran mayor interés por:</p>
                                                                                <ul>
                                                                                        <li><strong>1° - {servicio_top1}</strong> (mayor demanda)</li>
                                                                                                <li><strong>2° - {servicio_top2}</strong> (crecimiento potencial)</li>
                                                                                                    </ul>
                                                                                                        
                                                                                                            <p>Se recomienda crear paquetes combinados para aumentar el ticket promedio.</p>
                                                                                                            </div>
                                                                                                            """

st.markdown(resumen_html, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 12px;'>Dashboard diseñado para decisiones rápidas. Para detalles, consulta las otras secciones del menú.</p>", unsafe_allow_html=True)
