from thinkdsp import read_wave
import tkinter as tk
from tkinter import Label, ttk
from scipy.io.wavfile import write
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry('1300x700')
root.configure(background='#b3ccff')


SFiltrar=read_wave('outputRecording1.wav')
EspFiltrar= SFiltrar.make_spectrum()
EspFiltrar.low_pass(5000)#Cambiar segun filtro
SFiltrada= EspFiltrar.make_wave()
SFiltrada.normalize()
#Guardado y Mostrado de resultados
SFiltrada.plot(color='#66a3ff')
plt.xlabel('Tiempo (s)')
plt.title('Onda Filtrada')
plt.grid(True)
plt.savefig('Filtered_Wave.png')
plt.clf()
EspFiltrar.plot(color='#ff471a')
plt.xlabel('Frecuencia (Hz)')
plt.title('Espectro Filtrado')
plt.grid(True)
plt.savefig('Filtered_Spectrum.png')
plt.clf()
#FilteredWaveImage
wIn_Img=Image.open('Filtered_Wave.png')
wIn_Img = wIn_Img.resize((int((wIn_Img.width)-((wIn_Img.width)*0.5)),int((wIn_Img.height)-((wIn_Img.height)*0.5))), Image.ANTIALIAS)
render1=ImageTk.PhotoImage(wIn_Img)
wIn_Label = Label(root,image=render1)
wIn_Label.image = render1
wIn_Label.grid(row=1, column=5, sticky="nsew", padx=1, pady=1)
#FilteredSpectrumImage
sIn_Img=Image.open('Filtered_Spectrum.png')
sIn_Img = sIn_Img.resize((int((sIn_Img.width)-((sIn_Img.width)*0.5)),int((sIn_Img.height)-((sIn_Img.height)*0.5))), Image.ANTIALIAS)
render2=ImageTk.PhotoImage(sIn_Img)
sIn_Label = Label(root,image=render2)
sIn_Label.image=render2
sIn_Label.grid(row=1, column=6, sticky="nsew", padx=1, pady=1)