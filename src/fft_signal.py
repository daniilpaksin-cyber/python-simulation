import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

N = 500                    
t_min = 0
t_max = 10
t = np.linspace(t_min, t_max, N)
dt = t[1] - t[0]        

noise_mean = 2
noise_sigma = 2

amplitudes = [1, 2, 1, 7]
frequencies = [0.5, 0.4, 1, 2]

signal = np.zeros(N)
for i in range(len(amplitudes)):
    signal += amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t)

noise = np.random.normal(noise_mean, noise_sigma, N)
mixture = signal + noise

spectrum_signal = fft(signal)
spectrum_noise = fft(noise)
spectrum_mixture = fft(mixture)

amp_signal = np.abs(spectrum_signal)
amp_noise = np.abs(spectrum_noise)
amp_mixture = np.abs(spectrum_mixture)

freq = fftfreq(N, dt)[:N//2]

amp_signal_pos = amp_signal[:N//2]
amp_noise_pos = amp_noise[:N//2]
amp_mixture_pos = amp_mixture[:N//2]

plt.figure(1)
plt.stem(freq, amp_signal_pos, basefmt=" ", markerfmt=" ", linefmt="b-")
plt.title('Амплитудный спектр сигнала (4 синусоиды)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.xlim(0, 3) 

plt.figure(2)
plt.plot(freq, amp_noise_pos, 'g-', linewidth=1)
plt.title('Амплитудный спектр шума (нормальное распределение)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.figure(3)
plt.plot(freq, amp_mixture_pos, 'r-', linewidth=1)
plt.title('Амплитудный спектр аддитивной смеси (сигнал + шум)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.figure(4)
plt.plot(freq, amp_signal_pos, 'b-', label='Сигнал', linewidth=1.5)
plt.plot(freq, amp_noise_pos, 'g-', label='Шум', linewidth=1, alpha=0.7)
plt.plot(freq, amp_mixture_pos, 'r-', label='Смесь', linewidth=1)
plt.title('Сравнение спектров')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)
plt.xlim(0, 3)

plt.show()