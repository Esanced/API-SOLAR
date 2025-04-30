import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

st.title("📚 Sección Educativa sobre Paneles Solares")

# ============================
# Sidebar con índice de temas
# ============================
with st.sidebar:
    st.header("📚 Temas de la Sección Educativa")
    seleccion = st.radio("Selecciona un tema:", [
        "Introducción a la Energía Solar",
        "Funcionamiento de los Paneles Solares",
        "Tipos de Paneles Solares",
        "Cálculo del Ahorro Energético y Financiero",
        "Beneficios de la Energía Solar",
        "Mantenimiento y Vida Útil",
        "Impacto Económico y Políticas de Incentivos",
        "Instalación y Requerimientos Técnicos",
        "Evolución Tecnológica de los Paneles Solares",
        "Energía Solar en el Mundo",
        "Comparación con Otras Energías Renovables",
        "Factores que Afectan el Rendimiento",
        "Almacenamiento de Energía Solar",
        "Normativas y Regulaciones",
        "Casos de Éxito y Proyectos Destacados",
        "Eficiencia de Inversión en Paneles Solares",
        "Impacto de las Condiciones Climáticas en el Rendimiento",
        "Diseño e Instalación de un Sistema Solar Residencial",
        "Tendencias Futuras en Energía Solar",
        "Integración de la Energía Solar con la Red Eléctrica"
    ])


# ============================
# Introducción a la Energía Solar
# ============================
if seleccion == "Introducción a la Energía Solar":
    st.header("🌞 Paneles Solares y Energía Solar: Una Alternativa Sustentable para el Futuro")
    st.write(
        "En las últimas décadas, la energía solar ha ganado protagonismo como una de las alternativas más prometedoras para la generación de energía sustentable. "
        "La crisis climática y el agotamiento de combustibles fósiles han impulsado la transición hacia fuentes renovables, y entre ellas, la energía solar se destaca por su abundancia, accesibilidad y bajo impacto ambiental."
    )
    
    st.subheader("La Energía Solar: Una Fuente Renovable")
    st.write(
        "La energía solar es una de las formas de energía renovable más importantes en la actualidad. Se obtiene a partir de la radiación solar, la cual puede ser convertida en electricidad o calor mediante diferentes tecnologías."
    )
    
    st.markdown("### Principales tecnologías de aprovechamiento de la energía solar")
    st.write("- **Energía solar fotovoltaica:** Conversión directa de la luz solar en electricidad mediante células fotovoltaicas.")
    st.write("- **Energía solar térmica:** Captación del calor del sol para calefacción y generación de electricidad en plantas termosolares.")
    st.write("- **Energía solar pasiva:** Diseño arquitectónico que aprovecha la luz solar para iluminación y regulación térmica de edificios.")
    
    st.subheader("Beneficios de la Energía Solar")
    st.write("- **Inagotable y renovable:** El sol emite más energía en una hora de la que el mundo consume en un año.")
    st.write("- **Reducción de emisiones:** No genera gases de efecto invernadero durante su operación.")
    st.write("- **Accesible en zonas remotas:** Permite llevar electricidad a comunidades aisladas sin conexión a la red.")
    st.write("- **Mantenimiento bajo:** Requiere solo limpieza ocasional y revisiones periódicas.")
    
    st.subheader("Desafíos de la Energía Solar")
    st.write("- **Dependencia de la luz solar:** La eficiencia disminuye en días nublados o en la noche.")
    st.write("- **Costo inicial elevado:** Aunque ha disminuido en los últimos años, la inversión inicial sigue siendo alta.")
    st.write("- **Espacio necesario:** Grandes instalaciones requieren superficies amplias para generar suficiente energía.")
    
    # Gráfico de crecimiento de la energía solar en el mundo con diseño mejorado
    data = pd.DataFrame({
        "Año": [2010, 2012, 2014, 2016, 2018, 2020, 2022],
        "Capacidad Global (GW)": [40, 100, 180, 300, 480, 710, 1000]
    })
    fig = px.line(data, x="Año", y="Capacidad Global (GW)", title="📈 Crecimiento de la Energía Solar en el Mundo", markers=True, line_shape='spline', color_discrete_sequence=['#F39C12'])
    st.plotly_chart(fig)

    # Mapa de países con mayor uso de energía solar
    data_map = pd.DataFrame({
        "País": ["China", "Estados Unidos", "Alemania", "India", "Japón", "España", "Australia"],
        "Capacidad Instalada (GW)": [306, 95, 58, 49, 68, 18, 27],
        "Latitud": [35.8617, 37.0902, 51.1657, 20.5937, 36.2048, 40.4637, -25.2744],
        "Longitud": [104.1954, -95.7129, 10.4515, 78.9629, 138.2529, -3.7492, 133.7751]
    })
    fig_map = px.scatter_geo(
        data_map, lat="Latitud", lon="Longitud", size="Capacidad Instalada (GW)",
        hover_name="País", title="🌍 Países con Mayor Uso de Energía Solar",
        color_discrete_sequence=["#F39C12"]
    )
    st.plotly_chart(fig_map)

    # Comparación del uso de energía renovable
    data_comp = pd.DataFrame({
        "Fuente": ["Solar", "Eólica", "Hidroeléctrica", "Geotérmica"],
        "Porcentaje Uso Mundial": [25, 35, 30, 10]
    })
    fig_comp = px.pie(data_comp, names="Fuente", values="Porcentaje Uso Mundial", title="🔄 Comparación de Energías Renovables", color_discrete_sequence=["#F39C12", "#3498DB", "#2ECC71", "#E74C3C"])
    st.plotly_chart(fig_comp)

    # Tabla de eficiencia de paneles solares por tipo
    data_eff = pd.DataFrame({
        "Tipo de Panel": ["Monocristalino", "Policristalino", "Película Delgada"],
        "Eficiencia (%)": [22, 18, 12]
    })
    st.subheader("📊 Eficiencia de Diferentes Tipos de Paneles Solares")
    st.table(data_eff)

# ============================
# Funcionamiento de los Paneles Solares
# ============================
if seleccion == "Funcionamiento de los Paneles Solares":
    st.header("🔆 ¿Cómo funcionan los paneles solares?")
    st.write(
        "Los paneles solares convierten la luz solar en electricidad mediante el efecto fotovoltaico. "
        "Cuando los fotones impactan una célula fotovoltaica, liberan electrones, generando una corriente eléctrica."
    )
    
    st.subheader("Estructura y Materiales de un Panel Solar")
    st.write(
        "Un panel solar está compuesto por múltiples celdas fotovoltaicas conectadas en serie y protegidas por una capa de vidrio templado. "
        "Los materiales más comunes en los paneles solares incluyen el silicio monocristalino y policristalino, que determinan su eficiencia y costo."
    )
    
    st.subheader("🔬 Principio del Efecto Fotovoltaico")
    st.write(
        "El efecto fotovoltaico es el fenómeno físico que permite la conversión de la luz en electricidad. "
        "Ocurre cuando los fotones de la luz solar excitan los electrones en un material semiconductor, creando una diferencia de potencial que genera corriente eléctrica."
    )
    
    # Gráfico ilustrativo del efecto fotovoltaico
    data_efecto = pd.DataFrame({
        "Proceso": ["Fotón impacta célula", "Electrones excitados", "Generación de corriente"],
        "Energía (eV)": [1.1, 1.5, 2.0]
    })
    fig_efecto = px.bar(data_efecto, x="Proceso", y="Energía (eV)", title="🔋 Proceso del Efecto Fotovoltaico", color="Proceso", color_discrete_sequence=["#F39C12"])
    st.plotly_chart(fig_efecto)

    st.subheader("⚙️ Componentes de un Sistema Solar Fotovoltaico")
    st.write("Para que un sistema fotovoltaico funcione correctamente, se requieren los siguientes componentes:")
    st.write("- **Paneles solares:** Captan la radiación solar y la convierten en electricidad.")
    st.write("- **Inversor:** Convierte la corriente continua en corriente alterna utilizable.")
    st.write("- **Baterías:** Almacenan energía para su uso posterior.")
    st.write("- **Controlador de carga:** Regula el flujo de energía entre los paneles y las baterías.")
    
    # Gráfico de flujo de energía en un sistema fotovoltaico
    data_flujo = pd.DataFrame({
        "Componente": ["Panel Solar", "Inversor", "Batería", "Consumo Hogar"],
        "Flujo de Energía (W)": [100, 90, 80, 70]
    })
    fig_flujo = px.funnel(data_flujo, x="Componente", y="Flujo de Energía (W)", title="🔄 Flujo de Energía en un Sistema Solar")
    st.plotly_chart(fig_flujo)

    st.subheader("🌍 Factores que Afectan la Eficiencia de los Paneles Solares")
    st.write("- **Ángulo de inclinación:** Un ángulo óptimo maximiza la captación de energía solar.")
    st.write("- **Temperatura:** El calor excesivo puede reducir la eficiencia de conversión eléctrica.")
    st.write("- **Sombras y obstrucciones:** Árboles o edificios pueden afectar la producción de energía.")
    st.write("- **Tipo de panel:** Los paneles monocristalinos son más eficientes que los policristalinos o de película delgada.")

    # Gráfico de pérdida de eficiencia según la temperatura
    data_temp = pd.DataFrame({
        "Temperatura (°C)": [0, 10, 20, 30, 40],
        "Eficiencia (%)": [100, 98, 95, 90, 85]
    })
    fig_temp = px.line(data_temp, x="Temperatura (°C)", y="Eficiencia (%)", title="🌡️ Impacto de la Temperatura en la Eficiencia de Paneles Solares", markers=True, color_discrete_sequence=['#E74C3C'])
    st.plotly_chart(fig_temp)

    st.subheader("🔗 Conexión de los Paneles Solares a la Red")
    st.write(
        "Los sistemas solares pueden operar de manera independiente (fuera de la red) o estar conectados a la red eléctrica pública, "
        "lo que permite vender el exceso de energía generada a las compañías eléctricas mediante el sistema de medición neta."
    )

    # Gráfico del flujo de energía con conexión a la red
    data_conexion = pd.DataFrame({
        "Fuente": ["Paneles Solares", "Baterías", "Red Eléctrica"],
        "Energía Disponible (kWh)": [500, 300, 700]
    })
    fig_conexion = px.bar(data_conexion, x="Fuente", y="Energía Disponible (kWh)", title="⚡ Conexión de un Sistema Solar con la Red Pública", color="Fuente", color_discrete_sequence=["#2ECC71", "#3498DB", "#F39C12"])
    st.plotly_chart(fig_conexion)

