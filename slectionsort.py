# def selection_sort(arr):
#     size=len(arr)
#     for i in range(size-1):
#         max=0
#         for j in range(1,size-i):
#             if arr[j]>arr[max]:
#                 max=j
#         temp=arr[size-1-i]
#         arr[size-1-i]=arr[max]
#         arr[max]=temp
# array=[3,1,25,6,4,9,4,5,45]
# selection_sort(array)
# print(array)
def selection_sort2(arr):
    size=len(arr)
    for i in range(size-1):
        max=i
        for j in range(i+1,size):
            if arr[j]<arr[max]:
                max=j
        temp=arr[i]
        arr[i]=arr[max]
        arr[max]=temp
array=[3,1,25,6,4,9,4,5,45]
selection_sort2(array)
print(array)
        