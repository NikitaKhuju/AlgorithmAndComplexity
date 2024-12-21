def LinearSearch(array, target):
    for index, x in enumerate(array):
        if x == target:
            return index
    return -1
    
array = [10,20,30,40,50]
target = 40

if LinearSearch(array,target) == -1:
    print(target , "not found")
else:
    print(target , "found at ", LinearSearch(array,target))