# ============================
# Cálculo del Ahorro Energético y Métricas de Evaluación
# ============================
if seleccion == "Cálculo del Ahorro Energético y Financiero":
    st.header("📊 Cálculo del Ahorro Energético y Métricas de Evaluación")
    st.write(
        "Para determinar el ahorro energético proporcionado por un sistema solar, se utilizan diversas fórmulas y métricas. "
        "Estos cálculos permiten evaluar la viabilidad económica de la inversión y estimar el tiempo necesario para recuperar el costo inicial."
    )
    
    st.subheader("Producción Energética Anual (PEA)")
    st.latex(r""" PEA = P_{panel} \times HSP \times D \times \eta """
    )
    st.write(
        "Esta fórmula calcula la cantidad de energía generada anualmente por el sistema solar. "
        "Depende de la potencia del panel (P_{panel}), las horas solares pico por día (HSP), el número de días al año (D) y la eficiencia del sistema (η)."
    )
    
    # Gráfico de impacto de la eficiencia en la producción anual
    data_pea = pd.DataFrame({
        "Eficiencia (%)": [10, 15, 20, 25, 30],
        "Energía Generada (kWh)": [500, 750, 1000, 1250, 1500]
    })
    fig_pea = px.line(data_pea, x="Eficiencia (%)", y="Energía Generada (kWh)",
                      title="📈 Impacto de la Eficiencia en la Producción Anual", markers=True, color_discrete_sequence=['#F39C12'])
    st.plotly_chart(fig_pea)
    
    st.subheader("Retorno de Inversión (ROI)")
    st.latex(r""" ROI = \frac{Ahorro\ Anual}{Costo\ Total} \times 100 """
    )
    st.write(
        "El retorno de inversión (ROI) indica el porcentaje del costo total que se recupera anualmente a través del ahorro en electricidad. "
        "Un ROI alto significa que el sistema solar es una inversión rentable a largo plazo."
    )
    
    # Comparación de ROI según costo de instalación
    data_roi = pd.DataFrame({
        "Costo Total (USD)": [5000, 10000, 15000, 20000, 25000],
        "ROI (%)": [40, 30, 25, 20, 18]
    })
    fig_roi = px.bar(data_roi, x="Costo Total (USD)", y="ROI (%)", title="💰 Relación entre Costo de Instalación y ROI", color="Costo Total (USD)", color_continuous_scale="Blues")
    st.plotly_chart(fig_roi)
    
    st.subheader("Tiempo de Retorno (Payback Period)")
    st.latex(r""" T = \frac{Costo\ Total}{Ahorro\ Anual} """
    )
    st.write(
        "El tiempo de retorno (payback period) es el número de años necesarios para recuperar la inversión inicial a través del ahorro energético. "
        "Este cálculo ayuda a determinar cuándo comenzará a generar beneficios el sistema solar."
    )
    
    # Gráfico de tiempo de retorno
    data_payback = pd.DataFrame({
        "Ahorro Anual (USD)": [500, 1000, 1500, 2000, 2500],
        "Tiempo de Retorno (años)": [10, 8, 6, 5, 4]
    })
    fig_payback = px.line(data_payback, x="Ahorro Anual (USD)", y="Tiempo de Retorno (años)",
                          title="⏳ Relación entre Ahorro Anual y Tiempo de Retorno", markers=True, color_discrete_sequence=['#E74C3C'])
    st.plotly_chart(fig_payback)
    
    st.subheader("📌 Factores que Afectan el Ahorro Energético")
    st.write("El ahorro energético no solo depende de la capacidad del sistema solar, sino también de otros factores como:")
    st.write("- **Ubicación y clima:** Más horas de sol equivalen a mayor producción de energía.")
    st.write("- **Consumo eléctrico del usuario:** Mientras mayor sea el consumo, mayor será el impacto del sistema solar.")
    st.write("- **Costo de la electricidad:** En lugares con tarifas eléctricas elevadas, el ahorro generado es más significativo.")
    
    # Comparación de ahorro en diferentes regiones
    data_region = pd.DataFrame({
        "Región": ["California", "Texas", "España", "Alemania", "México"],
        "Ahorro Promedio Anual (USD)": [1800, 1200, 1500, 900, 1300]
    })
    fig_region = px.bar(data_region, x="Región", y="Ahorro Promedio Anual (USD)", title="🌍 Ahorro Anual Promedio por Región", color="Región", color_discrete_sequence=["#3498DB"])
    st.plotly_chart(fig_region)

# ============================
# Beneficios de la Energía Solar
# ============================
if seleccion == "Beneficios de la Energía Solar":
    st.header("🌍 Beneficios de la Energía Solar")
    st.write(
        "La energía solar presenta múltiples ventajas tanto para el medio ambiente como para la economía. "
        "Desde la reducción de costos hasta la disminución de emisiones de carbono, su adopción está en crecimiento global."
    )
    
    st.subheader("🔋 Beneficios Ambientales")
    st.write("- **Cero emisiones:** No genera gases de efecto invernadero durante su operación.")
    st.write("- **Menor contaminación del agua:** No requiere grandes cantidades de agua para su funcionamiento, a diferencia de otras fuentes de energía.")
    st.write("- **Reducción de la huella de carbono:** Ayuda a combatir el cambio climático mediante la descarbonización del sector energético.")
    
    # Gráfico de reducción de CO₂ con energía solar
    data_co2 = pd.DataFrame({
        "Fuente de Energía": ["Carbón", "Gas Natural", "Petróleo", "Solar"],
        "Emisiones de CO₂ (kg/MWh)": [900, 450, 750, 50]
    })
    fig_co2 = px.bar(data_co2, x="Fuente de Energía", y="Emisiones de CO₂ (kg/MWh)",
                     title="💨 Comparación de Emisiones de CO₂ por Fuente de Energía",
                     color="Fuente de Energía", color_discrete_sequence=["#E74C3C", "#F39C12", "#3498DB", "#2ECC71"])
    st.plotly_chart(fig_co2)
    
    st.subheader("💰 Beneficios Económicos")
    st.write("- **Reducción en la factura eléctrica:** Disminuye la dependencia de la red pública.")
    st.write("- **Incentivos fiscales:** Muchos gobiernos ofrecen subsidios o créditos fiscales para instalaciones solares.")
    st.write("- **Incremento del valor de la propiedad:** Las viviendas con paneles solares suelen tener un mayor valor en el mercado inmobiliario.")
    
    # Comparación de ahorro anual con paneles solares
    data_ahorro = pd.DataFrame({
        "Año": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Ahorro Acumulado (USD)": [500, 1000, 1500, 2100, 2700, 3400, 4100, 4900, 5700, 6600]
    })
    fig_ahorro = px.line(data_ahorro, x="Año", y="Ahorro Acumulado (USD)",
                          title="💲 Ahorro Acumulado con Energía Solar", markers=True, color_discrete_sequence=['#2ECC71'])
    st.plotly_chart(fig_ahorro)
    
    st.subheader("⚡ Beneficios Sociales y Accesibilidad")
    st.write("- **Energía para comunidades remotas:** Permite electrificación en áreas sin acceso a la red eléctrica convencional.")
    st.write("- **Independencia energética:** Reduce la dependencia de combustibles fósiles importados.")
    st.write("- **Creación de empleo:** Impulsa la generación de nuevos empleos en la industria de energías renovables.")
    
    # Mapa de países con mayor adopción de energía solar
    data_paises = pd.DataFrame({
        "País": ["China", "Estados Unidos", "Alemania", "India", "Japón", "España", "Australia"],
        "Capacidad Solar (GW)": [306, 95, 58, 49, 68, 18, 27],
        "Latitud": [35.8617, 37.0902, 51.1657, 20.5937, 36.2048, 40.4637, -25.2744],
        "Longitud": [104.1954, -95.7129, 10.4515, 78.9629, 138.2529, -3.7492, 133.7751]
    })
    fig_paises = px.scatter_geo(
        data_paises, lat="Latitud", lon="Longitud", size="Capacidad Solar (GW)",
        hover_name="País", title="🌍 Países con Mayor Adopción de Energía Solar",
        color_discrete_sequence=["#F39C12"]
    )
    st.plotly_chart(fig_paises)
    
    st.subheader("📌 Conclusión")
    st.write(
        "La energía solar ofrece un amplio rango de beneficios, desde el ahorro económico hasta la reducción de emisiones contaminantes. "
        "Con el avance de la tecnología y el apoyo gubernamental, su adopción seguirá en crecimiento en los próximos años."
    )

