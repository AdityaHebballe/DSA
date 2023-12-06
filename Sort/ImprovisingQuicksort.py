from random import randint


def partition3(array, low,high):
    j = low
    pivot = array[low]
    for i in range(low+1,high+1):
        if array[i]<=pivot:
            j+=1
            array[i],array[j] = array[j],array[i]
    array[low],array[j] = array[j],array[low]
    return j

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m1 + 1, right)

arr = [4,2,7,1,9,5,3]
randomized_quick_sort(arr, 0, len(arr) - 1)
print(arr)
        
# if __name__ == '__main__':
#     input_n = int(input())
#     elements = list(map(int, input().split()))
#     assert len(elements) == input_n
#     randomized_quick_sort(elements, 0, len(elements) - 1)
#     print(*elements)
