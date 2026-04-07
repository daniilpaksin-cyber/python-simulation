import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq

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
spectrum_mixture = fft(mixture)

signal_restored = ifft(spectrum_signal)

mixture_restored = ifft(spectrum_mixture)

signal_restored = np.real(signal_restored)
mixture_restored = np.real(mixture_restored)

plt.figure(1)
plt.plot(t, signal, 'b-', linewidth=1.5, label='Исходный сигнал')
plt.plot(t, signal_restored, 'r--', linewidth=1, label='Восстановленный сигнал')
plt.title('Сравнение исходного и восстановленного сигнала')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)

plt.figure(2)
plt.plot(t, mixture, 'b-', linewidth=1, label='Исходная смесь')
plt.plot(t, mixture_restored, 'r--', linewidth=1, label='Восстановленная (обратное FFT)')
plt.title('Сравнение исходной и восстановленной аддитивной смеси')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)

plt.figure(3)
error_signal = np.abs(signal - signal_restored)
error_mixture = np.abs(mixture - mixture_restored)
plt.plot(t, error_signal, 'b-', label='Ошибка для сигнала', linewidth=1)
plt.plot(t, error_mixture, 'r-', label='Ошибка для смеси', linewidth=1)
plt.title('Ошибка восстановления')
plt.xlabel('Время')
plt.ylabel('Абсолютная ошибка')
plt.legend()
plt.grid(True)

plt.show()