# ============================
# Mantenimiento y Vida Útil
# ============================
if seleccion == "Mantenimiento y Vida Útil":
    st.header("🛠️ Mantenimiento y Vida Útil de los Paneles Solares")
    st.write(
        "Los paneles solares requieren un mantenimiento mínimo para garantizar su eficiencia y durabilidad. "
        "La limpieza regular y la inspección de conexiones eléctricas son clave para prolongar su vida útil."
    )
    
    st.subheader("🔍 Recomendaciones de Mantenimiento")
    st.write("- **Limpieza periódica:** Elimina polvo, hojas y suciedad para evitar obstrucciones en la captación de luz solar.")
    st.write("- **Inspección eléctrica:** Revisión de conexiones y cableado para prevenir fallas en el sistema.")
    st.write("- **Monitoreo de rendimiento:** Uso de software para verificar la eficiencia y detectar anomalías.")
    st.write("- **Protección contra sombras:** Evitar objetos que bloqueen la luz solar y afecten la producción de energía.")
    
    # Gráfico de impacto del mantenimiento en la eficiencia
    data_mantenimiento = pd.DataFrame({
        "Frecuencia de Mantenimiento": ["Sin Mantenimiento", "Cada 6 meses", "Cada 3 meses", "Mensual"],
        "Eficiencia del Panel (%)": [75, 85, 90, 98]
    })
    fig_mantenimiento = px.bar(
        data_mantenimiento, x="Frecuencia de Mantenimiento", y="Eficiencia del Panel (%)",
        title="🔧 Impacto del Mantenimiento en la Eficiencia de los Paneles",
        color="Frecuencia de Mantenimiento", color_discrete_sequence=["#E74C3C", "#F39C12", "#3498DB", "#2ECC71"]
    )
    st.plotly_chart(fig_mantenimiento)
    
    st.subheader("📆 Vida Útil de los Paneles Solares")
    st.write(
        "Los paneles solares tienen una vida útil promedio de **25 a 30 años**. Su rendimiento disminuye con el tiempo, "
        "pero continúan generando electricidad de manera efectiva con el mantenimiento adecuado."
    )
    
    # Gráfico de degradación del rendimiento con el tiempo
    data_vida_util = pd.DataFrame({
        "Años de Uso": [0, 5, 10, 15, 20, 25, 30],
        "Eficiencia (%)": [100, 95, 90, 85, 80, 75, 70]
    })
    fig_vida_util = px.line(
        data_vida_util, x="Años de Uso", y="Eficiencia (%)",
        title="📉 Degradación del Rendimiento de los Paneles con el Tiempo",
        markers=True, color_discrete_sequence=['#E67E22']
    )
    st.plotly_chart(fig_vida_util)
    
    st.subheader("🔗 Factores que Afectan la Vida Útil")
    st.write("Los siguientes factores pueden influir en la longevidad de un panel solar:")
    st.write("- **Condiciones climáticas extremas:** Granizo, nieve y vientos fuertes pueden afectar la estructura del panel.")
    st.write("- **Calidad de los materiales:** Paneles con materiales premium tienen mayor durabilidad.")
    st.write("- **Método de instalación:** Una instalación correcta evita daños y reduce la degradación prematura.")
    
    # Comparación de vida útil por tipo de panel
    data_tipos_panel = pd.DataFrame({
        "Tipo de Panel": ["Monocristalino", "Policristalino", "Película Delgada"],
        "Vida Útil (años)": [30, 25, 20]
    })
    fig_tipos_panel = px.bar(
        data_tipos_panel, x="Tipo de Panel", y="Vida Útil (años)",
        title="⏳ Comparación de Vida Útil por Tipo de Panel",
        color="Tipo de Panel", color_discrete_sequence=["#3498DB", "#F39C12", "#E74C3C"]
    )
    st.plotly_chart(fig_tipos_panel)
    
    st.subheader("📌 Conclusión")
    st.write(
        "Un mantenimiento adecuado puede extender la vida útil de los paneles solares y mejorar su eficiencia. "
        "Es importante realizar inspecciones periódicas y seguir las recomendaciones del fabricante para maximizar la inversión en energía solar."
    )

# ============================
# Impacto Económico y Políticas de Incentivos
# ============================
if seleccion == "Impacto Económico y Políticas de Incentivos":
    st.header("💰 Impacto Económico y Políticas de Incentivos")
    st.write(
        "La energía solar representa una inversión inicial significativa, pero proporciona ahorro a largo plazo en costos energéticos. "
        "Además, existen incentivos y subsidios gubernamentales que pueden reducir el costo inicial de instalación."
    )
    
    st.subheader("📈 Beneficios Económicos")
    st.write("- **Reducción de facturas eléctricas:** Disminuye la dependencia de la red pública y protege contra aumentos de tarifas.")
    st.write("- **Incremento del valor de la propiedad:** Viviendas con sistemas solares pueden venderse a precios más altos.")
    st.write("- **Menores costos operativos a largo plazo:** A diferencia de combustibles fósiles, la energía solar no tiene costos variables de suministro.")
    
    # Comparación de ahorro con energía solar
    data_ahorro_solar = pd.DataFrame({
        "Año": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Ahorro Acumulado (USD)": [500, 1000, 1500, 2100, 2700, 3400, 4100, 4900, 5700, 6600]
    })
    fig_ahorro_solar = px.line(
        data_ahorro_solar, x="Año", y="Ahorro Acumulado (USD)",
        title="💲 Ahorro Acumulado con Energía Solar", markers=True, color_discrete_sequence=['#2ECC71']
    )
    st.plotly_chart(fig_ahorro_solar)
    
    st.subheader("🏛️ Incentivos y Subsidios")
    st.write(
        "Muchos gobiernos y entidades ofrecen incentivos fiscales y subsidios para fomentar la adopción de la energía solar. "
        "Estos incentivos varían según el país y pueden incluir créditos fiscales, reducción de impuestos y tarifas preferenciales."
    )
    
    # Tabla de incentivos por país
    data_incentivos = pd.DataFrame({
        "País": ["EE.UU.", "España", "México", "Alemania", "Brasil"],
        "Subsidio Promedio (%)": [26, 30, 20, 35, 25],
        "Deducción Fiscal (%)": [22, 18, 15, 25, 20]
    })
    st.subheader("🌍 Comparación de Incentivos por País")
    st.table(data_incentivos)
    
    # Gráfico de incentivos por país
    fig_incentivos = px.bar(
        data_incentivos, x="País", y=["Subsidio Promedio (%)", "Deducción Fiscal (%)"],
        title="📊 Comparación de Subsidios y Deducciones Fiscales por País",
        barmode='group', color_discrete_sequence=["#3498DB", "#F39C12"]
    )
    st.plotly_chart(fig_incentivos)
    
    st.subheader("📊 Retorno de Inversión y Tiempo de Recuperación")
    st.write(
        "El retorno de inversión (ROI) y el tiempo de recuperación son métricas clave para evaluar la viabilidad económica de un sistema solar."
    )
    
    data_roi = pd.DataFrame({
        "Costo de Instalación (USD)": [5000, 10000, 15000, 20000, 25000],
        "ROI (%)": [40, 30, 25, 20, 18],
        "Tiempo de Recuperación (años)": [5, 7, 8, 10, 12]
    })
    
    fig_roi = px.scatter(
        data_roi, x="Costo de Instalación (USD)", y="ROI (%)",
        size="Tiempo de Recuperación (años)", color="Tiempo de Recuperación (años)",
        title="📉 Relación entre Costo de Instalación, ROI y Tiempo de Recuperación",
        color_continuous_scale="Bluered_r"
    )
    st.plotly_chart(fig_roi)
    
    st.subheader("📌 Conclusión")
    st.write(
        "La energía solar no solo representa una inversión en sustentabilidad, sino que también ofrece beneficios económicos significativos. "
        "Aprovechar los incentivos gubernamentales y calcular adecuadamente el retorno de inversión puede hacer que la adopción de esta tecnología sea aún más rentable."
    )
    
