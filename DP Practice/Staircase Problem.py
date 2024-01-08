def stair(ind):
    if ind == 0:
        return 1
    if ind ==1:
        return 1
    left = stair(ind-1)
    right = stair(ind-2)
    
    return left + right

print(stair(5))