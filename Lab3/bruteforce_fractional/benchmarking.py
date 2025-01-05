import time
import matplotlib.pyplot as plt
from main import bruteforce_fractional_knapsack
import random

input_sizes = [5,10,15,20,25]
execution_times = []

for n in input_sizes:
    p = [random.randint(1,50) for _ in range(n)]
    w = [random.randint(1,25) for _ in range(n)]
    m = random.randint(25,100)

    start_time = time.time()
    bruteforce_fractional_knapsack(p,w,m)
    end_time = time.time()

    execution_times.append(end_time - start_time)
    print(f"Completed n={n} in {end_time - start_time:.2f} seconds")


plt.figure(figsize=(8,5))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color = 'b', label="Brute Force 0/1 Knapsack")
plt.title("Benchmarking Brute Force fractional Knapsack")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()