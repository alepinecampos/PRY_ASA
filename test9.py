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


#Filtrado: 

# N = 100 # define N que es la longitud de lasmuestras que llega hasta N-1 si N = 100 len(N) llega a 99
# X = np.zeros(N, dtype = complex) #crea una matriz llena de 0 de tamaño N con capacidad para complejos
# realiza la transforamada de fourier  dando por resulrado una matriz de complejos *revisar la formula de la transformada para entender bien que pasa
# for k in range(N):
    # for n in range(N):
       #  X[k] = X[k] + x[n]*np.exp(-2j*np.pi*n*k/N)
# X/N #divide la sumatoria entre el numero de muestras


# plt.plot(np.absolute(X)) 


#t = np.arange(0,100) #no tienen interpretacion

#plt.plot(t/np.max(t),np.absolute(X)) # normaliza la señal 


#fmuestreo = 44100 #2 veces la frecuencia maxima mueatreada 
#plt.plot(fmuestreo*t[0:50]/np.max(t),np.absolute(X[0:50]))  # se plotea el arreglo despues que se multiplico la señal por el intervalo desde 0 hasta Fs


#z = np.zeros(25, dtype=complex) # se crea un arreglo con 0 de tamaño de lo que no quiero dejar pasar

#Z = np.concatenate((z,X[25:50])) # se concatena el arreglo de 0 con el resto de la señal que es mayor a la frecuencia que quiero 
#plt.plot(Z)

#f= np.concatenate((Z,X[50:76]))
#k= np.concatenate((f,z))
#plt.plot(k)


#iw = np.fft.ifft(k) # Se obtiene la transformada inversa de fourier para regresar al domminio del tiempo
#plt.plot(iw) # se plotea la señal


#S=np.zeros(N)
#for i in range (N):
 #   S[i] = x[i]

#plt.plot(S)

#plt.plot(S) # se plotean la original con la filtrada
#plt.plot(iw)

#J = np.concatenate((X[0:25],z)) # se concatena el arreglo de 0 con el resto de la señal que es mayor a la frecuencia de corte, que quiero 
#plt.plot(J)


#p= np.concatenate((J,z))
#l= np.concatenate((p,X[75:100]))
#plt.plot(l)

#iv = np.fft.ifft(l) # Se obtiene la transformada inversa de fourier para regresar al domminio del tiempo
#plt.plot(iv) # se plotea la señal

#plt.plot(S) # se plotean la original con la filtrada
#plt.plot(iv)





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
