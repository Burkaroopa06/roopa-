# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize, integrate

# 1. NumPy: Create an array and perform basic operations
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# Operations
arr_squared = np.square(arr)
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_std = np.std(arr)

print("Squared Array:", arr_squared)
print("Sum of Array:", arr_sum)
print("Mean of Array:", arr_mean)
print("Standard Deviation of Array:", arr_std)

# 2. Matplotlib: Plotting the array
plt.plot(arr, label='Original')
plt.plot(arr_squared, label='Squared')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('NumPy Array Operations')
plt.legend()
plt.show()

# 3. SciPy: Statistical functions and optimization
# Statistical functions
mean, variance = stats.norm.stats(loc=arr_mean, scale=arr_std, moments='mv')
print("Mean:", mean)
print("Variance:", variance)

# Optimization example: Find the minimum of a quadratic function
def quadratic(x):
    return x**2 + 2*x + 1

result = optimize.minimize(quadratic, 0)
print("Optimization Result:", result)

# Integration example: Integrate a simple function
def integrand(x):
    return x**2

integral_result, error = integrate.quad(integrand, 0, 1)
print("Integral Result:", integral_result)
print("Integration Error:", error)
