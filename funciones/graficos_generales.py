import pandas as pd
import plotly.express as px

def grafico_barras_categoricas(data, columna, x_titulo = "eje x", y_titulo = "ejey", titulo="Distribución de Datos"):
    conteo = data[columna].value_counts().reset_index()
    conteo.columns = [columna, 'Frecuencia']
    
    fig = px.bar(conteo, 
                 x=columna, 
                 y='Frecuencia',
                 title=titulo,
                 labels={'Frecuencia': 'Cantidad de Casos', columna: 'Categoría'},
                 color_discrete_sequence=["#c71585"]) 
    fig.update_layout(template="plotly_white", 
                      xaxis_title=x_titulo, 
                      yaxis_title=y_titulo, 
                      plot_bgcolor='white', 
                      paper_bgcolor='white',
                      font=dict(family='Bahnschrift', size=14, color='black'),
                      title_font=dict(family='Bahnschrift', size=22, color='black'),
                      yaxis=dict(range=[0, conteo["Frecuencia"].max() + 5000]))  

    fig.update_yaxes(tickformat=",")
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.show()

color_scale = ['#ff69b4', '#ffc0cb', '#db7093', '#ff1493', '#c71585', '#ffb6c1', '#d87093', '#f08080', '#fa8072', '#e9967a']


def grafico_circular_categorico(data, columna, titulo="Distribución de Datos"):

    conteo = data[columna].value_counts().reset_index()
    conteo.columns = [columna, 'Frecuencia']
    
    fig = px.pie(conteo, 
                 names=columna, 
                 values='Frecuencia', 
                 title=titulo,
                 color_discrete_sequence=color_scale,
                 hole=0.3)

    fig.update_traces(textinfo='percent+label', 
                      textfont=dict(family='Bahnschrift', size=14),
                      pull=[0.02]*len(conteo))

    fig.update_layout(title_font=dict(family='Bahnschrift', size=22, color='black'),
                      font=dict(family='Bahnschrift', color='black'),
                      template='plotly_white',
                      showlegend=True)
    fig.show()