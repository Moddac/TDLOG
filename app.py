import datetime

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    ##En-tête

    dbc.Container(dbc.Row(
            [
                dbc.Col(html.H6("Henri Pinsolle, Ramzi Sayah, Nil Parent, Timothée Pascal")),
                dbc.Col(html.H1("Shazam méfie toi",style = {'textAlign': 'center'})),
                dbc.Col(html.H6("Projet TDLOG 2021-2022", style = {'textAlign' : 'end'})),
            ]
        )
    ),

    ## Bibliothèque

    dbc.Container([
        dbc.Row([
            dbc.Col([
                    html.H2('Bibliothèque'),
                    dcc.Upload(
                        id='upload-mp3',
                        children=html.Div([
                            'Drag and Drop or ',
                            dbc.Button("Select File", color="primary", className="me-1")
                            ]),
                        style={
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            },
                        # Allow multiple files to be uploaded
                        multiple=True
                    )
            ], width=2),
            dbc.Col(html.Div(id='output-mp3-upload'), width = 8)
        ]),
    ]),



])

def parse_contents(contents, filename, date):
    return html.Div([
        html.H2('Analyse'),
        html.H1(filename, className="song-title"),
        html.H5('Artiste, Album, Année de sortie'),
        html.H6('Style, BPM'),
        html.H6(),
        html.Audio(src=contents, controls=True),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    options=[
                        {'label': '1er truc à afficher', 'value': '1'},
                        {'label': '2ème', 'value': '2'},
                        {'label': '3ème', 'value': '3'}
                    ],
                    searchable=False
                )
            ], width=2),
        ]),
        
        html.H2('Sélection d\'une partie de la chanson'),
        dcc.RangeSlider(
            count=1,
            min=-5,
            max=10,
            step=0.5,
            value=[-3, 7]
            )


    ])


@app.callback(Output('output-mp3-upload', 'children'),
              Input('upload-mp3', 'contents'),
              State('upload-mp3', 'filename'),
              State('upload-mp3', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)
