from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data

df = pd.read_csv('https://raw.githubusercontent.com/Artem34343512/RGR_voen_uch_stol/main/voen_uch_ctol.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Личные карточки военнообязанных'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)