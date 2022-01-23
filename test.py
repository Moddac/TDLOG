import pandas as pd
import librosa
import numpy as np
import plotly.express as px

import soundfile as sf

periods=10

end_time='00:0'+str(1)+':'+str(30)

end_time=pd.Timestamp(end_time)
duration=(60*end_time.minute+end_time.second)
y,sr = librosa.load("Luis Fonsi - Despacito ft. Daddy Yankee.mp3",offset= 0,duration=duration)
sf.write('stereo_file.wav', y, sr, subtype='PCM_24')