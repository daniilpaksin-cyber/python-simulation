import numpy as np
import matplotlib.pyplot as plt

ampl = 3
f0 = 10
min_limit_x = 0
max_limit_x = 1
N = 512              
fd = N / max_limit_x  

t = np.linspace(min_limit_x, max_limit_x, N)

mas_psp4 = [1, 7, 9, 2, 8, 6, 4, 5, 3, 1]

casual_signal = []
signal_prp4 = []

for i in t:
    tmp = int(i / 0.1)
    if tmp >= len(mas_psp4):
        tmp = len(mas_psp4) - 1 
    
    freq = mas_psp4[tmp]        
    
    casual_signal.append(ampl * np.sin(2 * np.pi * f0 * i))
    signal_prp4.append(ampl * np.sin(2 * np.pi * f0 * freq * i))

plt.figure(1)
plt.plot(t, signal_prp4, label='Сигнал с ППРЧ')
plt.plot(t, casual_signal, label='Обычный сигнал')
plt.grid(True)
plt.legend()
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.title('ППРЧ')

M = 2 * N               
f_range = np.zeros(2 * M)   

for smp_ref in range(-int(M), int(M)):
    f_range[smp_ref] = (smp_ref / (M * 2)) * fd

fft_result_casual = np.fft.fft(casual_signal, M * 2) / N
fft_result_prp4 = np.fft.fft(signal_prp4, M * 2) / N

mod_casual = np.abs(fft_result_casual)
mod_prp4 = np.abs(fft_result_prp4)

plt.figure(2)
plt.plot(f_range, mod_casual, label='Спектр обычного сигнала')
plt.plot(f_range, mod_prp4, label='Спектр сигнала с ППРЧ')
plt.grid(True)
plt.legend()
plt.xlabel('Частота')
plt.ylabel('Амплитуда')
plt.title('ППРЧ: спектры')
plt.xlim(-200, 200)

plt.show()