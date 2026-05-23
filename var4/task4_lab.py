import numpy as np
import matplotlib.pyplot as plt

N = 200
noise_min, noise_max = -10, 2 
amplitudes = [6, 7, 3, 1] 
frequencies = [2, 8, 7, 5] 

t = np.linspace(0, 2 * np.pi, N)
signal = np.zeros(N)
for A, f in zip(amplitudes, frequencies):
    signal += A * np.sin(f * t)

noise = np.random.uniform(noise_min, noise_max, N)

mixed = signal + noise

def plot_spectrum(data, title, color, subplot_idx):
    spectrum = np.fft.fft(data)
    freq = np.fft.fftfreq(N, d=2*np.pi/N)
    
    plt.subplot(3, 2, subplot_idx)
    plt.plot(freq[:N//2], np.abs(spectrum)[:N//2], color)
    plt.title(title)
    plt.grid(True)
    plt.xlabel('Частота')
    plt.ylabel('|Спектр|')

plt.figure(figsize=(14, 10))

plt.subplot(3, 2, 1)
plt.plot(signal, 'g')
plt.title('Сигнал (временная область)')
plt.grid(True)

plot_spectrum(signal, 'Спектр сигнала', 'g', 2)

plt.subplot(3, 2, 3)
plt.plot(noise, 'r')
plt.title('Шум (временная область)')
plt.grid(True)

plot_spectrum(noise, 'Спектр шума', 'r', 4)

plt.subplot(3, 2, 5)
plt.plot(mixed, 'b')
plt.title('Аддитивная смесь (временная область)')
plt.grid(True)

plot_spectrum(mixed, 'Спектр смеси', 'b', 6)

plt.tight_layout()
plt.show()

spectrum_mixed = np.fft.fft(mixed)
reconstructed = np.fft.ifft(spectrum_mixed).real

plt.figure(figsize=(12, 4))
plt.plot(mixed, 'b', alpha=0.6, label='Оригинальная смесь')
plt.plot(reconstructed, 'r--', alpha=0.8, label='После обратного ПФ')
plt.title('Проверка обратного преобразования Фурье')
plt.legend()
plt.grid(True)
plt.show()

print(f"Максимальная ошибка восстановления: {np.max(np.abs(mixed - reconstructed)):.2e}")