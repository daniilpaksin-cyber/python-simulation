import numpy as np
import matplotlib.pyplot as plt

ampl = 1
f0 = 20
N = 1024
T = 1
t_min = 0
fs = N / T

mas_manip = [1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1]
period = T / len(mas_manip)
sample_per = int(fs * period)

#AM-signal
bit_list = []
for bit in mas_manip:
    bit_list.extend([bit] * sample_per)
    
t_bit = np.linspace(0, period, sample_per)

AM_signal = []

for i in range(len(mas_manip)):
    if mas_manip[i] == 1:
        sin_wave1 = ampl * np.sin(2 * np.pi * f0 * t_bit)
        AM_signal.extend(sin_wave1)
    else:
        AM_signal.extend([0] * sample_per)

t1 = np.linspace(t_min, T, len(AM_signal))

#PM-signal
PM_signal = []
for i in range(len(mas_manip)):
    if mas_manip[i] == 1:
        sin_wave2 = ampl * np.sin(2 * np.pi * f0 * t_bit)
        PM_signal.extend(sin_wave2)
    else:
        sin_wave2 = ampl * np.sin(2 * np.pi * f0 * t_bit + np.pi)
        PM_signal.extend(sin_wave2)

#FM-signal
FM_signal = []
for i in range(len(mas_manip)):
    if mas_manip[i] == 1:
        sin_wave3 = ampl * np.sin(2 * np.pi * 4 * f0 * t_bit)
        FM_signal.extend(sin_wave3)
    else:
        sin_wave3 = ampl * np.sin(2 * np.pi * f0 * t_bit)
        FM_signal.extend(sin_wave3)
        
#fft_AM
M = 2 * len(AM_signal)
fft_AM = np.fft.fft(AM_signal, M) / len(AM_signal)
freq_AM = np.fft.fftfreq(M, 1/fs)

half = M // 2
freq_AM_one = freq_AM[:half]
ampl_spectrum_AM = 2 * np.abs(fft_AM[:half])
ampl_spectrum_AM[0] = ampl_spectrum_AM[0] / 2
if M % 2 == 0:
    ampl_spectrum_AM[-1] = ampl_spectrum_AM[-1] / 2
    
#fft_PM
fft_PM = np.fft.fft(PM_signal, M) / len(PM_signal)
freq_PM = np.fft.fftfreq(M, 1/fs)

ampl_spectrum_PM = 2 * np.abs(fft_PM[:half])
ampl_spectrum_PM[0] = ampl_spectrum_PM[0] / 2
if M % 2 == 0:
    ampl_spectrum_PM[-1] = ampl_spectrum_PM[-1] / 2

#fft_FM
fft_FM = np.fft.fft(FM_signal, M) / len(FM_signal)
freq_FM = np.fft.fftfreq(M, 1/fs)

ampl_spectrum_FM = 2 * np.abs(fft_FM[:half])
ampl_spectrum_FM[0] = ampl_spectrum_FM[0] / 2
if M % 2 == 0:
    ampl_spectrum_FM[-1] = ampl_spectrum_FM[-1] / 2

#fft_plot
plt.figure(5)
plt.plot(freq_AM_one, ampl_spectrum_AM, 'g-', label = 'AM', alpha=0.7)
plt.plot(freq_AM_one, ampl_spectrum_PM, 'b-', label = 'PM', alpha=0.7)
plt.plot(freq_AM_one, ampl_spectrum_FM, 'r-', label = 'FM', alpha=0.7)
plt.legend()
plt.xlim(0, 200)

#AM-signal#FM-signal
plt.figure(1)
plt.plot(t1, AM_signal)
plt.figure(1)
plt.plot(t1, bit_list)

#PM-signal
plt.figure(2)
plt.plot(t1, PM_signal)
plt.figure(2)
plt.plot(t1, bit_list)

#FM-signal
plt.figure(3)
plt.plot(t1, FM_signal)
plt.figure(3)
plt.plot(t1, bit_list)


plt.show()
    
