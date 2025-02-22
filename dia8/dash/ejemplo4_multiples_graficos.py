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
    html.H1("Dashboard Completo de Pingüinos"),
    
    dcc.Dropdown(
        id="dropdown_especie",
        options=[{"label": especie, "value": especie} for especie in df["species"].unique()],
        value="Adelie",
        clearable=False
    ),

    html.Div([
        dcc.Graph(id="grafico_dispersion"),
        dcc.Graph(id="grafico_boxplot")
    ])
])

@app.callback(
    [Output("grafico_dispersion", "figure"),
     Output("grafico_boxplot", "figure")],
    Input("dropdown_especie", "value")
)
def actualizar_graficos(especie):
    df_filtrado = df[df["species"] == especie]

    fig1 = px.scatter(df_filtrado, x="bill_length_mm", y="bill_depth_mm", color="sex",
                      title=f"Longitud vs Profundidad del Pico ({especie})")

    fig2 = px.box(df_filtrado, x="sex", y="body_mass_g", title=f"Masa Corporal por Sexo ({especie})")

    return fig1, fig2

if __name__ == "__main__":
    app.run_server(debug=True)