# ============================
# Instalación y Requerimientos Técnicos
# ============================
if seleccion == "Instalación y Requerimientos Técnicos":
    st.header("🏗️ Instalación y Requerimientos Técnicos")
    st.write(
        "La instalación de un sistema solar requiere planificación y consideración de múltiples factores técnicos. "
        "Desde la ubicación hasta la compatibilidad con la red eléctrica, cada aspecto es fundamental para garantizar eficiencia y seguridad."
    )
    
    st.subheader("📍 Factores Claves para la Instalación")
    st.write("- **Ubicación y orientación:** Idealmente, los paneles deben colocarse en dirección sur en el hemisferio norte y norte en el hemisferio sur.")
    st.write("- **Capacidad del sistema:** Debe dimensionarse según el consumo energético del hogar o empresa.")
    st.write("- **Requisitos eléctricos:** Es fundamental cumplir con normativas de seguridad y compatibilidad con la red eléctrica.")
    st.write("- **Inclinación de los paneles:** Un ángulo óptimo maximiza la absorción de la radiación solar.")
    
    # Comparación de eficiencia según inclinación
    data_inclinacion = pd.DataFrame({
        "Ángulo de Inclinación (°)": [0, 15, 30, 45, 60],
        "Eficiencia (%)": [50, 75, 90, 80, 60]
    })
    fig_inclinacion = px.line(
        data_inclinacion, x="Ángulo de Inclinación (°)", y="Eficiencia (%)",
        title="📈 Relación entre Inclinación del Panel y Eficiencia",
        markers=True, color_discrete_sequence=['#F39C12']
    )
    st.plotly_chart(fig_inclinacion)
    
    st.subheader("🔧 Componentes Esenciales para la Instalación")
    st.write("Los sistemas solares requieren diferentes componentes para su correcto funcionamiento:")
    st.write("- **Paneles solares:** Captan la energía solar y la convierten en electricidad.")
    st.write("- **Inversor solar:** Transforma la corriente continua en corriente alterna.")
    st.write("- **Baterías (opcional):** Almacenan energía para su uso nocturno o en días nublados.")
    st.write("- **Estructuras de montaje:** Aseguran la correcta orientación y estabilidad de los paneles.")
    st.write("- **Medidores bidireccionales:** Permiten la medición de energía exportada e importada de la red pública.")
    
    # Gráfico de distribución de costos de instalación
    data_costos = pd.DataFrame({
        "Componente": ["Paneles Solares", "Inversor", "Baterías", "Estructuras de Montaje", "Mano de Obra"],
        "Costo (%)": [50, 20, 15, 10, 5]
    })
    fig_costos = px.pie(
        data_costos, names="Componente", values="Costo (%)",
        title="💰 Distribución de Costos en la Instalación de un Sistema Solar",
        color_discrete_sequence=["#F39C12", "#3498DB", "#2ECC71", "#E74C3C", "#9B59B6"]
    )
    st.plotly_chart(fig_costos)
    
    st.subheader("⚡ Conexión a la Red y Normativas")
    st.write(
        "Dependiendo de la instalación, los sistemas solares pueden operar de manera independiente (off-grid) o estar conectados a la red pública (on-grid)."
    )
    st.write("- **Sistemas On-Grid:** Conectados a la red eléctrica, permiten vender el excedente de energía.")
    st.write("- **Sistemas Off-Grid:** Utilizan baterías para almacenar energía y funcionan de manera autónoma.")
    st.write("- **Normativas de seguridad:** La instalación debe cumplir con regulaciones locales sobre voltaje, sistemas de protección y compatibilidad."
    )
    
    # Comparación de tipos de sistemas solares
    data_sistemas = pd.DataFrame({
        "Tipo de Sistema": ["On-Grid", "Off-Grid"],
        "Costo de Instalación (USD)": [10000, 15000],
        "Ahorro Anual (USD)": [1200, 1000]
    })
    fig_sistemas = px.bar(
        data_sistemas, x="Tipo de Sistema", y=["Costo de Instalación (USD)", "Ahorro Anual (USD)"],
        title="⚖️ Comparación de Costos y Ahorros entre Sistemas On-Grid y Off-Grid",
        barmode='group', color_discrete_sequence=["#3498DB", "#2ECC71"]
    )
    st.plotly_chart(fig_sistemas)
    
    st.subheader("📌 Conclusión")
    st.write(
        "La correcta instalación de un sistema solar es clave para maximizar su eficiencia y garantizar la seguridad operativa. "
        "Considerar los factores técnicos, elegir los componentes adecuados y cumplir con las regulaciones permitirá una transición exitosa a la energía solar."
    )

# ============================
# Evolución Tecnológica de los Paneles Solares
# ============================
if seleccion == "Evolución Tecnológica de los Paneles Solares":
    st.header("🔬 Evolución Tecnológica de los Paneles Solares")
    st.write(
        "En las últimas décadas, la eficiencia de los paneles solares ha mejorado significativamente gracias a innovaciones tecnológicas. "
        "Desde nuevos materiales hasta sistemas inteligentes de gestión de energía, la evolución de esta tecnología ha permitido una mayor adopción a nivel mundial."
    )
    
    st.subheader("🚀 Avances en la Tecnología Solar")
    st.write("- **Celdas fotovoltaicas de tercera generación:** Uso de materiales como perovskitas para aumentar la eficiencia.")
    st.write("- **Paneles bifaciales:** Capturan luz en ambas caras para mayor generación energética.")
    st.write("- **Integración con baterías:** Permiten el almacenamiento de energía para uso nocturno o en días nublados.")
    st.write("- **Sistemas de seguimiento solar:** Paneles que ajustan su orientación automáticamente para captar más radiación.")
    st.write("- **Uso de inteligencia artificial:** Algoritmos optimizan el rendimiento de los paneles y predicen fallas.")
    
    # Comparación de eficiencia de diferentes generaciones de paneles solares
    data_evolucion = pd.DataFrame({
        "Generación": ["Primera (Silicio Cristalino)", "Segunda (Capa Fina)", "Tercera (Perovskita)"],
        "Eficiencia (%)": [18, 22, 30]
    })
    fig_evolucion = px.bar(
        data_evolucion, x="Generación", y="Eficiencia (%)",
        title="📈 Evolución de la Eficiencia en Paneles Solares",
        color="Generación", color_discrete_sequence=["#F39C12", "#3498DB", "#2ECC71"]
    )
    st.plotly_chart(fig_evolucion)
    
    st.subheader("⚙️ Materiales Innovadores")
    st.write("La búsqueda de nuevos materiales ha sido clave en el desarrollo de paneles solares más eficientes y accesibles.")
    st.write("- **Silicio cristalino:** Material tradicional con alta eficiencia y durabilidad.")
    st.write("- **Perovskita:** Promete mayor eficiencia y menor costo de producción.")
    st.write("- **Grafeno:** Material ultraligero con alta conductividad eléctrica para futuras aplicaciones solares.")
    
    # Gráfico de costos de fabricación por material
    data_materiales = pd.DataFrame({
        "Material": ["Silicio Cristalino", "Perovskita", "Grafeno"],
        "Costo de Producción (USD/m²)": [150, 100, 75]
    })
    fig_materiales = px.bar(
        data_materiales, x="Material", y="Costo de Producción (USD/m²)",
        title="💰 Comparación de Costos de Producción de Materiales Fotovoltaicos",
        color="Material", color_discrete_sequence=["#E74C3C", "#F39C12", "#3498DB"]
    )
    st.plotly_chart(fig_materiales)
    
    st.subheader("📊 Crecimiento Global de la Tecnología Solar")
    st.write("El avance tecnológico ha impulsado un crecimiento exponencial en la capacidad instalada de energía solar en el mundo.")
    
    data_crecimiento = pd.DataFrame({
        "Año": [2010, 2015, 2020, 2025],
        "Capacidad Global (GW)": [50, 230, 710, 1500]
    })
    fig_crecimiento = px.line(
        data_crecimiento, x="Año", y="Capacidad Global (GW)",
        title="🌍 Crecimiento Global de la Capacidad Solar Instalada",
        markers=True, color_discrete_sequence=['#2ECC71']
    )
    st.plotly_chart(fig_crecimiento)
    
    st.subheader("📌 Conclusión")
    st.write(
        "Los avances tecnológicos han permitido que la energía solar sea más eficiente, asequible y accesible. "
        "A medida que la investigación continúe, se espera que la eficiencia de los paneles solares aumente y los costos de producción disminuyan, facilitando su adopción a nivel global."
    )

