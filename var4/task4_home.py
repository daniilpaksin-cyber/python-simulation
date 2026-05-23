import numpy as np
import matplotlib.pyplot as plt

N = 200
noise_min, noise_max = -10, -2
amplitudes = [6, 7, 3, 1]
frequencies = [1, 2, 8, 7]

t = np.linspace(0, 2 * np.pi, N)
signal = np.zeros(N)
for A, f in zip(amplitudes, frequencies):
    signal += A * np.sin(f * t)

noise = np.random.uniform(noise_min, noise_max, N)

mixed = signal + noise

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(signal, 'g')
plt.title(f'Сигнал (сумма {len(amplitudes)} синусоид)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(noise, 'r')
plt.title(f'Равномерный шум [{noise_min}, {noise_max}]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(mixed, 'b')
plt.title('Аддитивная смесь сигнала и шума')
plt.grid(True)

plt.tight_layout()
plt.show()