# python3
import numpy

# Discrete Knapsack problem without repetition
def partitions(W, n, items):
    count  = 0
    value = [[0]*(len(items)+1) for _ in range(W+1)]
    for i in range(1,W+1):
        for j in range(1,len(items)+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<= i:
                value[i][j] = max(value[i][j], value[i-items[j-1]][j-1]+items[j-1])
            if W==value[i][j]:
                count+=1
    if count<3:
        print('0')
    else:
        print('1')
        
partitions(7,6,[1,2,3,4,5,6])