import random
def RandomizedQuicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x<pivot]
        equal = [x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
        return RandomizedQuicksort(left)+equal+RandomizedQuicksort(right)

print(RandomizedQuicksort([2,5,7,7,4,2,4]))