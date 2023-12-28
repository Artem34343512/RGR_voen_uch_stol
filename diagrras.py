from dash import Dash, dcc, html
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Artem34343512/RGR_voen_uch_stol/main/RGR_voen_uch_stol.csv')

# Initialize the app
app = Dash(__name__)

# Создаем диаграмму рассеивания
fig = go.Figure(data=go.Scatter(
   x=df['ФИО'],
   y=df['Воинское звание'],
   mode='markers'
))

# Добавляем заголовки и метки
fig.update_layout(
   title='Диаграмма рассеивания',
   xaxis_title='ФИО',
   yaxis_title='Воинское звание'
)

# Отображаем диаграмму
fig.show()

if __name__ == '__main__':
   app.run(debug=True)