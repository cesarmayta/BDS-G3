import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import seaborn as sns
import pandas as pd



import plotly.express as px

# Cargar dataset de Seaborn
df = sns.load_dataset("penguins")

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Interactivo de Pingüinos"),
    
    html.Div([
        html.Label("Selecciona una especie:"),
        dcc.Dropdown(
            id="dropdown_especie",
            options=[{"label": especie, "value": especie} for especie in df["species"].unique()],
            value="Adelie",
            clearable=False
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Selecciona una variable:"),
        dcc.RadioItems(
            id="radio_variable",
            options=[{"label": "Masa Corporal", "value": "body_mass_g"},
                     {"label": "Longitud del Aleta", "value": "flipper_length_mm"}],
            value="body_mass_g"
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id="grafico_histograma")
])

# Callback para actualizar el gráfico
@app.callback(
    Output("grafico_histograma", "figure"),
    [Input("dropdown_especie", "value"),
     Input("radio_variable", "value")]
)
def actualizar_histograma(especie, variable):
    df_filtrado = df[df["species"] == especie]
    fig = px.histogram(df_filtrado, x=variable, nbins=20, title=f"Distribución de {variable} en {especie}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
