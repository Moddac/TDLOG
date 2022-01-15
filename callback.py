import datetime
from recognition import recognize
from figs import figs
import base64
import numpy as np
from scipy.io.wavfile import write
import ffmpeg
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html


def parse_contents(contents, filename, date,url):
    title, artist, img = recognize(url)

    return html.Div([
        html.H2('Analyse a partir de Shazam'),
        html.H6(filename, className="song-title"),
        html.Div([
            html.H5('Artiste : ' +artist),
            html.H5('Titre : ' + title),
            html.Img(src=img),
        ]),
        html.H6(),
        html.Audio(src=contents, controls=True),
        html.Hr(),





    ])

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        contents=list_of_contents[0]
        file_name=list_of_names[0]
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        with open("Bibliotheque\ "+file_name , "wb") as wav_file:
            wav_file.write(decoded)
        url="Bibliotheque\ "+file_name
        children = [
            parse_contents(c, n, d,url) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

def update_figs(n_click,file_name, choice_fig) :
    if choice_fig is not None :
        file_name=file_name[0]
        url="Bibliotheque\ "+file_name
        figs(url,choice_fig)

        image_filename = "Figs\\" + choice_fig + ".png"  # replace with your own image
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())

        test_base64 = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

        if choice_fig=="Spectogram" :
            return html.Div([html.Img(src='data:image/png;base64,{}'.format(test_base64), height=800, width=800),])
        else :
            return html.Div([html.Img(src='data:image/png;base64,{}'.format(test_base64), height=400, width=800), ])