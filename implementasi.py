import numpy as np
import time

def f(x):
    return 4 / (1 + x**2)

def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    total_area = 0
    for i in range(N):
        x = a + i * dx
        total_area += f(x) * dx
    return total_area

# Testing the function with various values of N
N_values = [10, 100, 1000, 10000]
true_pi = 3.14159265358979323846
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integral(f, 0, 1, N)
    end_time = time.time()
    
    error = pi_approx - true_pi
    rms_error = np.sqrt(error**2)
    execution_time = end_time - start_time
    
    results.append((N, pi_approx, rms_error, execution_time))

# Display the results
for result in results:
    N, pi_approx, rms_error, execution_time = result
    print(f"N={N}: Pi Approximation={pi_approx}, RMS Error={rms_error}, Execution Time={execution_time:.6f} seconds")
