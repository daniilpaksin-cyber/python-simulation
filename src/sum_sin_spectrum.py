import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T = 0.5
N = int(T * fs)
f0 = [6, 40]
ampl = [2, 1]
sigma = 0.5


t = np.linspace(0, T, N)

signal = np.zeros(N)
for i in range(len(f0)):
    signal += ampl[i] * np.sin(2 * np.pi * f0[i] * t)
    
noise = np.random.normal(0, sigma, N)
signal_noise = noise + signal

ach = np.zeros(N)
index_40 = int(40 * N / fs)
ach[index_40] = 1
ach[N - index_40] = 1
    
fft_signal_noise = np.fft.fft(signal_noise)
freq = np.fft.fftfreq(N, 1/fs)
fft_ampl = np.abs(fft_signal_noise) / N

freq_one = freq[:N//2]
spectrum_freq = 2 * fft_ampl[:N//2]
spectrum_freq[0] = spectrum_freq[0] / 2
if N % 2 == 0:
    spectrum_freq[-1] = spectrum_freq[-1] / 2
    
fft_ach = ach * fft_signal_noise

plt.figure(1)
plt.plot(t, noise)

plt.figure(2)
plt.plot(t, signal)

plt.figure(3)
plt.plot(t, signal_noise)

plt.figure(4)
plt.plot(freq_one, spectrum_freq)
plt.xlim(0, 50)

plt.figure(5)
plt.plot(freq_one, fft_ach)
plt.xlim(0, 50)

plt.show()
