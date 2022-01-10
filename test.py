import librosa
import numpy
from scipy.io.wavfile import write
import ffmpeg
import librosa.display
import matplotlib.pyplot as plt
y,sr=librosa.load('Demo Track 1.mp3')
plt.plot(y);
plt.title('Signal');
plt.xlabel('Time (samples)');
plt.ylabel('Amplitude');
plt.show()
