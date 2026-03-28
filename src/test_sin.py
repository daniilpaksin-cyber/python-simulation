import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4*np.pi, 100)
y = 2 * np.sin(x)
plt.figure(1)
plt.plot(x, y)
plt.grid(True)
plt.title('2*Sin(x)')
plt.xlabel('radian')
plt.ylabel('sin(x)')
plt.show()