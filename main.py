import matplotlib.pyplot as plt
import numpy as np

M = 100
m = 10
G = 6.67 * 10 ** 3
T_Earth = 365
T_Moon = 235
r = 45
r1 = 12
t = 0
dt = 0.001

v_Earth = 2 * np.pi * r / T_Earth
v_Moon = 2 * np.pi * r / T_Moon

x0 = []
y0 = []
x = []
y = []

while t <= 10:
    t += dt
    x0_value = v_Earth * dt
    y0_value = v_Earth * dt
    x_value = v_Moon * dt
    y_value = v_Moon * dt

    R = np.sqrt((x_value - x0_value) ** 2 + (y_value - y0_value) ** 2)
    F = -G * m * M / R ** 2
    x0.append(x0)
    y0.append(y0)
    x.append(x)
    y.append(y)
    print(x0)

plt.title('Траектории')
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()
