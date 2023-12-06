import random
from time import time
def RandomizedQuicksort(arr,left,right):
    if left<=1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x<pivot]
        equal = [x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
        return RandomizedQuicksort(left)+equal+RandomizedQuicksort(right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    RandomizedQuicksort(elements, 0, len(elements) - 1)
    print(*elements)

