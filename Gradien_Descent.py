import math

# Define the Rosenbrock function
def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

# Define the gradient of the Rosenbrock function
def gradient(x, y):
    return [-2 * (1 - x) - 400 * x * (y - x ** 2), 200 * (y - x ** 2)]

# Define the learning rate
learning_rate = 0.001

# Initialize the starting point
x, y = 0, 0

# Perform gradient descent
for i in range(10000):
    grad = gradient(x, y)
    x -= learning_rate * grad[0]
    y -= learning_rate * grad[1]

# Print the final result
print("The minimum value of the Rosenbrock function is", rosenbrock(x, y), "at x =", x, "and y =", y)
