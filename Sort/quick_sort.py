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
def partition(array, low, high):
    pivot = array[high]

    j = low - 1
    for i in range(low, high):
        if array[i] <= pivot:
            j+=1
            (array[j], array[i]) = (array[i], array[j])
    (array[j + 1], array[high]) = (array[high], array[j + 1])
 
    return j + 1
 
 
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 
 
arr = [4,2,7,1,9,5,3]
quickSort(arr, 0, len(arr) - 1)
print(arr)
        
# if __name__ == '__main__':
#     input_n = int(input())
#     elements = list(map(int, input().split()))
#     assert len(elements) == input_n
#     QuickSort(elements, 0, len(elements) - 1)
#     print(*elements)
