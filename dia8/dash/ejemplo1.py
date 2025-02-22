import dash
from dash import html,dcc
from plotly import express as px
import pandas as pd
import seaborn as sns


df = sns.load_dataset('penguins')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mi primer dashboard en Dash - César Mayta'),
    html.Div([
        dcc.Graph(
            figure=px.scatter(df, x='flipper_length_mm', y='bill_length_mm', color='species')
        )
    ])   
])


if __name__ == '__main__':
    app.run_server(debug=True)