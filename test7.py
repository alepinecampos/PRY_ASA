import numpy as np
from scipy.io.wavfile import write
from thinkdsp import read_wave
import matplotlib.pyplot as plt
from numpy import fft
from IPython.display import Audio #Probando uso de libreria para guardar señal filatrada en archivo .WAV

#08/11/2020-23:06 
#Lectura de .WAV y extracción de amplitudes
#Espectro por FFT 
#Ejes frecuencias y tiempo original
#Espectro de poder

sampling_rate = 46000


dataW = read_wave('outputRecording1.wav').ys #Lectura de .WAV y extracción de amplitudes
dataW = np.asanyarray(dataW)
time = np.arange(len(dataW)) / sampling_rate #Array para eje x del ploteo (En Tiempo)

fourier_transform = np.fft.fft(dataW) #Fourier Transform (Espectro normal)
fourier_transform = np.asanyarray(np.abs(fourier_transform))
fs = np.fft.fftfreq(len(dataW),(1/sampling_rate)) #Array para eje x del ploteo (En Frecuencias)
fs = np.asanyarray(np.abs(fs))

power_spectrum = np.square(fourier_transform) #Eleva amplitudes del espectro normal al cuadrado para obtener el espectro de poder

plt.plot(fs, power_spectrum) #Ploteo de (eje x) vs (eje y).
plt.show()



