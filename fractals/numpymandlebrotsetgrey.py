import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x, y = np.ogrid[-2:1:500j, -1.5:1.5:500j]

# Increase this to improve the shape of the fractal
iterations = 9

c = x + 1j*y

z = reduce(lambda x, y: x**2 + c, [1] * iterations, c)

plt.figure(figsize=(10, 10))
plt.imshow(np.angle(z))

plt.figure(figsize=(10, 10))
