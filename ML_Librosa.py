from tensorflow.keras.models import load_model
import pandas as pd
import librosa
import librosa.display
import librosa.feature
import numpy as np
import pickle
import keras as k
import plotly.express as px
pd.options.plotting.backend = "plotly"

#-----Loading model and parameters-----
# Corresponding dictionnary between genre and number
label_to_int = {'blues' : 0, 'classical' : 1, 'country' : 2, 'disco' : 3, 'hiphop' : 4,
          'jazz' : 5, 'metal' : 6, 'pop' : 7, 'reggae' : 8, 'rock' : 9}
int_to_label = {0 : 'blues', 1 : 'classical', 2 : 'country', 3 : 'disco', 4 : 'hiphop',
                5 : 'jazz', 6 : 'metal', 7 : 'pop', 8 : 'reggae', 9 : 'rock'}

filepath = './saved_model'
model = load_model(filepath, compile=True)
scaler = pickle.load(open('params/scaler.pkl', 'rb'))

def prediction(y,sr) :
    y, _ = librosa.effects.trim(y)

    features = []

    # Chroma
    chroma_stft = librosa.feature.chroma_stft(y,sr,hop_length=5000)
    chroma_stft_mean, chroma_stft_var = np.mean(chroma_stft), np.var(chroma_stft)
    features += [chroma_stft_mean, chroma_stft_var]

    # RMS
    rms = librosa.feature.rms(y)
    rms_mean, rms_var = np.mean(rms), np.var(rms)
    features += [rms_mean, rms_var]

    # Spectral Centroid
    spectral_centroid = librosa.feature.spectral_centroid(y, sr)
    spectral_centroid_mean, spectral_centroid_var = np.mean(spectral_centroid), np.var(spectral_centroid)
    features += [spectral_centroid_mean, spectral_centroid_var]

    #Spectral Bandwith
    spectral_bandwith = librosa.feature.spectral_bandwidth(y, sr)
    spectral_bandwith_mean, spectral_bandwith_var = np.mean(spectral_bandwith), np.var(spectral_bandwith)
    features += [spectral_bandwith_mean, spectral_bandwith_var]

    # Rolloff
    rolloff = librosa.feature.spectral_rolloff(y, sr)
    rolloff_mean, rolloff_var = np.mean(rolloff), np.var(rolloff)
    features += [rolloff_mean, rolloff_var]

    # Zero crossing rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    zero_crossing_rate_mean, zero_crossing_rate_var = np.mean(zero_crossing_rate), np.var(zero_crossing_rate)
    features += [zero_crossing_rate_mean, zero_crossing_rate_var]

    # Harmony and perceptrual
    harmony, percussive = librosa.effects.hpss(y)
    harmony_mean, harmony_var = np.mean(harmony), np.var(harmony)
    percussive_mean, percussive_var = np.mean(percussive), np.var(percussive)
    features += [harmony_mean, harmony_var, percussive_mean, percussive_var]

    # Tempo
    onset_env = librosa.onset.onset_strength(y, sr)
    tempo = librosa.beat.tempo(onset_env, sr)[0]
    features += [tempo]

    # MFCC
    mfcc = librosa.feature.mfcc(y, sr)
    mfcc_means, mfcc_var = np.mean(mfcc, axis=1), np.var(mfcc, axis=1)
    for index in range(mfcc.shape[0]):
      features += [mfcc_means[index], mfcc_var[index]]
    features = scaler.transform(np.array([features]))
    result=model.predict(features)[0]

    df=pd.Series(data=result,index=label_to_int,name="probabilities")

    fig = df.plot.barh()

    return (int_to_label[np.argmax(result)],fig)
