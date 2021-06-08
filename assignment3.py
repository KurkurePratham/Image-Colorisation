import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = (pd.read_csv('User_Data')).to_numpy()
# scaling
diff_x2 = max(dataset[0:, 2]) - min(dataset[0:, 2])
mean_x2 = np.mean(dataset[0:, 2])
diff_x3 = max(dataset[0:, 3]) - min(dataset[0:, 3])
mean_x3 = np.mean(dataset[0:, 3])
scaled_x1 = [(i - mean_x2) / diff_x2 for i in dataset[0:, 2]]
scaled_x2 = [(i - mean_x3) / diff_x3 for i in dataset[0:, 3]]
y = dataset[0:, 4]
theta0 = 2.0
theta1 = 2.0
theta2 = 2.0
alpha = 1.0
epsilon = 0.01

def hypothesis(i):
    return 1.0/(1 + math.exp(-theta0 - theta1 * scaled_x1[i] - theta2 * scaled_x2[i]))

def dhypothesis(i):
    return math.exp(-theta0 - theta1 * scaled_x1[i] - theta2 * scaled_x2[i]) * hypothesis(i) ** 2


while True:
    grad0 = 0.0
    grad1 = 0.0
    grad2 = 0.0
    for i in range(400):
        h = hypothesis(i)
        dh = dhypothesis(i)
        grad0 += (y[i] * math.log(h) + (1.0 - y[i]) * math.log(1.0 - h)) * (y[i]*dh*1.0/h - (1.0 - y[i])*dh/(1.0 - h))
        grad1 += (y[i] * math.log(h) + (1 - y[i]) * math.log(1 - h)) * (y[i]*dh*scaled_x1[i]/h - (1 - y[i])*dh*scaled_x1[i]/(1-h))
        grad2 += (y[i] * math.log(h) + (1 - y[i]) * math.log(1 - h)) * (y[i]*dh*scaled_x2[i] / h - (1 - y[i])*dh*scaled_x2[i]/(1-h))
    theta0 -= grad0 * alpha / 400
    theta1 -= grad1 * alpha / 400
    theta2 -= grad2 * alpha / 400
    print(grad0, theta0, grad1, theta1, grad2, theta2)
    if abs(grad0) < epsilon and abs(grad1) < epsilon and abs(grad2) < epsilon:
        break
print(theta0, theta1, theta2)

for i in range(400):
    if y[i] == 1:
        plt.scatter(scaled_x1[i], scaled_x2[i], c='red', s=6)
    else:
        plt.scatter(scaled_x1[i], scaled_x2[i], c='blue', s=6)
x = np.arange(-0.6, 0.7, 0.01)
y = (-theta0 - theta1 * x) / theta2
plt.plot(x, y)
plt.show()
