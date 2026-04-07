import numpy as np
import matplotlib.pyplot as plt

N = 500
t_min = 0
t_max = 10
t = np.linspace(t_min, t_max, N)

noise_mean = 2
noise_sigma = 2

amplitudes = [1, 2, 1, 7]
frequencies = [0.5, 0.4, 1, 2]

signal = np.zeros(N)
for i in range(len(amplitudes)):
    signal += amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t)

noise = np.random.normal(noise_mean, noise_sigma, N)

multiplicative_mixture = signal * noise

additive_mixture = signal + noise

plt.figure(1)
plt.plot(t, signal, 'b-', linewidth=1.5)
plt.title('Cумма 4 синусоид')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.figure(2)
plt.plot(t, noise, 'g-', linewidth=1)
plt.title('Шум'.format(noise_mean, noise_sigma))
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.figure(3)
plt.plot(t, multiplicative_mixture, 'r-', linewidth=1)
plt.title('Мультипликативная смесь')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.figure(4)
plt.plot(t, additive_mixture, 'm-', linewidth=1, label='Аддитивная смесь')
plt.plot(t, multiplicative_mixture, 'c-', linewidth=1, label='Мультипликативная смесь')
plt.title('Сравнение аддитивной и мультипликативной смесей')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)

plt.show()