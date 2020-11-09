import numpy as np
from scipy.io.wavfile import write
from thinkdsp import read_wave
import matplotlib.pyplot as plt
from numpy import fft
from IPython.display import Audio #Probando uso de libreria para guardar señal filatrada en archivo .WAV


sampling_rate = 46000



dataW = read_wave('outputRecording1.wav').ys
dataW = np.asanyarray(dataW)
time = np.arange(len(dataW)) / sampling_rate #Array para eje x del ploteo (En Tiempo)
time = np.asanyarray(time)

# l = len(dataW)
# l = l//2
# l = np.int64(l)

fourier_transform = np.fft.fft(dataW) #Fourier Transform (Espectro normal)
fourier_transform = np.asanyarray(np.abs(fourier_transform))
fs = np.fft.fftfreq(len(dataW),(1/sampling_rate))
fs = np.asanyarray(np.abs(fs))

# abs_fourier_transform = np.abs(fourier_transform)#Toma unicamente los positivos con valor abs. Se obtiene el espectro normal.
# abs_fourier_transform = np.abs(fourier_transform[0:l])
# abs_fourier_transform.resize(l*2, refcheck=False)
power_spectrum = np.square(fourier_transform) #Eleva amplitudes del espectro normal al cuadrado para obtener el espectro de poder

# frequency = np.linspace(0, sampling_rate/2, len(power_spectrum)) #Array para eje x del ploteo (En Frecuencias)


#Starting separation/cleaning process
indices = power_spectrum > 5000000 #X como valor de corte. Todas las amplitudes superiores a 2500 pasan intactas, el resto es seteado a cero.
# indices2 = power_spectrum < 4000000

power_spectrum_clean = power_spectrum * indices #Espectro de poder filtrado
frecuenciasFiltradas = fourier_transform * indices

# abs_fourier_transform_clean = abs_fourier_transform * indices #Espectro de frecuencias (normal) filtrado.
# noise_spectrum = abs_fourier_transform * indices2 #Espectro de frecuencias (normal) del ruido removido.

clean_signal = np.fft.ifft(frecuenciasFiltradas) #Transformada Inversa para obtener la señal filtrada COMPLETA en el tiempo.
clean_signal = np.asanyarray(clean_signal)


high, low = abs(max(clean_signal)), abs(min(clean_signal))
clean_signal = 1 * clean_signal / max(high, low)

# noise_signal = np.fft.ifft(noise_spectrum) #Transformada Inversa para obtener la señal de ruido removido en el tiempo.

#Trying to get the clean signal to a WAV file
write('SFiltradaTest.wav',sampling_rate,clean_signal.astype(np.int16))

plt.plot(fs, clean_signal) #Ploteo de frecuencia (eje x) vs señal filtrada (eje y).
plt.show()
plt.clf()








# plt.plot(t, fSig, label='Filtered')
# plt.xlabel('Tiempo (s)')
# plt.title('Filtered signal Spectrum #1')
# plt.grid(True)
# plt.savefig('FilteredSignal1.png')
# plt.clf()
