from callback import *

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    ##En-tête

    dbc.Container(dbc.Row(
            [
                dbc.Col(html.H6("Henri Pinsolle, Ramzi Sayah, Nil Parent, Timothée Pascal")),
                dbc.Col(html.H1("Application",style = {'textAlign': 'center'})),
                dbc.Col(html.H6("Projet TDLOG 2021-2022", style = {'textAlign' : 'end'})),
            ]
        )
    ),

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
                    ),html.H1("->"),]),
                    dbc.Row([

                    html.Hr(),
                    html.H4("Mode d'emploi :"),
                    html.H5("Téléchargez une musique (mp3/wav) ci dessus"),
                    html.H5("Grâce à l'API Shazam on trouve les informations de la musique"),
                    html.H5("On fait une analyse musicale du son"),
                    html.H5("A droite : Reconnaisance du genre du son grâce au Machine Learning"),
            ])]
               , width=2),
            dbc.Col([html.Div(id='output-mp3-upload'),
                     html.Div(id="update_figs"),

                     dcc.Dropdown(
                         id='choice',
                         options=[
                             {'label': 'Wave', 'value': 'Simple'},
                         ],
                         searchable=True,
                         multi=False,
                         style={'display': 'none'}
                     ),
                    html.Button('Calcul', id='submit-val', n_clicks=0,style={'display': 'none'}),
                    dcc.Graph(id='wave',style={'display': 'none'}),
                    html.Div(id='test_layout'),

                    dbc.Col([html.Button('Extraire', id='extract', n_clicks=0,style={'display': 'none'}),])

                     ], width = 8),


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
            Output("wave",'style'),
            Output("extract",'style'),
            Input('submit-val', 'n_clicks'),
            State('upload-mp3', 'filename'),
            State('choice', 'value'), prevent_initial_call = True)
def update_figures(n_click,file_name, choice_fig) :
    return update_figs(n_click,file_name, choice_fig),{'display': 'block'},{'display': 'block'}

@app.callback(Output('test_layout', 'children'),
              State('upload-mp3', 'filename'),
              Input('extract','n_clicks'),
         [State('wave', 'relayoutData')],prevent_initial_call = True) # this triggers the event
def update_ext(name,n_click,relayout_data) :
    return update_extraction(name,n_click,relayout_data)



if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)
