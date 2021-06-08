import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = (pd.read_csv('data1.csv')).to_numpy()
# scaling
diff_x = max(dataset[0:, 0]) - min(dataset[0:, 0])
mean_x = np.mean(dataset[0:, 0])
diff_y = max(dataset[0:, 1]) - min(dataset[0:, 1])
mean_y = np.mean(dataset[0:, 1])
scaled_x = [(i - mean_x) / diff_x for i in dataset[0:, 0]]
scaled_y = [(i - mean_y) / diff_y for i in dataset[0:, 1]]

theta0 = 0.3
theta1 = 0.6
alpha = 0.01
epsilon = 0.1
while True:
    grad0 = 0.0
    grad1 = 0.0
    for i in range(45):
        grad0 += (theta0 + theta1*scaled_x[i] - scaled_y[i])
        grad1 += (theta0 + theta1*scaled_x[i] - scaled_y[i])*scaled_x[i]
    theta0 -= grad0*alpha/45
    theta1 -= grad1*alpha/45
    print(grad0,theta0, grad1, theta1)
    if abs(grad0) < epsilon and abs(grad1) < epsilon:
        break
print(theta0, theta1)
for i in range(45):
    plt.scatter(scaled_x, scaled_y)
x = np.arange(-1, 1, 0.01)
y = theta0 + theta1*x
plt.plot(x, y)
plt.show()
