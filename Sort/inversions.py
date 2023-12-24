def merge(left,right):
    final=list()
    i=j=inversion = 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            final.append(left[i])
            i+=1
        else:
            final.append(right[j])
            inversion+=len(left)-i
            j+=1
            
    final+=left[i:]
    final+=right[j:] 
    return final,inversion

    
def mergesort(arr):
    global tot_count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    tot_count += temp
    return sorted_arr

tot_count = 0
if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    mergesort(elements)
    print(tot_count)


