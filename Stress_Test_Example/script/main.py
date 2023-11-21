def MaxPair(lst):
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
    print(MaxPair(input_numbers))