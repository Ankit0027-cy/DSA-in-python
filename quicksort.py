def quicksort(arr):
    size= len(arr)
    if size<=1:
        return arr
    pivot=arr[size//2]
    items_greater=[]
    items_lower=[]
    for i in range(len(arr)):
            if arr[i]==pivot:
                continue
            if arr[i]>=pivot:
             items_greater.append(arr[i])
            else:
                items_lower.append(arr[i])
    return quicksort(items_lower)+[pivot]+quicksort(items_greater)

arr=([8,5,9,6,2,7,3,1,4])
quicksort(arr)
print(arr)