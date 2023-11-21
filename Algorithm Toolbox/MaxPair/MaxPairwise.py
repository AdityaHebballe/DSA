from random import randint
import time

def MaxPair(lst):
    start_time = time.time()
    lst.sort() 
    max1 = max(lst)
    lst.remove(max1)
    if lst!=[]:
        max2 = max(lst)
        return max1*max2
    else:
        return max1*max1


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    start_time = time.time()
    print(MaxPair(input_numbers))
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time} seconds")