# ============================
# Energía Solar en el Mundo
# ============================
if seleccion == "Energía Solar en el Mundo":
    st.header("🌍 Energía Solar en el Mundo")
    st.write(
        "La energía solar ha experimentado un crecimiento exponencial en la última década. "
        "Países como China, Estados Unidos y Alemania lideran en capacidad instalada. "
        "Este crecimiento se debe a la reducción de costos de producción, avances tecnológicos y políticas gubernamentales de apoyo."
    )
    
    st.subheader("🌞 Principales Países con Energía Solar")
    st.write(
        "Diferentes naciones han adoptado la energía solar con diversas estrategias, ya sea mediante plantas solares a gran escala o incentivos para instalaciones residenciales."
    )
    
    data_paises = pd.DataFrame({
        "País": ["China", "Estados Unidos", "Alemania", "India", "Japón", "España", "Australia"],
        "Capacidad Instalada (GW)": [306, 95, 58, 49, 68, 18, 27]
    })
    fig_paises = px.bar(
        data_paises, x="País", y="Capacidad Instalada (GW)",
        title="📊 Capacidad Solar Instalada por País",
        color="País", color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_paises)
    
    st.subheader("📈 Crecimiento de la Energía Solar en el Mundo")
    st.write(
        "El crecimiento de la energía solar ha sido acelerado en los últimos años, con una tasa de adopción que supera a la de muchas otras energías renovables."
    )
    
    data_crecimiento = pd.DataFrame({
        "Año": [2010, 2015, 2020, 2025],
        "Capacidad Global (GW)": [50, 230, 710, 1500]
    })
    fig_crecimiento = px.line(
        data_crecimiento, x="Año", y="Capacidad Global (GW)",
        title="📈 Crecimiento Global de la Capacidad Solar Instalada",
        markers=True, color_discrete_sequence=['#2ECC71']
    )
    st.plotly_chart(fig_crecimiento)
    
    st.subheader("🗺️ Distribución Global de la Energía Solar")
    st.write("El siguiente mapa muestra la distribución de la capacidad solar instalada en diferentes países.")
    
    data_mapa = pd.DataFrame({
        "País": ["China", "Estados Unidos", "Alemania", "India", "Japón", "España", "Australia"],
        "Capacidad (GW)": [306, 95, 58, 49, 68, 18, 27],
        "Latitud": [35.8617, 37.0902, 51.1657, 20.5937, 36.2048, 40.4637, -25.2744],
        "Longitud": [104.1954, -95.7129, 10.4515, 78.9629, 138.2529, -3.7492, 133.7751]
    })
    
    fig_mapa = px.scatter_geo(
        data_mapa, lat="Latitud", lon="Longitud", size="Capacidad (GW)",
        hover_name="País", title="🌍 Mapa de Capacidad Solar Instalada por País",
        color_discrete_sequence=["#F39C12"]
    )
    st.plotly_chart(fig_mapa)
    
    st.subheader("📌 Conclusión")
    st.write(
        "El crecimiento de la energía solar a nivel global es una señal clara de la transición hacia fuentes de energía renovable. "
        "Con más países invirtiendo en infraestructura solar y reduciendo costos de implementación, se espera que esta tendencia continúe en los próximos años."
    )

# ============================
# Comparación con Otras Energías Renovables
# ============================
if seleccion == "Comparación con Otras Energías Renovables":
    st.header("⚡ Comparación con Otras Energías Renovables")
    st.write(
        "La energía solar es una de las fuentes renovables más utilizadas en el mundo, pero existen otras fuentes de energía "
        "como la eólica, hidroeléctrica y geotérmica, cada una con sus propias ventajas y desafíos."
    )
    
    st.subheader("📊 Comparación de Costos de Generación")
    data_costos = pd.DataFrame({
        "Energía": ["Solar", "Eólica", "Hidroeléctrica", "Geotérmica"],
        "Costo (USD/MWh)": [40, 30, 50, 60]
    })
    fig_costos = px.bar(
        data_costos, x="Energía", y="Costo (USD/MWh)",
        title="💰 Comparación de Costos de Generación de Energías Renovables",
        color="Energía", color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_costos)
    
    st.subheader("📈 Eficiencia y Factores de Capacidad")
    st.write(
        "El factor de capacidad mide cuánto de la capacidad instalada de una fuente de energía se utiliza realmente a lo largo del tiempo."
    )
    data_factor = pd.DataFrame({
        "Energía": ["Solar", "Eólica", "Hidroeléctrica", "Geotérmica"],
        "Factor de Capacidad (%)": [20, 35, 50, 70]
    })
    fig_factor = px.bar(
        data_factor, x="Energía", y="Factor de Capacidad (%)",
        title="⚙️ Comparación de Factores de Capacidad",
        color="Energía", color_discrete_sequence=px.colors.qualitative.Prism
    )
    st.plotly_chart(fig_factor)
    
    st.subheader("🌱 Impacto Ambiental")
    st.write("Diferentes fuentes de energía renovable tienen distintos impactos ambientales.")
    data_impacto = pd.DataFrame({
        "Energía": ["Solar", "Eólica", "Hidroeléctrica", "Geotérmica"],
        "Emisiones CO₂ (kg/MWh)": [0, 0, 10, 5]
    })
    fig_impacto = px.bar(
        data_impacto, x="Energía", y="Emisiones CO₂ (kg/MWh)",
        title="🌍 Comparación de Emisiones de CO₂ por Energía Renovable",
        color="Energía", color_discrete_sequence=px.colors.qualitative.Dark2
    )
    st.plotly_chart(fig_impacto)
    
    st.subheader("📌 Conclusión")
    st.write(
        "Cada fuente de energía renovable tiene características particulares que la hacen adecuada para diferentes entornos. "
        "Mientras que la energía solar es accesible y de bajo mantenimiento, la energía eólica puede ser más eficiente en ciertas regiones. "
        "La hidroeléctrica y la geotérmica tienen factores de capacidad elevados, pero pueden tener impactos ambientales significativos."
    )

# ============================
# Factores que Afectan el Rendimiento
# ============================
if seleccion == "Factores que Afectan el Rendimiento":
    st.header("📉 Factores que Afectan el Rendimiento de los Paneles Solares")
    st.write(
        "El rendimiento de los paneles solares está influenciado por varios factores ambientales y técnicos. "
        "Comprender estos factores ayuda a maximizar la eficiencia del sistema solar."
    )
    
    st.subheader("🌞 Principales Factores que Reducen la Eficiencia")
    st.write("- **Inclinación incorrecta:** Una mala orientación puede reducir la captación de radiación solar.")
    st.write("- **Temperaturas extremas:** El calor excesivo puede disminuir la eficiencia del panel.")
    st.write("- **Sombras parciales:** Árboles, edificios y objetos pueden bloquear la luz solar.")
    st.write("- **Suciedad y polvo:** La acumulación de suciedad reduce la capacidad de absorción de la luz.")
    st.write("- **Ubicación geográfica:** Las horas solares pico varían según la latitud del sistema."
    )
    
    data_factores = pd.DataFrame({
        "Factor": ["Inclinación", "Temperatura", "Sombras", "Suciedad", "Ubicación"],
        "Impacto (%)": [30, 20, 25, 15, 10]
    })
    fig_factores = px.pie(
        data_factores, names="Factor", values="Impacto (%)",
        title="📉 Factores que Reducen el Rendimiento de los Paneles Solares",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_factores)
    
    st.subheader("🔍 Mitigación de los Factores Negativos")
    st.write("Para maximizar el rendimiento de los paneles solares, se pueden tomar las siguientes medidas:")
    st.write("- **Ajustar la inclinación y orientación de los paneles según la ubicación.")
    st.write("- **Mantener los paneles limpios y libres de suciedad o polvo.")
    st.write("- **Evitar la instalación en zonas con sombras constantes.")
    st.write("- **Utilizar sistemas de refrigeración pasiva en climas extremadamente cálidos.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "Los factores ambientales y de instalación juegan un papel clave en la eficiencia de los paneles solares. "
        "Con una instalación adecuada y un mantenimiento regular, se pueden minimizar las pérdidas y maximizar la producción de energía."
    )

