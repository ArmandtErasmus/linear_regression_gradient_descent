# Some Usefull Libraries
import numpy as np
import matplotlib.pyplot as plt

# Hardcoding a Cost Function
def cost_function(w, b, data):
    total_error = 0
    for point in range(len(data)):
        x = data[point][0]
        y = data[point][1]
        total_error += (y - (w * x + b)) ** 2
    total_error / float(len(data))

# Gradient Descent Algorithm
def gradient_descent(w, b, data, lr):
    w_grad = 0
    b_grad = 0

    n = len(data)

    for point in range(n):
        x = data[point][0]
        y = data[point][1]

        w_grad += -(1 / n) * (y - (w * x + b)) * x
        b_grad += -(1 / n) * (y - (w * x + b))

    weight = w - w_grad * lr
    bias = b - b_grad * lr
    return weight, bias

# Example Case

data = [[5, 90], [10, 140], [15, 250], [20, 300], [30, 380]]

w = 0
b = 0
lr = 0.002
epochs = 100000

for epoch in range(epochs):
    w, b = gradient_descent(w, b, data, lr)
print(w, b)

# Plot Result
plt.style.use('seaborn-v0_8')
plt.scatter([data[i][0] for i in range(len(data))], [data[i][1] for i in range(len(data))], color = "#8f8f8f")
plt.plot(list(range(0, 35)), [w * x + b for x in range(0, 35)], color = "#fc3858")
plt.title("Relationship Between the Maintenance Cost (USD) and the Age of an Appliance (Months)")
plt.xlabel("Age (months)")
plt.ylabel("Cost ($)")
plt.show()