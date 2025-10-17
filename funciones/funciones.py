import plotly.express as px
import pandas as pd
def grafico_barras_categoricas(data, columna, x_titulo = "eje x", y_titulo = "ejey", titulo="Distribución de Datos"):
    """
    Genera un gráfico de barras con Plotly para una variable categórica.

    Parámetros:
    - data: DataFrame de pandas con los datos.
    - columna: Nombre de la columna categórica a analizar.
    - titulo: Título del gráfico (opcional).
    
    Retorna:
    - Gráfico de barras en Plotly.
    """
    # Contar valores únicos de la columna
    conteo = data[columna].value_counts().reset_index()
    conteo.columns = [columna, 'Frecuencia']

    # Crear gráfico de barras
    fig = px.bar(conteo, 
                 x=columna, 
                 y='Frecuencia',
                 title=titulo,
                 labels={'Frecuencia': 'Cantidad de Casos', columna: 'Categoría'},
                 color_discrete_sequence=["#c71585"])  # Tonalidad rosa

    # Ajustar diseño
    fig.update_layout(template="plotly_white", 
                      xaxis_title=x_titulo, 
                      yaxis_title=y_titulo, 
                      plot_bgcolor='white', 
                      paper_bgcolor='white',
                      font=dict(family='Bahnschrift', size=14, color='black'),
                      title_font=dict(family='Bahnschrift', size=22, color='black'),
                      yaxis=dict(range=[0, conteo["Frecuencia"].max() + 5000]))  # Ajuste de rango

    # Evitar notación científica en el eje Y
    fig.update_yaxes(tickformat=",")

    # Mostrar valores sobre las barras
    fig.update_traces(texttemplate='%{y}', textposition='outside')

    # Mostrar gráfico
    fig.show()


def grafico_datos_faltantes(data, titulo="Porcentaje de Datos Faltantes por Variable"):
    """
    Genera un gráfico de barras con Plotly mostrando el porcentaje de datos faltantes en cada variable.

    Parámetros:
    - data: DataFrame de pandas con los datos.
    - titulo: Título del gráfico (opcional).
    
    Retorna:
    - Gráfico de barras en Plotly.
    """
    # Calcular porcentaje de datos faltantes
    missing_percent = (data.isnull().sum() / len(data)) * 100
    missing_percent = missing_percent.sort_values(ascending=False)  


    # Escala de colores en tonos rosa
    color_scale = ["#F8BBD0", "#F48FB1", "#F06292", "#EC407A", "#D81B60"]

    # Crear el gráfico de barras
    fig = px.bar(
        missing_percent, 
        x=missing_percent.index, 
        y=missing_percent.values,
        labels={'x': 'Variables', 'y': 'Porcentaje de Datos Faltantes (%)'},
        title=titulo,
        color=missing_percent.values, 
        color_continuous_scale=color_scale, 
        text=missing_percent.values.round(2)
    )

    # Ajustar diseño
    fig.update_layout(
        xaxis_title="Variables", 
        yaxis_title="Porcentaje de Datos Faltantes", 
        title_font_size=20, 
        xaxis_tickangle=-45,
        plot_bgcolor="white", 
        paper_bgcolor="white",
        font=dict(family="Bahnschrift", size=14, color="black"),
        title_font=dict(family="Bahnschrift", size=22, color="black"),
        yaxis=dict(range=[0, missing_percent.max() + 10])
    )

    # Mostrar valores sobre las barras
    fig.update_traces(textposition="outside")  

    # Mostrar gráfico
    fig.show()

def grafico_circular_categorico(data, columna, titulo="Distribución de Datos"):
    """
    Genera un diagrama circular con Plotly para una variable categórica.

    Parámetros:
    - data: DataFrame de pandas con los datos.
    - columna: Nombre de la columna categórica a analizar.
    - titulo: Título del gráfico (opcional).
    
    Retorna:
    - Diagrama circular en Plotly.
    """
    # Contar valores únicos de la columna
    conteo = data[columna].value_counts().reset_index()
    conteo.columns = [columna, 'Frecuencia']
    
    # Crear gráfico circular
    fig = px.pie(conteo, 
                 names=columna, 
                 values='Frecuencia', 
                 title=titulo,
                 color_discrete_sequence=['#ff69b4', '#ffc0cb', '#db7093', '#ff1493', '#c71585', '#ffb6c1',
                                          '#d87093', '#f08080', '#fa8072', '#e9967a'],
                 hole=0.3)

    # Estilo
    fig.update_traces(textinfo='percent+label', 
                      textfont=dict(family='Bahnschrift', size=14),
                      pull=[0.02]*len(conteo))  # Separación ligera

    fig.update_layout(title_font=dict(family='Bahnschrift', size=22, color='black'),
                      font=dict(family='Bahnschrift', color='black'),
                      template='plotly_white',
                      showlegend=True)

    # Mostrar gráfico
    fig.show()

