import pandas as pd
import plotly.express as px

color_scale = ["#F8BBD0", "#F48FB1", "#F06292", "#EC407A", "#D81B60"]

def grafico_datos_faltantes(data, titulo="Porcentaje de Datos Faltantes por Variable"):

    missing_percent = (data.isnull().sum() / len(data)) * 100
    missing_percent = missing_percent.sort_values(ascending=False)  

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

    fig.update_traces(textposition="outside")  
    fig.show()