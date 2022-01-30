import librosa
import numpy as np
import ffmpeg
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd
path="Figs\\"

#Create the fig from the path of the music

def figs(path_link,choice) :
    # sr = librosa.get_samplerate(path_link)
    #
    # frame_length = (2048 * sr) // 22050
    # hop_length = (512 * sr) // 22050
    # stream = librosa.stream(path_link,
    #         block_length = 256,
    #         frame_length = frame_length,
    #         hop_length = hop_length)
    # y0=next(stream)
    y,sr=librosa.load(path_link,duration=90)
    y0=y
    n = len(y)
    periods = n - n % sr
    y = y[:periods]
    y = y[::30]
    total_seconds = int(n // sr)
    minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60
    end_time = '00:0' + str(minutes) + ':' + str(remaining_seconds)
    end_time = pd.Timestamp(end_time)
    t = pd.date_range(start=pd.Timestamp('00:00:00'), end=end_time, periods=periods)
    t = t[::30]
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    BPM=int(tempo[0])
    fig = px.line(x=t, y=y,title='BPM : '+str(BPM))

    return fig,y0,sr

