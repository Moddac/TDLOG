import os
import io
import base64
import dash
import matplotlib.pyplot as plt
import librosa



import wave
from pydub import AudioSegment
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server





app.layout = html.Div([
    html.H2('Shazam, méfie toi grandement'),

html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
    html.Div(id='output-data-upload'),
]),
])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(contents, file_name, list_of_dates):

    if file_name!=None :



        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        file_name=str(file_name)

        file_name.replace(".mp3",".wav")
        print(file_name)
        path="Bibliotheque\\"+'Demo Track 1.wav'
        src = "Demo Track 1.mp3"
        dst = "test.wav"

        # convert wav to mp3
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        print(path)

        #y,sr=librosa.load("12.wav")

        if "mp3" in file_name :
            return html.H6("C'est bien un MP3")
        else :
            return html.H6("Il se passe rien")


if __name__ == '__main__':
    app.run_server(debug=True)