def BinarySearch(array, target):
    low = 0
    high = len(array)-1

    while low <=high:
        mid = low + (high-low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid-1
    return -1

array = [10,20,30,40,50]
target = 40

if BinarySearch(array,target) == -1:
    print(target , "not found")
else:
    print(target , "found at ", BinarySearch(array,target))