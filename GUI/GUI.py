#!/usr/bin/env python 


# GUI Libs
from dash import ALL, callback_context, dcc, html, ctx
from dash.dependencies import Input, Output, State
from dash.dcc import Dropdown
import dash_bootstrap_components as dbc
import plotly.express as px
from jupyter_dash import JupyterDash
import dash_daq as daq
import warnings
warnings.filterwarnings("ignore")


# Libs
import io
import pandas as pd
import requests


# Self modules:
from defines import *



# Configuration
REQUEST_IP = "127.0.0.1"
REQUEST_PORT = str(API_PORT)
UPDATE_INTERVAL = 2000*1000
TITLE = "GPS Interface"


# df = pd.read_csv("data.csv", sep=";")




def main():

    app = JupyterDash(__name__, external_stylesheets=[dbc.themes.MINTY])

    global df
    df = pd.DataFrame()



    #------------------------------
    #             GUI
    #------------------------------

    app.layout = dbc.Container([
        dbc.Col([
            html.Br(),
            html.H3(id="title", children=TITLE),
            dcc.Interval(
                id='interval-component',
                interval=UPDATE_INTERVAL,
                n_intervals=0
            ),
            html.Br(),
            html.Hr(),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='GPS', style={'width': '120vh', 'height': '72vh'}),
                ],
                width={'size': 7, 'offset': 0, 'order': 1}),


                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            daq.Gauge(
                                id='speed',
                                showCurrentValue=True,
                                units="km/h",
                                value=0.0,
                                label='Speed',
                                max=1500,
                                min=0,
                                size=150
                            )
                        ],
                        width={'offset': 0, 'order': 1}),
                        dbc.Col([
                            daq.Gauge(
                                id='acc',
                                showCurrentValue=True,
                                units="g",
                                value=0.0,
                                label='Acceleration',
                                max=30,
                                min=0,
                                size=150
                            ),
                        ],
                        width={ 'offset': 0, 'order': 2}),    
                    ]),
                    dcc.Graph(id='height', style={'width': '60vh', 'height': '40vh'})
                ],
                width={'size': 4, 'offset': 0, 'order': 2}), 

            ]),

        ], width={'size': 14, 'offset': 0, 'order': 1}),
    ], fluid=True)






    #------------------------------
    #         CALLBACKS
    #------------------------------

    @app.callback(Output('GPS', 'figure'),
                  Output('height', 'figure'),
                   Input('interval-component', 'n_intervals'),
                   prevent_initial_call=True)
    def update_text(n):
        str_new_data = requests.get(url="http://"+REQUEST_IP+":"+REQUEST_PORT+"/get_new_data").content
        global df
        df = pd.concat([df, pd.read_csv(io.StringIO(str(str_new_data)), delim_whitespace=True, skipinitialspace=True)])
        return px.scatter(x=df["TIME"].to_list(), y=df["ALT"].to_list()), px.scatter(x=[1,2,3], y=[1,2,3])

    app.run_server(debug=True)



if __name__ == '__main__':
    main()



