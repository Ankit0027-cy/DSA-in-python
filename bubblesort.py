def bubble_sort(arr):
    size=len(arr)
    swapped=1
    
    for i in range(size-1):
        swapped=0
        for j in range(size-1-1):
            if (arr[j])> arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped +=1
        if swapped== 0:
            break
array=[1,4,7,2,5,8,3,6]
bubble_sort(array)
print(array)