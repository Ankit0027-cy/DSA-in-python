import random
def is_sorted(arr):
    sorted=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted=False
            return sorted
# arr=[1,2,4,6,7,9]
# is_sorted(arr)
# print(arr)
def monkey_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
        
    print(arr)
    
a=[5,2,1,3,4,6,8,7,9]
monkey_sort(a)