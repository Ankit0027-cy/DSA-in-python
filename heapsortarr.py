def max_heap(arr,n,parent_index):
    largest=parent_index
    left=2*parent_index+1
    right=2*parent_index+2
    
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest != parent_index:
        arr[largest],arr[parent_index]=arr[parent_index],arr[largest]
        max_heap(arr,n,largest)

def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1):
        max_heap(arr,n,1)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heap(arr,i,0)
arr=[10,45,23,1,67,2]
heapsort(arr)
print(arr)
 