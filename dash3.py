# -*- coding: utf-8 -*-
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Table([
        html.Tr([html.Td(dcc.Input(id='my-input1', type='number', value= 4)),  html.Td(dcc.Input(id='my-input2', type='number', value=9))]),
        html.Tr([html.Td(id='multiple_1_1'), html.Td(id='multiple_1_2')]),
        html.Tr([html.Td(id='multiple_2_1'), html.Td(id='multiple_2_2')]),
        html.Tr([html.Td(id='multiple_3_1'), html.Td(id='multiple_3_2')]),
        html.Tr([html.Td(id='multiple_4_1'), html.Td(id='multiple_4_2')]),
        html.Tr([html.Td(id='multiple_5_1'), html.Td(id='multiple_5_2')])
    ])
])

@app.callback(
     [Output('multiple_1_1', 'children'),
     Output('multiple_2_1', 'children'),
     Output('multiple_3_1', 'children'),
     Output('multiple_4_1', 'children'),
     Output('multiple_5_1', 'children')],
     [Input(component_id='my-input1', component_property = 'value')]
)
def callbackFunc1(num):
    result = []
    for i in range(1,6):
        str = "%i x %i = %i" % (num, i, num*i)
        result.append(str)

    return result


@app.callback(
    [Output('multiple_1_2', 'children'),
     Output('multiple_2_2', 'children'),
     Output('multiple_3_2', 'children'),
     Output('multiple_4_2', 'children'),
     Output('multiple_5_2', 'children')],
     [Input(component_id='my-input2', component_property = 'value')]
)

def callbackFunc2(num):
    result = []
    for i in range(1,6):
        str = "%i x %i = %i" % (num, i, num*i)
        result.append(str)

    return result



if __name__ == '__main__':
    app.run_server(debug=True)

