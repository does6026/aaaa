# -*- coding: utf-8 -*-
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

colors1 = {
     'background' : '#F8FF59',
     'text' : '#060606'
}

colors2 = {
     'background' : '#35E072',
     'text' : '#060606'
}


app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
             'color' : colors1['text']
             
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
       'color' : colors1['text']
    }),

    html.Div(children=[
        html.Div(
            dcc.Graph(
                id='example-graph-1',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {'plot_bgcolor' : colors1['background'],
                            'paper_bgcolor' : colors1['background'],
                             'font': {
                                 'color' : colors1['text']
                             },
                        'width': 700,
                        'height': 400
                    }
                }
            ),
            style={
                'display' : 'inline-block',
                'border' : '2px black solid'
            }
        ),
        html.Div(
            dcc.Graph(
                id='example-graph-2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {'plot_bgcolor' : colors2['background'],
                               'paper_bgcolor' : colors2['background'],
                         
                        'font': {
                            'color' : colors2['text']
                        },
                        'width': 400,
                        'height': 400
                    }
                }
            ),
            style={
                'display' : 'inline-block',
                'marginLeft' : 30,
                'border' : '2px black solid'
            }
        )
    ], style={
       'display' : 'flex',
       'justify-content' : 'center'
    })

])

if __name__ == '__main__':
    app.run_server(debug=True)
