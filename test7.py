import numpy as np
from scipy.io.wavfile import write
from thinkdsp import read_wave
import matplotlib.pyplot as plt
from numpy import fft
from IPython.display import Audio #Probando uso de libreria para guardar señal filatrada en archivo .WAV

#08/11/2020-23:06 
#Lectura de .WAV y extracción de amplitudes
#Espectro por FFT original y filtrado con indices
#Ejes frecuencias y tiempo original
#Espectro de poder original

#NOTE: De momento la señal puede ser filtrada y devuelta al dominio del tiempo
# pero al plotear con variable 'time' para eje x se obtiene la señal con 'efecto espejo'
# Al plotear con variable 'fs' para eje x se obtiene un resultado esperado pero con escala erronea
#
#
#SOLUCION: Intentando hacer ifft para fs en espera de obtener una escala adecuada en fs

sampling_rate = 46000


dataW = read_wave('outputRecording1.wav').ys #Lectura de .WAV y extracción de amplitudes
dataW = np.asanyarray(dataW)
time = np.arange(len(dataW)) / sampling_rate #Array para eje x del ploteo (En Tiempo)

fourier_transform = np.fft.fft(dataW) #Fourier Transform (Espectro normal)
fourier_transform = np.asanyarray(np.abs(fourier_transform))
fs = np.fft.fftfreq(len(dataW),(1/sampling_rate)) #Array para eje x del ploteo (En Frecuencias)
fs = np.asanyarray(np.abs(fs))

power_spectrum = np.square(fourier_transform) #Eleva amplitudes del espectro normal al cuadrado para obtener el espectro de poder

#Iniciando proceso de separación
indices = power_spectrum > 4000000 #4000000 como valor de corte. Todas las amplitudes superiores a 2500 pasan intactas, el resto es seteado a cero.
frecuenciasFiltradas = fourier_transform * indices

clean_signal = np.fft.ifft(frecuenciasFiltradas) #Transformada Inversa para obtener la señal filtrada COMPLETA en el tiempo.
clean_signal = np.asanyarray(clean_signal)
high, low = abs(max(clean_signal)), abs(min(clean_signal))
clean_signal = 1 * clean_signal / max(high, low)

# time2 = np.fft.ifft(fs) #Intentando obtener un eje x apropiado para la señal filtrada
# time2 = np.asanyarray(fs) 


plt.plot(fs, clean_signal) #Ploteo de (eje x) vs (eje y).
plt.show()
plt.clf()



