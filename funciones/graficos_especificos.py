import pandas as pd
import plotly.express as px

def grafico_edad(data, x_titulo, y_titulo, titulo):
    orden_edad = ['40-54 años', '55-64 años', '65-74 años', '75+ años']

    conteo = data['grupo_edad'].value_counts().reset_index()
    conteo.columns = ['grupo_edad', 'Frecuencia']

    # Aplicar el orden correcto de edades
    conteo['grupo_edad'] = pd.Categorical(conteo['grupo_edad'], categories=orden_edad, ordered=True)
    conteo = conteo.sort_values('grupo_edad')

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

    conteo = data['mes_def'].value_counts().reset_index()
    conteo.columns = ['mes_def', 'Frecuencia']

    # Aplicar orden de meses
    conteo['mes_def'] = pd.Categorical(conteo['mes_def'], categories=orden_meses, ordered=True)
    conteo = conteo.sort_values('mes_def')

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



