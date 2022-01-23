import librosa
import numpy as np
import ffmpeg
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd
path="Figs\\"

def figs(url,choice) :
    y, sr = librosa.load(url, duration=60)
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

    fig = px.line(x=t, y=y)
    # fig.update_layout(
    #     xaxis=dict(
    #         rangeselector=dict(
    #             buttons=list([
    #                 dict(step="all")
    #             ])
    #         ),
    #         rangeslider=dict(
    #             visible=True
    #         ),
    #         type="date"
    #     )
    # )
    return fig

