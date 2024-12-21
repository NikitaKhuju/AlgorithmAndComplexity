import time
import matplotlib.pyplot as plt
from BinarySearch import BinarySearch

input_sizes = [1000, 5000, 10000,20000,30000,40000, 50000,70000,80000,90000, 100000]
execution_times = []

for size in input_sizes:
    array = list(range(1, size + 1))
    target = size  # Target is the last element
    start_time = time.time()
    BinarySearch(array, target)
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b', label="Binary Search")
plt.title("Benchmarking Binary Search")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
