import streamlit as st
import pandas as pd
import plotly.express as px
import os
import pdfplumber
import re
from datetime import datetime

# ============================
# Configuración inicial
# ============================
EXCEL_PATH = "Inversión sistema fotovoltaico.xlsx"
EXCEL_SHEET = "Total"

# ============================
# Configurar la página principal
# ============================
st.set_page_config(
    page_title="Monitoreo Solar",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Lee el valor del secreto o usa uno por defecto
# Cambiamos esto a una variable de sesión
if 'INVERSION_INICIAL' not in st.session_state:
    st.session_state['INVERSION_INICIAL'] = 100000

LOGO_PATH = "logo_solar.png"

# ============================
# Funciones auxiliares
# ============================

def get_float_value(data, key, default=0.0):
    """Obtiene un valor float de un diccionario con manejo de errores"""
    value = data.get(key, default)
    try:
        return float(value) if value is not None else default
    except:
        return default

# ============================
# Cargar y preparar los datos
# ============================
def load_data_from_excel(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.columns = [col.strip() for col in df.columns]
        
        numeric_cols = ['Ahorro Total', 'Básico Solar', 'Intermedio 1 Solar', 'Intermedio 2 Solar', 
                       'Excedente Solar', 'Básico CFE', 'Intermedio 1 CFE', 'Intermedio 2 CFE', 
                       'Excedente CFE', 'Subtotal Solar', 'IVA Solar', 'Total de recibo Solar', 
                       'Subtotal CFE', 'IVA CFE', 'Subtotal CFE.1']
        
        for col in numeric_cols:
            if col in df.columns:
                try:
                    df[col] = df[col].replace("[\\$,]", "", regex=True).astype(float)
                except:
                    st.warning(f"No se pudo convertir la columna {col} a numérica")
        
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return pd.DataFrame()

df = load_data_from_excel(EXCEL_PATH, EXCEL_SHEET)

# Ajustar nombre de columna según sea necesario
periodo_col = "Periodos" if "Periodos" in df.columns else "Periodo"
origen_col = "Origen" if "Origen" in df.columns else None

# ============================
# Funciones para procesar PDFs
# ============================
def procesar_recibo_pdf(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        
        datos = {
            "periodo_facturado": extraer_patron(r"PERIODO FACTURADO:\s*(.*?)\n", text),
            "total_pagar": extraer_numero(r"TOTAL A PAGAR:\s*\$\s*([\d,]+)", text),
            "energia_total_kwh": extraer_numero(r"Energía\s*\(kWh\)\s+(\d+,\d+|\d+)", text),
            "consumo_total_periodo": extraer_numero(r"Energía\s*\(kWh\)\s+.*?\s+.*?\s+(\d+,\d+|\d+)", text),
            
            # Básico
            "basico_kwh": extraer_numero(r"Básico\s+(\d+,\d+|\d+)\s+(\d+,\d+|\d+)\s+(\d+)", text, group=3),
            "basico_precio": extraer_numero(r"Básico\s+.*?(\d+\.\d+)\s+(\d+\.\d+)", text, group=1),
            "basico_subtotal": extraer_numero(r"Básico\s+.*?\s+(\d+\.\d+)\s+(\d+\.\d+)", text, group=2),
            
            # Intermedio
            "intermedio_kwh": extraer_numero(r"Intermedio\s+(\d+,\d+|\d+)\s+(\d+\.\d+)", text, group=1),
            "intermedio_precio": extraer_numero(r"Intermedio\s+(\d+,\d+|\d+)\s+(\d+\.\d+)", text, group=2),
            "intermedio_subtotal": extraer_numero(r"Intermedio\s+.*?\s+(\d+\.\d+)\s+(\d+\.\d+)", text, group=3),
            
            # Excedente
            "excedente_kwh": extraer_numero(r"Excedente\s+(\d+,\d+|\d+)\s+(\d+\.\d+)", text, group=1),
            "excedente_precio": extraer_numero(r"Excedente\s+(\d+,\d+|\d+)\s+(\d+\.\d+)", text, group=2),
            "excedente_subtotal": extraer_numero(r"Excedente\s+.*?\s+(\d+\.\d+)\s+(\d+\.\d+)", text, group=3),
            
            "apoyo_gubernamental": extraer_numero(r"Apoyo Gubernamental\s+([\d\.,]+)", text),
        }
        
        return datos
    except Exception as e:
        st.error(f"Error al procesar PDF: {str(e)}")
        return None

def extraer_patron(patron, texto, group=1):
    try:
        match = re.search(patron, texto, re.DOTALL)
        return match.group(group).strip() if match else ""
    except:
        return ""

def extraer_numero(patron, texto, group=1):
    try:
        match = re.search(patron, texto, re.DOTALL)
        if match:
            try:
                valor = match.group(group).replace(",", "")
                return float(valor) if '.' in valor else float(valor)
            except:
                return 0.0
        return 0.0
    except:
        return 0.0

# ============================
# Sidebar - Logo y filtros
# ============================
with st.sidebar:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_column_width=True)
           
    # ============================
    # Sidebar - Carga de recibo de luz
    # ============================
            
    st.markdown("## Cargar Recibo de Luz (PDF)")
    
    uploaded_file = st.file_uploader("Sube tu recibo CFE en PDF", type="pdf", key="pdf_uploader")
    
    if uploaded_file is not None:
        datos_recibo = procesar_recibo_pdf(uploaded_file)
        
        if datos_recibo:
            st.success("Recibo procesado correctamente!")
            
            with st.expander("Ver datos extraídos", expanded=False):
                st.json(datos_recibo)
            
            # Pre-llenar el formulario con los datos del PDF
            try:
                periodo_pdf = datos_recibo.get("periodo_facturado", "").replace(" - ", " al ")
                st.session_state["nuevo_periodo"] = periodo_pdf if periodo_pdf else ""
                
                consumo_total = get_float_value(datos_recibo, "consumo_total_periodo")
                #precio_basico = get_float_value(datos_recibo, "basico_precio")
                #precio_intermedio = get_float_value(datos_recibo, "intermedio_precio")
                #precio_excedente = get_float_value(datos_recibo, "excedente_precio")
                
                st.session_state["precio_basico"] = get_float_value(datos_recibo, "basico_precio")
                st.session_state["precio_intermedio"] = get_float_value(datos_recibo, "intermedio_precio")
                st.session_state["precio_excedente"] = get_float_value(datos_recibo, "excedente_precio")

                # Lógica para Básico CFE
                if consumo_total > 150:
                    st.session_state["nuevo_basico_cfe"] = 150 
                else:
                    st.session_state["nuevo_basico_cfe"] = consumo_total 

                # Lógica para Intermedio 1 CFE
                if consumo_total > 150:
                    if consumo_total > 350:
                        st.session_state["nuevo_intermedio1_cfe"] = 200 
                    else:
                        st.session_state["nuevo_intermedio1_cfe"] = (consumo_total - st.session_state["nuevo_basico_cfe"])
                else:
                    st.session_state["nuevo_intermedio1_cfe"] = 0

                # Lógica para Excedente CFE
                #if consumo_total > 350:
                 #   st.session_state["nuevo_excedente_cfe"] = (consumo_total - (st.session_state["nuevo_basico_cfe"] + st.session_state["nuevo_intermedio1_cfe"]))
               # else:
                #    st.session_state["nuevo_excedente_cfe"] = 0     
                               
                #st.info("Los campos del formulario se han pre-llenado con los datos del recibo. Verifica y ajusta si es necesario.")
                
                # Lógica para Excedente CFE
                st.session_state["nuevo_excedente_cfe"] = get_float_value(datos_recibo, "excedente_kwh")   
                
                # Lógica para devolucion a la red
                st.session_state["MWh_devueltos"] = consumo_total - st.session_state["nuevo_basico_cfe"] - st.session_state["nuevo_intermedio1_cfe"] - st.session_state["nuevo_excedente_cfe"]


                st.info("Los campos del formulario se han pre-llenado con los datos del recibo. Verifica y ajusta si es necesario.")
             
                      
            except Exception as e:
                st.error(f"Error al cargar datos en el formulario: {str(e)}")
                                
    # ============================
    # Sección para actualizar la meta de inversión
    # ============================
    
    st.markdown("## Configuración de Meta")
    with st.expander("Actualizar Meta de Ahorro"):
        
        nueva_meta = st.number_input(
            "Meta de inversión a recuperar ($)", 
            min_value=0.0, 
            value=float(st.session_state['INVERSION_INICIAL']),
            step=1000.0,
            format="%.2f"
        )
        
        if st.button("Actualizar Meta"):
            st.session_state['INVERSION_INICIAL'] = nueva_meta
            st.success(f"Meta actualizada a ${nueva_meta:,.2f}")
    
    # ============================
    # Sidebar - Filtros
    # ============================
    
    st.markdown("## Filtros")
    with st.expander("Filtros"):
        opciones_periodo = ["Seleccionar todo"] + list(df[periodo_col].unique()) if not df.empty else ["Seleccionar todo"]
        seleccion_periodo = st.multiselect('Selecciona periodos', opciones_periodo, default=["Seleccionar todo"])
        
        df_filtrado = df.copy()
        if seleccion_periodo and "Seleccionar todo" not in seleccion_periodo:
            df_filtrado = df_filtrado[df_filtrado[periodo_col].isin(seleccion_periodo)]
        
        if origen_col:
            opciones_origen = ["Seleccionar todo"] + list(df[origen_col].unique()) if not df.empty else ["Seleccionar todo"]
            seleccion_origen = st.multiselect('Selecciona origen', opciones_origen, default=["Seleccionar todo"])
            if seleccion_origen and "Seleccionar todo" not in seleccion_origen:
                df_filtrado = df_filtrado[df_filtrado[origen_col].isin(seleccion_origen)]
        
        opciones_nivel = ["Seleccionar todo"] + ['Básico', 'Intermedio 1', 'Intermedio 2', 'Excedente']
        seleccion_nivel = st.multiselect('Selecciona nivel de cobro', opciones_nivel, default=["Seleccionar todo"])
        if seleccion_nivel and "Seleccionar todo" not in seleccion_nivel:
            columnas_nivel = [col for col in df.columns if any(n in col for n in seleccion_nivel)]
            df_filtrado = df_filtrado[[periodo_col] + ([origen_col] if origen_col else []) + columnas_nivel]
            
    # ============================
    # Menú para ingresar datos
    # ============================
    st.markdown("## Ingresar Datos")
    with st.expander("Nuevo Registro"):
        with st.form(key='ingreso_datos_form'):
            # Campo de período
            nuevo_periodo = st.text_input(
                "Nuevo Período", 
                value=st.session_state.get("nuevo_periodo", ""),
                key="periodo_input"
            )
            
            # Campos solares (siempre comienzan en 0)
            nuevo_basico_solar = st.number_input(
                "Básico Solar", 
                min_value=0.0, 
                format="%.2f", 
                value=0.0,
                key="basico_solar_input"
            )
            nuevo_intermedio1_solar = st.number_input(
                "Intermedio 1 Solar", 
                min_value=0.0, 
                format="%.2f", 
                value=0.0,
                key="intermedio1_solar_input"
            )
            nuevo_intermedio2_solar = st.number_input(
                "Intermedio 2 Solar", 
                min_value=0.0, 
                format="%.2f", 
                value=0.0,
                key="intermedio2_solar_input"
            )
            nuevo_excedente_solar = st.number_input(
                "Excedente Solar", 
                min_value=0.0, 
                format="%.2f", 
                value=0.0,
                key="excedente_solar_input"
            )
            
            # Campos CFE con valores predefinidos del PDF o 0
            nuevo_basico_cfe = st.number_input(
                "Básico CFE", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("nuevo_basico_cfe", 0.0)),
                key="basico_cfe_input"
            )
            nuevo_intermedio1_cfe = st.number_input(
                "Intermedio 1 CFE", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("nuevo_intermedio1_cfe", 0.0)),
                key="intermedio1_cfe_input"
            )
            nuevo_intermedio2_cfe = st.number_input(
                "Intermedio 2 CFE", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("nuevo_intermedio2_cfe", 0.0)),
                key="intermedio2_cfe_input"
            )
            nuevo_excedente_cfe = st.number_input(
                "Excedente CFE", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("nuevo_excedente_cfe", 0.0)),
                key="excedente_cfe_input"
            )
            
            # Campos de precios por nivel
            precio_basico = st.number_input(
                "Precio Básico", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("precio_basico", 0.0)),
                key="basico_precio_input"
            )
            precio_intermedio = st.number_input(
                "Precio Intermedio", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("precio_intermedio", 0.0)),
                key="precio_intermedio_input"
            )
            precio_excedente = st.number_input(
                "Precio Excedente", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("precio_excedente", 0.0)),
                key="precio_excedente_input"
            )
            
            # Campos de devolucion a la red
            MWh_devueltos = st.number_input(
                "Mwh Devueltos", 
                min_value=0.0, 
                format="%.2f", 
                value=float(st.session_state.get("MWh_devueltos", 0.0)),
                key="Mwh_devueltos_input"
            )

            submit_button = st.form_submit_button(label='Agregar Datos')
        
    if submit_button:
        try:
            # Convertir todos los valores a float explícitamente
            nuevo_basico_solar = float(nuevo_basico_solar)
            nuevo_intermedio1_solar = float(nuevo_intermedio1_solar)
            nuevo_intermedio2_solar = float(nuevo_intermedio2_solar)
            nuevo_excedente_solar = float(nuevo_excedente_solar)
            nuevo_basico_cfe = float(nuevo_basico_cfe)
            nuevo_intermedio1_cfe = float(nuevo_intermedio1_cfe)
            nuevo_intermedio2_cfe = float(nuevo_intermedio2_cfe)
            nuevo_excedente_cfe = float(nuevo_excedente_cfe)
            precio_basico = float(precio_basico)
            precio_intermedio = float(precio_intermedio)
            precio_excedente = float(precio_excedente)
            MWh_devueltos = float(MWh_devueltos)
            
            # Calcular campos faltantes para el nuevo registro
            if "No. Periodo" in df.columns:
                nuevo_num_periodo = df["No. Periodo"].max() + 1
            else:
                nuevo_num_periodo = 1
            
            # Datos de energia de paneles solares
            subtotal_solar = (
                (nuevo_basico_solar) + (nuevo_intermedio1_solar) + 
                (nuevo_intermedio2_solar) + (nuevo_excedente_solar)
            )
            
            iva_solar = subtotal_solar * 0.16
            total_recibo_solar = subtotal_solar + iva_solar
            
            
            # Datos de energia de recibo de CFE
            subtotal_cfe = (
                (nuevo_basico_cfe*precio_basico) + (nuevo_intermedio1_cfe*precio_intermedio) + 
                (nuevo_intermedio2_cfe) + (nuevo_excedente_cfe*precio_excedente)
            )
            
            iva_cfe = subtotal_cfe * 0.16
            total_cfe = subtotal_cfe + iva_cfe
            
            if MWh_devueltos <= 150:
                ahorro_total = MWh_devueltos * precio_basico
            elif MWh_devueltos <= 350:
                ahorro_basico = 150 * precio_basico
                ahorro_intermedio = (MWh_devueltos - 150) * precio_intermedio
                ahorro_total = ahorro_basico + ahorro_intermedio
            else:  # MWh_devueltos > 350
                ahorro_basico = 150 * precio_basico
                ahorro_intermedio = 200 * precio_intermedio
                ahorro_excedente = (MWh_devueltos - 350) * precio_excedente
                # Se corrigió el cálculo final para sumar la variable correcta.
                ahorro_total = ahorro_basico + ahorro_intermedio + ahorro_excedente
                                
            nuevo_registro = {
                periodo_col: nuevo_periodo,
                "No. Periodo": nuevo_num_periodo,
                "Básico Solar": nuevo_basico_solar,
                "Intermedio 1 Solar": nuevo_intermedio1_solar,
                "Intermedio 2 Solar": nuevo_intermedio2_solar,
                "Excedente Solar": nuevo_excedente_solar,
                "Básico CFE": nuevo_basico_cfe*precio_basico,
                "Intermedio 1 CFE": nuevo_intermedio1_cfe*precio_intermedio,
                "Intermedio 2 CFE": nuevo_intermedio2_cfe,
                "Excedente CFE": nuevo_excedente_cfe*precio_excedente,
                "Mwh Devueltos": MWh_devueltos,
                "Subtotal Solar": subtotal_solar,
                "IVA Solar": iva_solar,
                "Total de recibo Solar": total_recibo_solar,
                "Subtotal CFE": subtotal_cfe,
                "IVA CFE": iva_cfe,
                "Subtotal CFE.1": total_cfe, 
                "Ahorro Total": ahorro_total
            }
            
            # Agregar el nuevo registro al DataFrame
            df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
            
            # Guardar el DataFrame actualizado en el archivo Excel
            df.to_excel(EXCEL_PATH, sheet_name=EXCEL_SHEET, index=False)
            st.success("Datos agregados correctamente y guardados en el archivo!")
            
        except Exception as e:
            st.error(f"Error al procesar los datos: {str(e)}")
                        
    # Botón para borrar último registro
    if st.button('🗑️ Borrar último registro', key='borrar_registro'):
        if len(df) > 0:
            try:
                df_actualizado = df.iloc[:-1].copy()
                
                with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl', mode='w') as writer:
                    df_actualizado.to_excel(writer, sheet_name=EXCEL_SHEET, index=False)
                
                df = load_data_from_excel(EXCEL_PATH, EXCEL_SHEET)
                
                st.success(f"Registro del período {df.iloc[-1][periodo_col]} eliminado correctamente!")
                st.experimental_rerun()
                
            except Exception as e:
                st.error(f"Error al guardar cambios: {str(e)}")
        else:
            st.warning("No hay registros para eliminar")

