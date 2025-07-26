import matplotlib.pyplot as plt
import numpy as np

for i in range(50):
    plt.plot(np.random.randn(100),linewidth = 1)
plt.title("Too much Data can be confusing")
plt.grid(True)
plt.tight_layout()
plt.show()