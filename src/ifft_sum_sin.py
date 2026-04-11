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

filtered_fft = fft_signal_noise * ach

filtered_signal = np.fft.ifft(filtered_fft).real

aampl = np.abs(fft_signal_noise) / N
filtered_aampl = np.abs(filtered_fft) / N

freq_one = freq[:N//2]
spectrum_before = 2 * aampl[:N//2]
spectrum_before[0] = spectrum_before[0] / 2
spectrum_after = 2 * filtered_aampl[:N//2]
spectrum_after[0] = spectrum_after[0] / 2
if N % 2 == 0:
    spectrum_before[-1] = spectrum_before[-1] / 2
    spectrum_after[-1] = spectrum_after[-1] / 2

plt.figure(1)
plt.plot(t, signal_noise)
plt.title('Сигнал + шум (время)')

plt.figure(2)
plt.plot(freq_one, spectrum_before)
plt.title('Спектр до фильтрации')

plt.figure(3)
plt.plot(freq_one, spectrum_after)
plt.title('Спектр после фильтрации')

plt.figure(4)
plt.plot(t, filtered_signal)
plt.title('Сигнал после фильтрации')

plt.show()
