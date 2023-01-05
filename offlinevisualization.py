# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

app = Dash(__name__)

df = pd.read_csv(
    'C:\\Users\\Hp\\Desktop\\P2M Codes\\data.csv')

fig = px.scatter(df, x="x", y="y", color='type')

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
