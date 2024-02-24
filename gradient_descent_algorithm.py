import numpy as np
import matplotlib.pyplot as plt

def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5

def z_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * y) * np.sin(5 * x)

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

c_vector = (0.6, 0.8, z_function(0.6, 0.5))

learning_rate = 0.0008

ax = plt.subplot(projection="3d", computed_zorder=False)

for _ in range(1000):

    if c_vector[0] - 0.3 <= 0.05 and c_vector[1] - 0.1 <= 0.05:
        plt.pause(10000)
    else:
        ax.set_title("Gradient Descent Algorithm Visualised")
        ax.set_xlabel("x"), ax.set_ylabel("y"), ax.set_zlabel("z")
        X_derivative, Y_derivative = z_gradient(c_vector[0], c_vector[1])
        X_update, Y_update = c_vector[0] - learning_rate * X_derivative, c_vector[1] - learning_rate * Y_derivative
        c_vector = (X_update, Y_update, z_function(X_update, Y_update))
        ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)
        ax.scatter(c_vector[0], c_vector[1], c_vector[2], color="#ff1947", zorder=1)
        plt.pause(0.001)
        ax.clear()
    