# ============================
# Almacenamiento de Energía Solar
# ============================
if seleccion == "Almacenamiento de Energía Solar":
    st.header("🔋 Almacenamiento de Energía Solar")
    st.write(
        "El almacenamiento de energía solar es clave para su uso en momentos sin luz solar, "
        "permitiendo el suministro continuo de electricidad en hogares y empresas. "
        "Las baterías solares han evolucionado para ofrecer mayor eficiencia, vida útil y rentabilidad."
    )
    
    st.subheader("🔋 Tipos de Baterías para Almacenamiento de Energía Solar")
    st.write("Existen varios tipos de baterías utilizadas en sistemas solares, cada una con ventajas y desventajas:")
    st.write("- **Baterías de Ion-Litio:** Alta eficiencia, mayor vida útil y carga rápida.")
    st.write("- **Baterías de Plomo-Ácido:** Económicas, pero con menor durabilidad y eficiencia.")
    st.write("- **Baterías de Flujo Redox:** Mayor vida útil y capacidad de almacenamiento, pero alto costo inicial.")
    
    # Comparación de durabilidad y costo de diferentes baterías
    data_baterias = pd.DataFrame({
        "Tipo de Batería": ["Ion-Litio", "Plomo-Ácido", "Flujo Redox"],
        "Durabilidad (años)": [15, 5, 20],
        "Costo (USD/kWh)": [150, 100, 300]
    })
    fig_baterias = px.bar(
        data_baterias, x="Tipo de Batería", y=["Durabilidad (años)", "Costo (USD/kWh)"],
        title="📊 Comparación de Tipos de Baterías para Almacenamiento Solar",
        barmode='group', color_discrete_sequence=["#2ECC71", "#E74C3C"]
    )
    st.plotly_chart(fig_baterias)
    
    st.subheader("⚙️ Factores Claves en la Elección de una Batería Solar")
    st.write("Para seleccionar una batería adecuada, se deben considerar los siguientes aspectos:")
    st.write("- **Capacidad de almacenamiento:** Cantidad de energía que la batería puede retener y suministrar.")
    st.write("- **Eficiencia de carga/descarga:** Indica cuánta energía almacenada se puede recuperar.")
    st.write("- **Ciclo de vida útil:** Número de ciclos de carga y descarga antes de perder eficiencia.")
    st.write("- **Mantenimiento y costos operativos:** Algunas baterías requieren más mantenimiento que otras.")
    
    # Comparación de eficiencia de carga y descarga de baterías
    data_eficiencia = pd.DataFrame({
        "Tipo de Batería": ["Ion-Litio", "Plomo-Ácido", "Flujo Redox"],
        "Eficiencia de Carga/Descarga (%)": [95, 80, 85]
    })
    fig_eficiencia = px.bar(
        data_eficiencia, x="Tipo de Batería", y="Eficiencia de Carga/Descarga (%)",
        title="⚡ Eficiencia de Carga y Descarga por Tipo de Batería",
        color="Tipo de Batería", color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_eficiencia)
    
    st.subheader("🔌 Integración de Almacenamiento en Sistemas Solares")
    st.write(
        "El almacenamiento de energía se puede integrar en sistemas solares de distintas formas:"
        "\n- **Sistemas Off-Grid:** Utilizan baterías para operar sin conexión a la red eléctrica."
        "\n- **Sistemas Híbridos:** Combinan almacenamiento con conexión a la red pública para optimizar el consumo."
        "\n- **Sistemas On-Grid con respaldo:** Almacenan energía para emergencias mientras siguen conectados a la red."
    )
    
    st.subheader("📌 Conclusión")
    st.write(
        "El almacenamiento de energía solar es fundamental para garantizar el suministro continuo y aprovechar al máximo la energía generada. "
        "Las baterías han evolucionado en eficiencia y accesibilidad, facilitando la adopción de sistemas solares independientes y sostenibles."
    )

# ============================
# Normativas y Regulaciones
# ============================
if seleccion == "Normativas y Regulaciones":
    st.header("📜 Normativas y Regulaciones")
    st.write(
        "Las normativas en energía solar varían por país y región, regulando la instalación, "
        "interconexión a la red, incentivos fiscales y estándares de seguridad. "
        "Comprender estas regulaciones es crucial para garantizar una instalación legal y eficiente, así como "
        "para maximizar los beneficios económicos y ambientales."
    )
    
    st.subheader("📋 Principales Ámbitos de Regulación")
    st.write("Las normativas suelen abarcar los siguientes aspectos clave:")
    st.write("- **Interconexión a la red:** Normas que regulan cómo los sistemas solares pueden conectarse a la red eléctrica pública.")
    st.write("- **Medición Neta:** Permite a los propietarios de paneles solares vender el exceso de energía a la red, generando ahorros adicionales.")
    st.write("- **Subsidios y créditos fiscales:** Incentivos que buscan reducir el costo inicial de la instalación de paneles solares.")
    st.write("- **Normas de seguridad:** Regulaciones sobre materiales, instalación, mantenimiento y protocolos de seguridad eléctrica.")
    st.write("- **Regulación ambiental:** Requisitos sobre el reciclaje y disposición final de paneles solares para evitar impactos negativos en el medio ambiente.")
    
    st.subheader("🌍 Ejemplo de Regulaciones en Diferentes Países")
    data_regulaciones = pd.DataFrame({
        "País": ["Estados Unidos", "Unión Europea", "China", "México", "Brasil"],
        "Regulación Clave": [
            "Incentivos fiscales y medición neta",
            "Objetivos de energía renovable y reducción de emisiones",
            "Subsidios a la producción de paneles solares y expansión de la industria",
            "Tarifas de interconexión y financiamiento gubernamental",
            "Programas de energía distribuida y créditos fiscales"
        ]
    })
    fig_regulaciones = px.bar(
        data_regulaciones, x="País", y="Regulación Clave",
        title="🌎 Principales Regulaciones de Energía Solar por País",
        color="País", color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig_regulaciones)
    
    st.subheader("📜 Regulaciones en Crecimiento y Nuevas Tendencias")
    st.write("En los últimos años, diversas tendencias han emergido en la regulación de la energía solar:")
    st.write("- **Obligatoriedad de paneles solares en nuevas construcciones en algunos países y ciudades.")
    st.write("- **Mayor regulación sobre la disposición y reciclaje de paneles solares al final de su vida útil.")
    st.write("- **Expansión de incentivos financieros para empresas y hogares que invierten en energía renovable.")
    st.write("- **Integración de redes inteligentes que permitan una mejor distribución de la energía solar generada.")
    
    st.subheader("⚖️ Importancia de Cumplir con las Regulaciones")
    st.write("El cumplimiento de normativas garantiza que los sistemas solares sean seguros, eficientes y económicamente viables.")
    st.write("- **Protección del consumidor:** Evita fraudes y garantiza la calidad del sistema instalado.")
    st.write("- **Acceso a incentivos:** Cumplir con las regulaciones permite aprovechar beneficios fiscales y subsidios, reduciendo el tiempo de retorno de la inversión.")
    st.write("- **Seguridad operativa:** Minimiza riesgos eléctricos, estructurales y ambientales en la instalación y operación de paneles solares.")
    st.write("- **Desarrollo sostenible:** Asegura que la expansión de la energía solar se realice de manera equilibrada y respetuosa con el medio ambiente.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "Las normativas y regulaciones en energía solar son fundamentales para el desarrollo del sector y la adopción masiva de esta tecnología. "
        "Cada país adapta sus leyes para promover el uso de energías renovables, garantizar instalaciones seguras y brindar incentivos económicos. "
        "A medida que la energía solar continúe creciendo, las regulaciones seguirán evolucionando para mejorar la eficiencia y accesibilidad de estos sistemas."
    )

