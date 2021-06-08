import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = (pd.read_csv('cars.csv')).to_numpy()
# scaling
diff_x1 = max(dataset[0:, 2]) - min(dataset[0:, 2])
mean_x1 = np.mean(dataset[0:, 2])
diff_x2 = max(dataset[0:, 3]) - min(dataset[0:, 3])
mean_x2 = np.mean(dataset[0:, 3])
diff_y = max(dataset[0:, 4]) - min(dataset[0:, 4])
mean_y = np.mean(dataset[0:, 4])
scaled_x1 = [(i - mean_x1) / diff_x1 for i in dataset[0:, 2]]
scaled_x2 = [(i - mean_x2) / diff_x2 for i in dataset[0:, 3]]
scaled_y = [(i - mean_y) / diff_y for i in dataset[0:, 4]]

theta0 = 7
theta1 = 4
theta2 = 6
alpha = 0.5
epsilon = 0.00001
iterations = 0
while True:
    grad0 = 0.0
    grad1 = 0.0
    grad2 = 0.0
    for i in range(36):
        grad0 += (theta0 + theta1*scaled_x1[i] + theta2*scaled_x2[i] - scaled_y[i]) * 1
        grad1 += (theta0 + theta1*scaled_x1[i] + theta2*scaled_x2[i] - scaled_y[i]) * scaled_x1[i]
        grad2 += (theta0 + theta1*scaled_x1[i] + theta2*scaled_x2[i] - scaled_y[i]) * scaled_x2[i]
    theta0 -= grad0 * alpha / 36
    theta1 -= grad1 * alpha / 36
    theta2 -= grad2 * alpha / 36
    iterations += 1
    alpha *= 1.001
    print(grad0, theta0, grad1, theta1, grad2, theta2)
    if iterations > 10:
        plt.scatter(iterations, grad0 ** 2)
    if abs(grad0) < epsilon and abs(grad1) < epsilon and abs(grad2) < epsilon:
        break
print(theta0, theta1, theta2)
for i in range(36):
    print((theta0 + theta1*scaled_x1[i] + theta2*scaled_x2[i] - scaled_y[i])/scaled_y[i])
plt.show()
"""ax = plt.axes(projection="3d")
for i in range(36):
    ax.scatter3D(scaled_x1[i], scaled_x2[i], scaled_y[i])
i = np.arange(-0.5, 0.5, 0.01)
z = i + theta0
y = i * theta1
x = i * theta2
ax.plot3D(x, y, z)
plt.show()"""

