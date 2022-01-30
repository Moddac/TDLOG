from callback import *

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    ##En-tête


    dbc.Container(dbc.Row(
        [
            dbc.Col(html.H6("Henri Pinsolle, Ramzi Sayah, Nil Parent, Timothée Pascal",
                            style={'font-family': 'Arial, sans-serif'})),
            dbc.Col(html.H1("Music'Ally", style={'textAlign': 'center', 'font-family': 'Arial, sans-serif'})),
            dbc.Col(html.H6("Projet TDLOG 2021-2022", style={'textAlign': 'end', 'font-family': 'Arial, sans-serif'})),
        ]
    ),
        style={'color': 'lavender', 'background-color': 'steelblue', 'border-radius': '5px',
               'box-shadow': '1px 1px 1px grey'}),
    ## Bibliothèque

    dbc.Container([
        dbc.Row([
            dbc.Col([
                    dbc.Row([html.H2('Bibliothèque'),

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
                            'padding' : '10 px'
                            },
                        # Allow multiple files to be uploaded
                        multiple=True
                    ),
                    html.Div(id='output-mp3-upload'),])]

               ),
            dbc.Col([
                html.H2('Machine Learning'),
                html.H5("Modèle pré entrainé d'une accuracy de 93%"),
                html.H5('Genres possibles : blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock'),
                html.Button('Prediction', id='ML', n_clicks=0, style={'display': 'none'}),
                html.Div(id='ML_prediction')
            ])
        ]),

            dbc.Row([
                     html.Div(id="update_figs"),
                     dcc.Store(id = 'y'),
                     dcc.Store(id = 'sr'),
                     html.Div([
                     dcc.Dropdown(
                         id='choice',
                         options=[
                             {'label': 'Wave', 'value': 'Simple'},
                         ],
                         searchable=True,
                         multi=False,
                         style={'display': 'none'}
                     ),
                     html.Button('Calcul', id='submit-val', n_clicks=0,style={'display': 'none'})
                     ],style={"width" : "50%"}),

                    dcc.Graph(id='wave',style={'display': 'none'}),
                    html.Div(id='test_layout'),

                    dbc.Col([html.Button('Extraire', id='extract', n_clicks=0,style={'display': 'none'}),])

                     ]),



        ]),
    ])








@app.callback(Output('output-mp3-upload', 'children'),
              Output('choice','style'),
              Output('submit-val','style'),
              Input('upload-mp3', 'contents'),
              State('upload-mp3', 'filename'),
              State('upload-mp3', 'last_modified'),prevent_initial_call = True)
def update_mp3(list_of_contents, list_of_names, list_of_dates) :
    if list_of_contents is not None :
        return update_output(list_of_contents, list_of_names, list_of_dates)


@app.callback(
            Output("wave",'figure'),
            Output('y','data'),
            Output('sr','data'),
            Output("wave",'style'),
            Output("extract",'style'),
            Output("ML",'style'),
            Input('submit-val', 'n_clicks'),
            State('upload-mp3', 'filename'),
            State('choice', 'value'), prevent_initial_call = True)
def update_figures(n_click,file_name, choice_fig) :
    fig,y,sr=update_figs(n_click,file_name, choice_fig)
    return fig,y,sr,{'display': 'block'},{'display': 'block'},{'display': 'block'}

@app.callback(Output('test_layout', 'children'),
              State('y','data'),
              State('upload-mp3', 'filename'),
              Input('extract','n_clicks'),
         [State('wave', 'relayoutData')],prevent_initial_call = True) # this triggers the event
def update_ext(y,name,n_click,relayout_data) :
    return update_extraction(name,n_click,relayout_data)


@app.callback(Output('ML_prediction', 'children'),
              State('y','data'),
              State('sr','data'),
              Input('ML','n_clicks'),prevent_initial_call = True)
def update_predict(y,sr,n_click) :
    return update_prediction(y,sr)



if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)
