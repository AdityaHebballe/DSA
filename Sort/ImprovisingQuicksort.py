from random import randint

def partition3(arr, l, r):
    m2 = l
    for i in range(l+1, r+1):
        if arr[i] <= arr[l]:
            arr[m2+1], arr[i] = arr[i], arr[m2+1]
            m2 += 1
    arr[l], arr[m2] = arr[m2], arr[l]
    m1 = l
    for i in range(l, m2):
        if arr[i] < arr[m2]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
    return m1, m2

def randomized_quick_sort(array, low, high):
    if low+1>=high:
        return
    m = randint(low, high-1)
    array[low], array[m] = array[m], array[low]
    m1,m2=partition3(array, low, high)
    randomized_quick_sort(array,low,m1)
    randomized_quick_sort(array,m2,high)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
# arr = [4,2,7,1,9,5,3,3,5,7]
# randomized_quick_sort(arr, 0, len(arr) - 1)
# print(arr)