# ============================
# Casos de Éxito y Proyectos Destacados
# ============================
if seleccion == "Casos de Éxito y Proyectos Destacados":
    st.header("🏆 Casos de Éxito y Proyectos Destacados")
    st.write(
        "Grandes proyectos han demostrado la viabilidad y escalabilidad de la energía solar, "
        "permitiendo el suministro de electricidad limpia y reduciendo la dependencia de combustibles fósiles. "
        "Estos casos de éxito han servido como modelos para futuras inversiones en energía renovable, "
        "destacando su impacto ambiental, económico y social."
    )
    
    st.subheader("🌞 Principales Proyectos Solares en el Mundo")
    proyectos = ["Parque Solar Tengger (China)", "Planta Solar Noor (Marruecos)", "Proyecto Solar en Australia", "Bhadla Solar Park (India)", "Topaz Solar Farm (EE.UU.)"]
    capacidad = [1547, 580, 3300, 2245, 550]
    data_proyectos = pd.DataFrame({"Proyecto": proyectos, "Capacidad (MW)": capacidad})
    
    fig_proyectos = px.bar(
        data_proyectos, x="Proyecto", y="Capacidad (MW)",
        title="🌍 Capacidad de Proyectos Solares Destacados",
        color="Proyecto", color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_proyectos)
    
    st.subheader("🔑 Factores Clave para el Éxito de los Proyectos Solares")
    st.write("Los proyectos más exitosos comparten ciertas características que los han convertido en referentes de la energía solar:")
    st.write("- **Ubicación estratégica:** Se encuentran en regiones con alta radiación solar anual, maximizando la producción de energía.")
    st.write("- **Infraestructura avanzada:** Utilizan tecnologías modernas como paneles bifaciales y sistemas de seguimiento solar para optimizar la eficiencia.")
    st.write("- **Inversión y financiamiento:** Reciben apoyo de gobiernos, inversionistas y organismos internacionales que garantizan su viabilidad.")
    st.write("- **Escalabilidad:** Han sido diseñados para expandirse conforme aumenta la demanda energética, permitiendo la adaptación a nuevas necesidades.")
    st.write("- **Sostenibilidad ambiental:** Implementan medidas para reducir su impacto ecológico, como el uso eficiente del suelo y programas de reciclaje de paneles.")
    
    st.subheader("📊 Comparación de Producción de Energía entre Proyectos")
    data_produccion = pd.DataFrame({
        "Proyecto": ["Tengger", "Noor", "Australia", "Bhadla", "Topaz"],
        "Producción Anual (GWh)": [3500, 1600, 5000, 4500, 1300]
    })
    fig_produccion = px.bar(
        data_produccion, x="Proyecto", y="Producción Anual (GWh)",
        title="⚡ Producción Anual de Energía de Proyectos Solares",
        color="Proyecto", color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_produccion)
    
    st.subheader("🌱 Impacto Ambiental y Social")
    st.write("Los proyectos solares no solo contribuyen a la reducción de emisiones de CO₂, sino que también generan empleo y desarrollo en las regiones donde se implementan:")
    st.write("- **Reducción de emisiones:** Se estima que estos proyectos evitan la emisión de millones de toneladas de CO₂ al año.")
    st.write("- **Creación de empleo:** La construcción y mantenimiento de estas plantas generan miles de empleos directos e indirectos.")
    st.write("- **Desarrollo rural:** En muchos casos, las instalaciones solares han mejorado la infraestructura y calidad de vida en comunidades cercanas.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "Los proyectos solares a gran escala han transformado la industria energética, demostrando que la energía solar es una opción confiable y sostenible. "
        "A medida que la tecnología avanza y los costos de instalación disminuyen, se espera que más países inviertan en proyectos solares de gran envergadura. "
        "Estos desarrollos no solo benefician al medio ambiente, sino que también impulsan la economía y mejoran la calidad de vida de muchas comunidades."
    )

# ============================
# Eficiencia de Inversión en Paneles Solares
# ============================
if seleccion == "Eficiencia de Inversión en Paneles Solares":
    st.header("💰 Eficiencia de Inversión en Paneles Solares")
    st.write(
        "El retorno de inversión (ROI) de los paneles solares depende del costo inicial, "
        "los ahorros en electricidad, los incentivos fiscales y la vida útil del sistema. "
        "Un análisis adecuado de estos factores permite determinar la rentabilidad de la inversión."
    )
    
    st.subheader("📊 Factores Clave que Afectan la Inversión")
    st.write("Para evaluar la eficiencia de la inversión en paneles solares, se deben considerar los siguientes aspectos:")
    st.write("- **Costo de instalación:** Incluye paneles, inversores, baterías y mano de obra.")
    st.write("- **Ahorro en electricidad:** Se calcula con base en el consumo reducido y el precio de la electricidad en la región.")
    st.write("- **Incentivos y subsidios:** Existen programas gubernamentales que disminuyen el costo inicial.")
    st.write("- **Durabilidad del sistema:** Los paneles solares tienen una vida útil de 25 a 30 años, con mínimos costos de mantenimiento.")
    
    # Comparación de costos y ahorro
    data_inversion = pd.DataFrame({
        "Factor": ["Costo Inicial (USD)", "Ahorro Anual (USD)", "Retorno de Inversión (años)"],
        "Valor": [10000, 1200, 8.3]
    })
    fig_inversion = px.bar(
        data_inversion, x="Factor", y="Valor",
        title="📈 Eficiencia de Inversión en Paneles Solares",
        color="Factor", color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_inversion)
    
    st.subheader("📉 Comparación del Costo de Energía con y sin Paneles Solares")
    data_costos = pd.DataFrame({
        "Año": list(range(1, 21)),
        "Costo sin Paneles (USD)": np.linspace(1200, 30000, 20),
        "Costo con Paneles (USD)": np.concatenate(([10000], np.linspace(10800, 15000, 19)))
    })
    fig_costos = px.line(
        data_costos, x="Año", y=["Costo sin Paneles (USD)", "Costo con Paneles (USD)"],
        title="⚖️ Comparación del Costo Energético con y sin Paneles Solares",
        color_discrete_map={"Costo sin Paneles (USD)": "#E74C3C", "Costo con Paneles (USD)": "#2ECC71"}
    )
    st.plotly_chart(fig_costos)
    
    st.subheader("📌 Conclusión")
    st.write(
        "Invertir en paneles solares es una estrategia rentable a largo plazo. "
        "Si bien la inversión inicial puede parecer alta, los ahorros anuales en electricidad y los incentivos fiscales reducen significativamente el tiempo de recuperación. "
        "A medida que los costos de la energía convencional aumentan, la adopción de sistemas solares se convierte en una decisión financiera inteligente y sustentable."
    )

# ============================
# Impacto de las Condiciones Climáticas en el Rendimiento
# ============================
if seleccion == "Impacto de las Condiciones Climáticas en el Rendimiento":
    st.header("🌦️ Impacto de las Condiciones Climáticas en el Rendimiento")
    st.write(
        "Las condiciones climáticas juegan un papel crucial en la eficiencia de los paneles solares. "
        "Factores como la nubosidad, la temperatura y la acumulación de nieve pueden reducir significativamente "
        "la cantidad de energía generada por los sistemas fotovoltaicos."
    )
    
    st.subheader("📊 Factores Climáticos que Afectan la Producción de Energía")
    st.write("Diferentes condiciones meteorológicas pueden impactar de diversas maneras el rendimiento de los paneles solares:")
    st.write("- **Días Soleados:** Condición óptima para la máxima generación de energía.")
    st.write("- **Cielos Nublados:** Reducen la radiación solar y la eficiencia de los paneles hasta en un 20%.")
    st.write("- **Lluvia:** Aunque limpia los paneles de suciedad, la cantidad de luz solar captada disminuye hasta un 40%.")
    st.write("- **Nieve y Hielo:** La acumulación de nieve puede reducir la eficiencia en un 60% si los paneles no se mantienen despejados.")
    
    data_clima = pd.DataFrame({
        "Condición Climática": ["Días Soleados", "Nublado", "Lluvia", "Nieve"],
        "Eficiencia Reducida (%)": [0, 20, 40, 60]
    })
    fig_clima = px.bar(
        data_clima, x="Condición Climática", y="Eficiencia Reducida (%)",
        title="📉 Impacto Climático en la Eficiencia Solar",
        color="Condición Climática", color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_clima)
    
    st.subheader("🌡️ Influencia de la Temperatura en el Rendimiento Solar")
    st.write(
        "Aunque los paneles solares dependen del sol para generar energía, temperaturas extremadamente altas "
        "pueden reducir su eficiencia. La mayoría de los paneles pierden rendimiento cuando la temperatura "
        "supera los 25°C (77°F), con una reducción de eficiencia aproximada del 0.5% por cada grado adicional."
    )
    
    data_temp = pd.DataFrame({
        "Temperatura (°C)": [10, 20, 30, 40, 50],
        "Pérdida de Eficiencia (%)": [0, 2, 5, 10, 15]
    })
    fig_temp = px.line(
        data_temp, x="Temperatura (°C)", y="Pérdida de Eficiencia (%)",
        title="🌡️ Efecto de la Temperatura en la Eficiencia de los Paneles Solares",
        markers=True, color_discrete_sequence=['#E74C3C']
    )
    st.plotly_chart(fig_temp)
    
    st.subheader("💡 Estrategias para Mitigar el Impacto Climático")
    st.write("Para reducir los efectos negativos del clima en los paneles solares, se pueden aplicar las siguientes estrategias:")
    st.write("- **Mantenimiento regular:** Limpiar los paneles para evitar acumulación de nieve, polvo o suciedad.")
    st.write("- **Optimización de inclinación:** Ajustar la orientación de los paneles para minimizar el impacto de sombras y nieve.")
    st.write("- **Uso de paneles bifaciales:** Capturan luz reflejada, mejorando el rendimiento en condiciones de nubosidad o nieve.")
    st.write("- **Sistemas de enfriamiento:** Implementar soluciones como ventilación pasiva o materiales de alta disipación térmica.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "Si bien las condiciones climáticas pueden afectar el rendimiento de los paneles solares, "
        "la implementación de tecnologías avanzadas y un adecuado mantenimiento permiten minimizar estos efectos. "
        "Con la correcta planificación, la energía solar sigue siendo una opción confiable y eficiente en diversas condiciones ambientales."
    )

