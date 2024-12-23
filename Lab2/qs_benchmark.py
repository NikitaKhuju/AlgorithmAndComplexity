import time
from numpy.random import randint
import matplotlib.pyplot as plt
from Quicksort import quick_sort

def getRuntime(n):
    data = randint(0, n, n)
    start = time.time()
    quick_sort(data, 0, len(data) - 1)
    end = time.time()

    return end - start

def BenchmarkQuickSort():
    x_points = []
    y_points = []
    
    i = 0
    while i <= 50000:
        i += 500
        x_points.append(i)
        y_points.append(getRuntime(i))

    plt.title("Benchmark Quick Sort")
    plt.xlabel("No. of elements ")
    plt.ylabel("Time taken in seconds")
    plt.plot(x_points, y_points)
    plt.show()
BenchmarkQuickSort()
    