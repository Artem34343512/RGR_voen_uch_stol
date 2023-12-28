from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/Artem34343512/RGR_voen_uch_stol/main/RGR_voen_uch_stol.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Гистограмма по категориям военнообязанных'),

    dcc.Graph(figure=px.histogram(df, x='Категория', y='Количество военнообязанных по категориям'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)