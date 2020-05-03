# -*- coding: utf-8 -*-
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_excel("https://github.com/KaistZelatore/IE481_1_TestGithub/blob/master/covid-19-example.xlsx")

city_options = ['Seoul', 'Daegu', 'Daejeon', 'Busan', 'Gwangju']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H2("Coronavirus Dashboard in Korea"),
    html.Div(
        [
            dcc.Dropdown(
                id="City",
                options=[{
                    'label': i,
                    'value': i
                } for i in city_options],
                value='All Cites'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='covid-graph'),
])

@app.callback(
    dash.dependencies.Output('covid-graph', 'figure'),
    [dash.dependencies.Input('City', 'value')])

def update_graph(City):
     if City == "All Cities":
         df_plot = df.copy
     else:
         df_plot = df[df['City'] == City]


     pv = pd.pivot_table(
        df_plot, 
        index = ['AgeGroup'],
        columns = ['Status'],
        values = ['Population'],
        aggfunc=sum,
        fill_value=0)


     trace1 = go.Bar(x = pv.index, y=pv[('Population','Death')], name = 'Death')
     trace2 = go.Bar(x = pv.index, y=pv[('Population','Recovered')], name = 'Recovered')
     trace3 = go.Bar(x = pv.index, y=pv[('Population','Active')], name = 'Active')


     return {
        'data':  [trace1, trace2, trace3],
        'layout':
            go.Layout(
                title='People Status for {}'.format(City),
                xaxis_title = "Age group",
                yaxis_title = "The number of people (unit: 100)",
                barmode = 'stack')
    }


if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
