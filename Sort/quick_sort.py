arr=[2,5,4,1,7]

def partition(arr,l,h):
    pivot = arr[l]
    i=l+1
    j=h
    while True:
        while arr[i]<=pivot and i<=j:
            i+=1
        while arr[j]>=pivot and i<=j:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[l],arr[j]=arr[j],arr[l]
    return j
def QuickSort(arr,l,h):
    if l<h:
        pivot = partition(arr,l,h)
        QuickSort(arr,l,pivot-1)
        QuickSort(arr,pivot+1,h)
QuickSort(arr,0,4)
print(arr)