def grafico_edad(data, x_titulo, y_titulo, titulo):
    orden_edad = [
        '40-54 años', '55-64 años', '65-74 años', '75+ años'
    ]

    conteo = data['grupo_edad'].value_counts().reset_index()
    conteo.columns = ['grupo_edad', 'Frecuencia']

    # Aplicar el orden correcto de edades
    conteo['grupo_edad'] = pd.Categorical(conteo['grupo_edad'], categories=orden_edad, ordered=True)
    conteo = conteo.sort_values('grupo_edad')

    # Crear gráfico de barras
    fig = px.bar(
        conteo,
        x='grupo_edad',
        y='Frecuencia',
        title=titulo,
        labels={'Frecuencia': y_titulo, 'grupo_edad': x_titulo},
        color_discrete_sequence=["#c71585"]
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title=x_titulo,
        yaxis_title=y_titulo,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Bahnschrift', size=14, color='black'),
        title_font=dict(family='Bahnschrift', size=22, color='black'),
        yaxis=dict(range=[0, conteo["Frecuencia"].max() + 5000])
    )

    fig.update_yaxes(tickformat=",")
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.show()


def grafico_mes_def(data, x_titulo, y_titulo, titulo):
    # Orden correcto de los meses
    orden_meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    # Conteo de frecuencias
    conteo = data['mes_def'].value_counts().reset_index()
    conteo.columns = ['mes_def', 'Frecuencia']

    # Aplicar orden de meses
    conteo['mes_def'] = pd.Categorical(conteo['mes_def'], categories=orden_meses, ordered=True)
    conteo = conteo.sort_values('mes_def')

    # Crear gráfico
    fig = px.bar(
        conteo,
        x='mes_def',
        y='Frecuencia',
        title=titulo,
        labels={'Frecuencia': y_titulo, 'mes_def': x_titulo},
        color_discrete_sequence=["#c71585"]
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title=x_titulo,
        yaxis_title=y_titulo,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Bahnschrift', size=14, color='black'),
        title_font=dict(family='Bahnschrift', size=22, color='black'),
        yaxis=dict(range=[0, conteo["Frecuencia"].max() + 500])
    )

    fig.update_yaxes(tickformat=",")
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.show()


import folium
from folium.features import GeoJsonTooltip

def crear_mapa_SMR(departamentos, nombre_columna, get_color, nombre_archivo):
    m = folium.Map(tiles="CartoDB positron", location=[4.5, -74], zoom_start=5)

    folium.GeoJson(
        departamentos,
        style_function=lambda feature: {
            "fillColor": get_color(feature["properties"].get("SMR")),
            "color": "black",
            "weight": 0.5,
            "fillOpacity": 0.85,
        },
        tooltip=GeoJsonTooltip(
            fields=[nombre_columna, "SMR"],
            aliases=["Departamento:", "SMR:"],
            localize=True,
            sticky=True
        )
    ).add_to(m)

    m.save(f'../map_outputs/{nombre_archivo}')
    

def crear_mapa_TAE(departamentos, nombre_columna, get_color, nombre_archivo):
    m = folium.Map(tiles="CartoDB positron", location=[4.5, -74], zoom_start=5)

    folium.GeoJson(
        departamentos,
        style_function=lambda feature: {
            "fillColor": get_color(feature["properties"].get("TAE")),
            "color": "black",
            "weight": 0.5,
            "fillOpacity": 0.85,
        },
        tooltip=GeoJsonTooltip(
            fields=[nombre_columna, "TAE"],
            aliases=["Departamento:", "TAE:"],
            localize=True,
            sticky=True
        )
    ).add_to(m)

    m.save(f'../map_outputs/{nombre_archivo}')
    

def crear_mapa_smr_mun(municipios, nombre_columna, get_color_smr_mun, nombre_archivo):
    m = folium.Map(tiles="CartoDB positron", location=[4.5, -74], zoom_start=5)

    folium.GeoJson(
        municipios,
        style_function=lambda feature: {
            "fillColor": get_color_smr_mun(feature["properties"].get("TAE")),
            "color": "black",
            "weight": 0.5,
            "fillOpacity": 0.85,
        },
        tooltip=GeoJsonTooltip(
            fields=[nombre_columna, "SMR"],
            aliases=["Municipio:", "SMR:"],
            localize=True,
            sticky=True
        )
    ).add_to(m)

    m.save(f'../map_outputs/{nombre_archivo}')
