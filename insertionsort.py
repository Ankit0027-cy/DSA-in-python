def insertion_sort(arr):
    size=len(arr)
    i=1
    for i in range(1,size):
        temp=arr[i]
        j=i
        while j>0 and arr[j-1] >temp:
            arr[j]=arr[j-1]
            j-=1
            arr[j]=temp

array=[5,1,23,1,4,8,9,7,]
insertion_sort(array)
print(array)
            