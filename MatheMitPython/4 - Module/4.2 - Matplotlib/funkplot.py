import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.linspace(0, 10, 500)
    y = x ** 2
    plt.plot(x, y, linewidth=2, linestyle='-', color='b')
    plt.show()