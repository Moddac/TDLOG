import datetime
from recognition import *
from figs import *
import base64
import numpy as np
from scipy.io.wavfile import write
import ffmpeg
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html


from ML_Librosa import *
import soundfile as sf
import pandas as pd
import librosa


def parse_contents(contents, filename, date,url):
    title, artist, img = recognize(url)
    return html.Div([
        html.H2('Analyse a partir de Shazam'),
        html.H6(filename, className="song-title"),
        html.Div([
            html.H5('Artiste : ' +artist),
            html.H5('Titre : ' + title),
            html.Img(src=img,height=400,width=400),
        ]),
        html.H6(),
        html.Audio(src=contents, controls=True),
    ])

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        contents=list_of_contents[0]
        file_name=list_of_names[0]
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        with open("Bibliotheque\\"+file_name , "wb") as wav_file:
            wav_file.write(decoded)
        url="Bibliotheque\\"+file_name
        children = [
            parse_contents(c, n, d,url) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children,{'display': 'block'},{'display': 'block'}

def update_figs(n_click,file_name, choice_fig) :
    if choice_fig is not None :
        file_name=file_name[0]
        url="Bibliotheque\\"+file_name
        fig,y,sr=figs(url,choice_fig)

        image_filename = "Figs\\" + choice_fig + ".png"  # replace with your own image
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())

        test_base64 = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

        if choice_fig=="Simple" :
            return fig,y,sr


def update_extraction(name,n_click,relayout_data) :
    name=name[0]
    time_begin = pd.Timestamp(relayout_data['xaxis.range[0]'])
    time_end = pd.Timestamp(relayout_data['xaxis.range[1]'])
    offset = time_begin.minute*60 +time_begin.second
    duration = time_end.minute*60 +time_end.second -offset
    path='assets/sample_'+str(n_click)+name
    path = path.replace("mp3","wav")
    path = path.replace(" ","")
    path = path.replace(".",'',path.count(".")-1)
    y,sr = librosa.load("Bibliotheque\\"+name, offset= offset,duration=duration)
    sf.write(path, y, sr, subtype='PCM_24')
    return [html.H5('Extraction réussie'),html.Audio(src=path, controls=True,style={'display': 'block'},loop=True ),]

def update_prediction(y,sr) :
    y = np.array(y)
    result,fig =prediction(y,sr)
    return [html.H5("Résultat trouvé : "+result),
            dcc.Graph(figure=fig)]