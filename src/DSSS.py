import numpy as np
import matplotlib.pyplot as plt

# Параметры
ampl = 1
f0 = 1000                # несущая частота (Гц)
T = 1                    # длительность (сек)
N = 1024                 # количество отсчётов
fs = N / T               # частота дискретизации

# Код Баркера (длина 11)
barker = [1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1]
len_barker = len(barker)

# Информационные биты
bits = [1, -1, 1]
len_bits = len(bits)

# Длительность одного символа кода Баркера
period_barker = T / (len_bits * len_barker)
samples_per_barker = int(fs * period_barker)

# Время для одного символа Баркера
t_barker = np.linspace(0, period_barker, samples_per_barker)

# 1. Формируем расширенный сигнал (биты × код Баркера)
extended_signal = []
for bit in bits:
    for symbol in barker:
        value = bit * symbol
        extended_signal.extend([value] * samples_per_barker)

# 2. Временная ось
t_total = np.linspace(0, T, len(extended_signal))

# 3. НАЛОЖЕНИЕ НА СИНУСОИДУ (частотная манипуляция)
#    значение +1 → частота f_high, значение -1 → частота f_low
# 3. НАЛОЖЕНИЕ НА СИНУСОИДУ (непрерывная фаза, без скачков)
f_high = f0 + 200
f_low = f0 - 200
dt = 1 / fs

rf_signal = []
phase = 0

for i, value in enumerate(extended_signal):
    if value > 0:
        f_current = f_high
    else:
        f_current = f_low
    
    rf_signal.append(ampl * np.sin(2 * np.pi * f_current * t_total[i] + phase))
    
    # Сохраняем фазу для плавного перехода
    phase += 2 * np.pi * f_current * dt
    phase = phase % (2 * np.pi)

rf_signal = np.array(rf_signal)

# 4. СПЕКТР РАСШИРЕННОГО СИГНАЛА (только положительные частоты)
M_ext = 2 * len(extended_signal)
fft_ext = np.fft.fft(extended_signal, M_ext) / len(extended_signal)
freq_ext = np.fft.fftfreq(M_ext, 1/fs)

half_ext = M_ext // 2
freq_ext_pos = freq_ext[:half_ext]
spectrum_ext = 2 * np.abs(fft_ext[:half_ext])
spectrum_ext[0] /= 2
if M_ext % 2 == 0:
    spectrum_ext[-1] /= 2

# 5. СПЕКТР ВЧ СИГНАЛА (только положительные частоты)
M_rf = 2 * len(rf_signal)
fft_rf = np.fft.fft(rf_signal, M_rf) / len(rf_signal)
freq_rf = np.fft.fftfreq(M_rf, 1/fs)

half_rf = M_rf // 2
freq_rf_pos = freq_rf[:half_rf]
spectrum_rf = 2 * np.abs(fft_rf[:half_rf])
spectrum_rf[0] /= 2
if M_rf % 2 == 0:
    spectrum_rf[-1] /= 2

# ========== ГРАФИКИ ==========

# График 1: Код Баркера
plt.figure(figsize=(12, 3))
plt.step(t_total[:len(barker)*samples_per_barker], 
         extended_signal[:len(barker)*samples_per_barker], where='post')
plt.title('Код Баркера (11 символов: +1,+1,+1,-1,-1,-1,+1,-1,-1,+1,-1)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.ylabel('Амплитуда')

# График 2: Расширенный сигнал (биты × код Баркера)
plt.figure(figsize=(12, 3))
plt.step(t_total, extended_signal, where='post')
plt.title('Информационные биты [1, -1, 1], расширенные кодом Баркера')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.ylabel('Амплитуда')
plt.xlabel('Время, с')

# График 3: Спектр расширенного сигнала (положительные частоты)
plt.figure(figsize=(12, 4))
plt.plot(freq_ext_pos, spectrum_ext)
plt.title('Спектр расширенного сигнала (DSSS, до ВЧ)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.xlim(0, 500)

# График 4: ВЧ сигнал (синусоида с частотной манипуляцией)
plt.figure(figsize=(12, 3))
plt.plot(t_total[:200], rf_signal[:200])
plt.title('ВЧ сигнал: частота скачет в такт с расширенным сигналом')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.grid(True)

# График 5: Спектр ВЧ сигнала (положительные частоты)
plt.figure(figsize=(12, 4))
plt.plot(freq_rf_pos, spectrum_rf)
plt.title('Спектр ВЧ сигнала (после DSSS + FSK)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.xlim(0, 1000)

plt.tight_layout()
plt.show()