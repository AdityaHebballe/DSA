from random import randint
import time

def MaxPairMine(lst):
    lst.sort() 
    max1 = max(lst)
    lst.remove(max1)
    if lst!=[]:
        max2 = max(lst)
        return max1*max2
    else:
        return max1*max1

def MaxPair(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product



if __name__ == '__main__':
    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    while(True):
        n = randint(1,15)
        rand_list=[]
        for i in range(n):
            rand_list.append(randint(0,1000))
    
        for i in range(n):
            print(rand_list[i])
            print(', ')
    
        result1 = MaxPair(rand_list)
        result2 = MaxPairMine(rand_list)
        if result1 != result2:
            print("Wrong Answer! ")
            print(f"{result1} != {result2}") 
            break;
        else:
            print("OK!")
    