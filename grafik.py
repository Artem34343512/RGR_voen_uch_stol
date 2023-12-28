from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/Artem34343512/RGR_voen_uch_stol/main/RGR_voen_uch_stol.csv')

# Initialize the app
app = Dash(__name__)

# Создаем линейный график
fig = px.line(df, x='ФИО', y='Должность', title='Линейный график ФИО и Должность военнообязанных')

# Добавляем график в макет приложения
app.layout = html.Div([
   dcc.Graph(figure=fig)
])

if __name__ == '__main__':
  app.run_server(debug=True)

