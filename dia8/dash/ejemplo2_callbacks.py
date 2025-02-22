import dash
from dash import html,dcc
from plotly import express as px
import pandas as pd
import seaborn as sns
from dash.dependencies import Input, Output


df = sns.load_dataset('penguins')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mi primer dashboard en Dash - César Mayta'),
    html.P('Seleccione una especie:'),
    dcc.Dropdown(
        id='species-dropdown',
        options=[{'label': especie, 'value': especie} for especie in df['species'].unique()],
        value='Adelie',
        clearable=False
    ),
    dcc.Graph(id='scatter-plot')
])

##callback para actualizar el gráfico
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('species-dropdown', 'value')
)
def actualizar_grafico(especie):
    df_filtrado = df[df['species'] == especie]
    fig = px.scatter(df_filtrado, x='bill_length_mm', y='bill_depth_mm', color='sex',
                     title=f'Ancho y largo del pico de los pingüinos {especie}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)