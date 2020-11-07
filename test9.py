import numpy as np
from scipy.io.wavfile import write
from thinkdsp import read_wave
import matplotlib.pyplot as plt
import winsound
from numpy import fft


sampling_rate = 46100

time = np.arange(0, 10, 1/sampling_rate)

# data = np.sin(2*np.pi*6*time) + np.random.randn(len(time))
data = read_wave('outputRecording1.wav').ys

fourier_transform = np.fft.rfft(data) #Fourier Transform
abs_fourier_transform = np.abs(fourier_transform) #Toma unicamente los positivos con valor abs. Se obtiene el espectro normal.
power_spectrum = np.square(abs_fourier_transform) #Eleva amplitudes del espectro normal al cuadrado para obtener el espectro de poder

frequency = np.linspace(0, sampling_rate/2, len(power_spectrum)) #Array para eje x del ploteo

#Starting separation/cleaning process
indices = power_spectrum > 2500 #2500 como valor de corte. Todas las amplitudes superiores a 2500 pasan intactas, el resto es seteado a cero.
indices2 = power_spectrum < 2500
power_spectrum_clean = power_spectrum * indices #Espectro de poder filtrado
abs_fourier_transform_clean = abs_fourier_transform * indices #Espectro de frecuencias (normal) filtrado.
noise_spectrum = abs_fourier_transform * indices2 #Espectro de frecuencias (normal) del ruido removido.
clean_signal = np.fft.ifft(abs_fourier_transform_clean) #Transformada Inversa para obtener la señal filtrada en el tiempo.
noise_signal = np.fft.ifft(noise_spectrum) #Transformada Inversa para obtener la señal de ruido removido en el tiempo.

#Trying to get the clean signal to a WAV file
write('SFiltradaTest.wav',sampling_rate,clean_signal)

plt.plot(frequency, noise_signal) #Ploteo de frecuencia (eje x) vs señal filtrada (eje y).
plt.show()






# WaveIn = read_wave('outputRecording1.wav')
# WaveIn.plot(color='#66a3ff')
# plt.xlabel('Tiempo (s)')
# plt.title('Onda #1')
# plt.grid(True)
# plt.savefig('Wave1.png')
# plt.clf()
# SpecIn = WaveIn.make_spectrum()
# SpecIn.plot(color='#ff471a')
# plt.xlabel('Frecuencia (Hz)')
# plt.title('Espectro #1')
# plt.grid(True)
# plt.savefig('Spectrum1.png')
# plt.clf()
# #----------------Testing Power Spectrum------------------
# plt.plot(SpecIn.fs,SpecIn.amps**2,color='#bd6ecf')
# plt.xlabel('Frecuencia (Hz)')
# plt.title('Power Spectrum #1')
# plt.grid(True)
# plt.savefig('PowSpectrum1.png')
# plt.clf()

# #--------------------------------------------------
# t = np.arange(0,46100,(1/46100))
# r = len(t)
# fhat = np.fft.fft(SpecIn.amps,r) #Complex values Fourier Coef
# PS = fhat * np.conj(fhat)/r #Power Spectrum
# freqs = (1/((1/46100)*r)) * np.arange(r)
# L = np.arange(1,np.floor(r/2),dtype='int')

# plt.plot(freqs[L],PS[L], label='Noisy')
# plt.xlabel('Frecuencia (Hz)')
# plt.title('Noisy Power Spectrum #1')
# plt.grid(True)
# plt.savefig('NoisyPowSpectrum1.png')
# plt.clf()
    
# indices = PS > 200000
# PSclean = PS * indices
# fhat = fhat * indices
# fSig = np.fft.ifft(fhat)

# plt.plot(freqs[L],PSclean[L], label='Filtered')
# plt.xlabel('Frecuencia (Hz)')
# plt.title('Filtered Power Spectrum #1')
# plt.grid(True)
# plt.savefig('FilteredPowSpectrum1.png')
# plt.clf()

# plt.plot(t, fSig, label='Filtered')
# plt.xlabel('Tiempo (s)')
# plt.title('Filtered signal Spectrum #1')
# plt.grid(True)
# plt.savefig('FilteredSignal1.png')
# plt.clf()
