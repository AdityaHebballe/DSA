from time import time
def merge(left,right):
    new=[]
    i,j=0,0
    
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new


def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    l_half=mergesort(arr[:mid])
    r_half=mergesort(arr[mid:])
    return merge(l_half,r_half)
before = time()
print(mergesort([8,3,7,4,9,2,6,5]))
after = time()
print(f"Time taken: {after-before} seconds")