# ============================
# Diseño e Instalación de un Sistema Solar Residencial
# ============================
if seleccion == "Diseño e Instalación de un Sistema Solar Residencial":
    st.header("🏠 Diseño e Instalación de un Sistema Solar Residencial")
    st.write(
        "El diseño e instalación de un sistema solar requiere una planificación detallada para maximizar la eficiencia y minimizar los costos. "
        "Desde la evaluación del consumo energético hasta la instalación final, cada paso es crucial para el éxito del sistema."
    )
    
    st.subheader("🛠️ Pasos Clave en el Diseño e Instalación")
    st.write("1. **Evaluación del Consumo Energético:** Analizar el historial de consumo eléctrico del hogar para determinar la capacidad necesaria.")
    st.write("2. **Selección del Tipo de Panel Solar:** Escoger entre paneles monocristalinos, policristalinos o de película delgada según el presupuesto y espacio disponible.")
    st.write("3. **Determinación de la Mejor Orientación e Inclinación:** Ajustar los paneles para optimizar la captación de luz solar según la ubicación geográfica.")
    st.write("4. **Instalación del Inversor y Conexión a la Red:** Configurar el inversor y establecer la interconexión con la red eléctrica o baterías de respaldo.")
    st.write("5. **Inspección y Mantenimiento:** Realizar pruebas de rendimiento y establecer un plan de mantenimiento periódico.")
    
    st.subheader("📊 Comparación de Costos y Ahorros en Sistemas Solares Residenciales")
    data_costos = pd.DataFrame({
        "Capacidad del Sistema (kW)": [3, 5, 7, 10],
        "Costo de Instalación (USD)": [6000, 9000, 12000, 16000],
        "Ahorro Anual (USD)": [700, 1100, 1500, 2200]
    })
    fig_costos = px.bar(
        data_costos, x="Capacidad del Sistema (kW)", 
        y=["Costo de Instalación (USD)", "Ahorro Anual (USD)"],
        title="💰 Comparación de Costos y Ahorros en Sistemas Solares Residenciales",
        barmode='group', color_discrete_sequence=["#E74C3C", "#2ECC71"]
    )
    st.plotly_chart(fig_costos)
    
    st.subheader("⚡ Beneficios de un Sistema Solar Residencial")
    st.write("- **Reducción en la factura eléctrica:** Disminuye la dependencia de la red y los costos de electricidad a largo plazo.")
    st.write("- **Sostenibilidad ambiental:** Contribuye a la reducción de emisiones de CO₂ y al uso de energía limpia.")
    st.write("- **Incremento en el valor de la propiedad:** Inmuebles con sistemas solares tienen mayor atractivo en el mercado inmobiliario.")
    st.write("- **Independencia energética:** Posibilidad de almacenar energía con baterías para evitar apagones o cortes de suministro.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "La instalación de un sistema solar residencial es una inversión rentable y ecológica. "
        "Con una correcta planificación, los beneficios económicos y ambientales superan ampliamente los costos iniciales, "
        "haciendo de la energía solar una opción accesible y sustentable para los hogares modernos."
    )

# ============================
# Tendencias Futuras en Energía Solar
# ============================
if seleccion == "Tendencias Futuras en Energía Solar":
    st.header("🚀 Tendencias Futuras en Energía Solar")
    st.write(
        "La innovación en energía solar está en constante evolución, con nuevas tecnologías que mejoran la eficiencia, "
        "accesibilidad y sostenibilidad de estos sistemas. Los avances actuales prometen reducir costos y aumentar "
        "la adopción de esta fuente renovable en los próximos años."
    )
    
    st.subheader("🔬 Nuevas Tecnologías en Energía Solar")
    st.write("Las siguientes innovaciones están revolucionando el sector solar:")
    st.write("- **Paneles solares bifaciales:** Capturan luz en ambas caras, aumentando la generación de electricidad hasta un 20%.")
    st.write("- **Células fotovoltaicas de perovskita:** Material de bajo costo y alta eficiencia, con potencial para superar el silicio tradicional.")
    st.write("- **Almacenamiento en baterías de estado sólido:** Mayor durabilidad y seguridad en comparación con baterías de ion-litio.")
    st.write("- **Tecnología fotovoltaica integrada en edificios (BIPV):** Paneles solares que se integran en ventanas y fachadas.")
    st.write("- **Seguimiento solar inteligente:** Sistemas que ajustan automáticamente la inclinación de los paneles para optimizar la captación de luz.")
    
    # Comparación de eficiencia de tecnologías futuras
    data_tecnologia = pd.DataFrame({
        "Tecnología": ["Silicio Tradicional", "Perovskita", "Bifacial", "BIPV"],
        "Eficiencia (%)": [22, 30, 28, 25]
    })
    fig_tecnologia = px.bar(
        data_tecnologia, x="Tecnología", y="Eficiencia (%)",
        title="📈 Comparación de Eficiencia de Nuevas Tecnologías Solares",
        color="Tecnología", color_discrete_sequence=px.colors.qualitative.Prism
    )
    st.plotly_chart(fig_tecnologia)
    
    st.subheader("🌍 Expansión y Aplicaciones Futuras")
    st.write("Las tendencias futuras en energía solar no solo se limitan a la tecnología, sino también a su adopción en diferentes sectores:")
    st.write("- **Plantas solares flotantes:** Instalaciones en lagos y océanos que aprovechan el espacio sin afectar terrenos agrícolas.")
    st.write("- **Electrificación rural con energía solar:** Proyectos que llevan electricidad a comunidades aisladas.")
    st.write("- **Movilidad solar:** Uso de paneles solares en automóviles, trenes y aviones para reducir la dependencia de combustibles fósiles.")
    st.write("- **Producción de hidrógeno verde:** Utilización de energía solar para generar hidrógeno como fuente de energía limpia y almacenable.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "Las tendencias futuras en energía solar apuntan a una mayor eficiencia, reducción de costos y expansión global. "
        "A medida que la tecnología avanza, la energía solar se convertirá en una fuente primaria de electricidad, "
        "permitiendo un futuro más sostenible y accesible para todos."
    )
    
# ============================
# Integración de la Energía Solar con la Red Eléctrica
# ============================
if seleccion == "Integración de la Energía Solar con la Red Eléctrica":
    st.header("🔌 Integración de la Energía Solar con la Red Eléctrica")
    st.write(
        "La integración de la energía solar con la red eléctrica permite maximizar el aprovechamiento de la energía generada, "
        "reduciendo costos y asegurando un suministro constante de electricidad. Dependiendo del tipo de conexión, "
        "los usuarios pueden beneficiarse de diferentes esquemas de consumo y compensación."
    )
    
    st.subheader("📡 Modelos de Integración con la Red Eléctrica")
    st.write("Los sistemas solares pueden integrarse con la red eléctrica de varias maneras:")
    st.write("- **Autoconsumo con baterías:** La energía generada se almacena para su uso posterior, reduciendo la dependencia de la red pública.")
    st.write("- **Medición neta:** La electricidad sobrante se envía a la red y se reciben créditos en la factura eléctrica.")
    st.write("- **Sistemas híbridos:** Combinan energía solar con otras fuentes, como la eólica o la red convencional, asegurando mayor estabilidad. ")
    
    # Comparación de eficiencia de modelos de integración
    data_integracion = pd.DataFrame({
        "Modelo": ["Autoconsumo con Baterías", "Medición Neta", "Sistema Híbrido"],
        "Ahorro Estimado (%)": [50, 70, 85]
    })
    fig_integracion = px.bar(
        data_integracion, x="Modelo", y="Ahorro Estimado (%)",
        title="📊 Comparación de Modelos de Integración con la Red Eléctrica",
        color="Modelo", color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig_integracion)
    
    st.subheader("⚡ Beneficios de la Integración con la Red")
    st.write("- **Optimización del consumo:** Se aprovecha mejor la energía generada, evitando desperdicios.")
    st.write("- **Reducción de costos:** Los usuarios pueden generar ahorros significativos en su factura de electricidad.")
    st.write("- **Estabilidad energética:** Se evita la intermitencia en el suministro eléctrico, especialmente con sistemas híbridos.")
    st.write("- **Mayor accesibilidad:** Facilita la adopción de energía solar sin necesidad de baterías costosas en algunos casos.")
    
    st.subheader("📌 Conclusión")
    st.write(
        "La integración de la energía solar con la red eléctrica es una estrategia efectiva para maximizar sus beneficios económicos y operativos. "
        "Los diferentes modelos de conexión permiten adaptarse a las necesidades del usuario, garantizando un uso eficiente y sostenible de la energía renovable."
    )

# ============================
# Conclusión y Pie de Página
# ============================
st.markdown("---")
st.write("_Monitoreo de paneles solares © 2024_", unsafe_allow_html=True)
