import time
from numpy.random import randint
from MergeSort import merge_sort
import matplotlib.pyplot as plt

def getRunTime(n):
    data = randint(0,n,n)
    start = time.time()
    merge_sort(data, 0, len(data) -1)
    end = time.time()

    return end-start

def benchmarkMergeSort():
    x =[]
    y =[]
    
    i = 0
    while i <= 50000:
        i+= 500
        x.append(i)
        y.append(getRunTime(i))

    plt.title("Benchmark Merge Sort")
    plt.xlabel("No. of elements")
    plt.ylabel("Time taken in seconds")
    plt.plot(x,y)
    plt.show()
benchmarkMergeSort()
