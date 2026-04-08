import numpy as np
import matplotlib.pyplot as plt

A = 1
f0 = 20
T = 1
N = 256
fs = N / T

t = np.linspace(0, T, N)
signal = A * np.sin(2 * np.pi * f0 * t)

fft_result = np.fft.fft(signal)
freq = np.fft.fftfreq(N, 1/fs)

spectrum = np.abs(fft_result) / N

plt.figure()
plt.plot(t, signal)
plt.grid(True)

plt.figure()
plt.plot(freq, spectrum)
plt.grid(True)
plt.xlim(0, 50)  
plt.show()