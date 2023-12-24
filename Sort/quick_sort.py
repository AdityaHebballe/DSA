from  random import randint
# def partition(arr,l,h):
#     pivot = arr[l]
#     i=l+1
#     j=h
#     while True:
#         while arr[i]<=pivot and i<=j:
#             i+=1
#         while arr[j]>=pivot and i<=j:
#             j-=1
#         if i<=j:
#             arr[i],arr[j]=arr[j],arr[i]
#         else:
#             break
#     arr[l],arr[j]=arr[j],arr[l]
#     return j

# def QuickSort(arr,l,h):
#     if l<h:
#         pivot=partition(arr,l,h)
#         QuickSort(arr,l,pivot-1)
#         QuickSort(arr,pivot+1,h)
def partition(arr,l,h):
    m=l
    
    k=randint(l,h)
    
    arr[k],arr[l]=arr[k],arr[l]
    
    for i in range(l+1,h+1):
        
        if arr[i]<arr[l]:
            
            m+=1
            arr[i],arr[m]=arr[m],arr[i]
            
    arr[l],arr[m]=arr[m],arr[l]
    return m
 
 
def quickSort(array, low, high):
    while low < high:
        pi = partition(array, low, high)
        if (pi-low)<(high-pi):
            quickSort(array, low, pi - 1)
            low=pi+1
        else:
            quickSort(array,pi+1,high)
            high=pi-1
    
 
arr = [4,2,7,1,9,5,3,5,23,12,345,3]
quickSort(arr, 0, len(arr) - 1)
print(arr)
        
# if __name__ == '__main__':
#     input_n = int(input())
#     elements = list(map(int, input().split()))
#     assert len(elements) == input_n
#     QuickSort(elements, 0, len(elements) - 1)
#     print(*elements)
