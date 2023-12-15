# def marge_sort(arr):
#     size=len(arr)
#     temp=[0]*size
#     merge_sort(arr,temp,0,size-1)

# def merge_sort(arr,temp,lower,upper):
#     if lower>= upper:
#         return
#     middle=(lower+upper) // 2
#     merge_sort(arr,temp,lower,middle)
#     merge_sort(arr,temp,middle+1,upper)
#     merge(arr,temp,lower,middle,upper)
    
# def merge(arr,temp,lower,middle,upper):
#     lower_start=lower
#     lower_stop=middle
    
#     upper_start=middle
#     upper_stop=upper
#     count=lower
    
#     while lower_start<=lower_stop and upper_start<=upper_stop:
#         if arr[lower_start]<arr[upper_start]:
#             temp[count]=arr[lower_start]
#             count += 1
#             lower_start +=1
#         else:
#             temp[count]=arr[upper_start]
#             count+=1
#             upper_start+=1
#     while lower_start<=lower_stop:
#         temp[count]= arr[lower_start]
#         # count +=1
#         lower_start +=1
#     while upper_start<=upper_stop:
#         arr[count]= arr[upper_start]
#         # count +=1
#         upper_start+=1
#     i=lower
        
#     while i<=upper:
#         arr[i]=temp[i]
#         i +=1
# array=[5,9,6,12,8,3,7,4,13]
# marge_sort(array)
# print(array)


#  next method try merge sort
# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left_half=arr[:mid]
#         right_half=arr[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         i=j=k=0
#         while i<len(left_half) and j<len(right_half):
#             if left_half[i]<right_half[j]:
#                 arr[k]=left_half[i]
#                 i+=1
#             else:
#                 arr[k]=right_half[j]
#                 j+=1
#                 k+=1
#         while i<len(left_half):
#             arr[k]=left_half[i]
#             i+=1
#             k+=1
#         while j<len(right_half):
#             arr[k]=right_half[j]
#             j+=1
#             k+=1
# def merge_sorted(arr):
#     if len(arr)==2:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     left=merge_sorted(left)
#     right=merge_sorted(right)
#     return merge_sorted(left,right)
# arr=[12,5,9,13,1,7,6,2,11,10,8]
# merge_sorted(arr)
# print(arr)
def merge_sort(arr):
    n=len(arr)
    if n>1:
        mid=n//2
        lefthalf=arr[:mid]
        righthalf=arr[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=k=j=0
        while i<len(lefthalf)and j<len(righthalf):
            if lefthalf[i]>righthalf[j]:
                arr[k]=righthalf[j]
                j+=1
            else:
                arr[k]=lefthalf[i]
                i+=1
            k+=1
        while i<len(lefthalf):
            arr[k]=lefthalf[i]
            k+=1
            i+=1
        while j<len(righthalf):
            arr[k]=righthalf[j]
            k+=1
            j+=1
            
arr=[12,6,9,13,4,8,5,7,1,2]
merge_sort(arr)
print(arr) 