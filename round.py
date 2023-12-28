from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Artem34343512/RGR_voen_uch_stol/main/RGR_voen_uch_stol.csv')

app = Dash(__name__)
grouped_df = df.groupby('Категория').sum()

labels = grouped_df.index
sizes = grouped_df['Количество военнообязанных по категориям']
colors = ['#ff9999', '#66b3ff']
fig1, ax1 = plt.subplots()


ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title('Количество военнообязанных по категориям')


plt.show()
if __name__ == '__main__':
    app.run(debug=True)