# ============================
# Análisis clave
# ============================
st.title("Monitoreo del Ahorro y Recuperación de Inversión")

# Cálculo de métricas principales
# Cálculo de métricas principales
if not df_filtrado.empty:
    ahorro_acumulado = df_filtrado["Ahorro Total"].sum()
    pendiente_recuperar = max(0, st.session_state['INVERSION_INICIAL'] - ahorro_acumulado)
    progreso = (ahorro_acumulado / st.session_state['INVERSION_INICIAL']) * 100 if st.session_state['INVERSION_INICIAL'] > 0 else 0
    
    if len(df_filtrado) > 0 and ahorro_acumulado > 0:
        meses_faltantes = pendiente_recuperar / (ahorro_acumulado / len(df_filtrado))
    else:
        meses_faltantes = 0
        
    ahorro_promedio_mensual = ahorro_acumulado / len(df_filtrado) if len(df_filtrado) > 0 else 0
else:
    ahorro_acumulado = 0
    pendiente_recuperar = st.session_state['INVERSION_INICIAL']
    progreso = 0
    meses_faltantes = 0
    ahorro_promedio_mensual = 0
    
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Ahorro Acumulado", f"${ahorro_acumulado:,.2f}")
col2.metric("Pendiente para Recuperar", f"${pendiente_recuperar:,.2f}")
col3.metric("Porcentaje Recuperado", f"{progreso:.2f}%")
col4.metric("Meses Estimados Restantes", f"{meses_faltantes:.1f} meses")
col5.metric("Ahorro Promedio por Mes", f"${ahorro_promedio_mensual:,.2f}")

