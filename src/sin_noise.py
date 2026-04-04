import numpy as np
import matplotlib.pyplot as plt

N = 500
t_min = 0
t_max = 6.28

noise_mean = 2
noise_sigma = 2

amplitudes = [1, 2, 1, 7]
frequences = [0.5, 0.4, 1, 2]

t = np.linspace(t_min, t_max, N)
signal = np.zeros(N)

for i in range(len(amplitudes)):
    signal = signal + amplitudes[i] * np.sin(2*np.pi*frequences[i]*t)

noise = np.random.normal(noise_mean, noise_sigma, N)
mixture = signal + noise

plt.figure(1)
plt.plot(t, signal)
plt.title('Signal')

plt.figure(2)
plt.plot(t, noise)
plt.title('Noise')

plt.figure(3)
plt.plot(t, mixture)
plt.title('Mixture')

plt.show()