st.markdown(
    """
    <style>
        div[data-testid="stMetric"] {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        div[data-testid="stMetric"] > div:first-child {
            font-weight: bold;
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Gráficos de Análisis
if not df_filtrado.empty:
    st.subheader("Tendencia del Ahorro Acumulado")
    fig_ahorro = px.area(
        df_filtrado, x=periodo_col, y="Ahorro Total",
        title="Evolución del Ahorro por Periodo",
        markers=True, color_discrete_sequence=["#2ECC71"]
    )
    st.plotly_chart(fig_ahorro, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tiempo Estimado de Recuperación")
        fig_dona = px.pie(
            names=["Ahorro Total", "Restante"],
            values=[ahorro_acumulado, pendiente_recuperar],
            title="Progreso de Recuperación",
            hole=0.5,
            color_discrete_sequence=["#2ECC71", "#E74C3C"]
        )
        st.plotly_chart(fig_dona, use_container_width=True)

    with col2:
        st.subheader("Distribución Total de Costos por Nivel de Cobro")
        df_totales = df_filtrado[["Básico Solar", "Intermedio 1 Solar", "Intermedio 2 Solar", "Excedente Solar", 
                                  "Básico CFE", "Intermedio 1 CFE", "Intermedio 2 CFE", "Excedente CFE"]].sum().reset_index()
        df_totales.columns = ["Nivel de Cobro", "Costo Total"]
        fig_treemap = px.treemap(
            df_totales, path=["Nivel de Cobro"], values="Costo Total",
            title="Proporción Total de Costos por Nivel de Cobro",
            color="Costo Total", color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig_treemap, use_container_width=True)

    # Comparación entre Consumo Real y Estimado
    st.subheader("Comparación de Consumo Real vs Estimado")
    fig_comparativo = px.bar(
        df_filtrado, x=periodo_col, y=["Total de recibo Solar", "Subtotal CFE.1"],
        barmode="group", title="Consumo Real (Verde) vs Estimado (Amarillo)",
        color_discrete_map={"Total de recibo Solar": "#2ECC71", "Subtotal CFE.1": "#F4D03F"}
    )
    st.plotly_chart(fig_comparativo, use_container_width=True)

    # Periodo con Mayor Ahorro
    st.subheader("Periodo con Mayor Ahorro")
    mes_max_ahorro = df_filtrado.loc[df_filtrado['Ahorro Total'].idxmax()]
    st.write(f"El mes con mayor ahorro fue **{mes_max_ahorro[periodo_col]}** con un ahorro de **${mes_max_ahorro['Ahorro Total']:,.2f}**.")

    # Tabla resumen
    st.subheader("Tabla Resumen de Datos Filtrados")
    numeric_cols = df_filtrado.select_dtypes(include=['number']).columns
    st.dataframe(df_filtrado.style.format({col: "${:,.2f}" for col in numeric_cols}))
else:
    st.warning("No hay datos disponibles para mostrar los gráficos y análisis")

st.markdown("---")
st.write("_Monitoreo de paneles solares © 2024_", unsafe_allow_html=True)