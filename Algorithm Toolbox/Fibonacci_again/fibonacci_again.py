def get_periods(n,m):
    prev = 0
    curr=1
    periods=0
    seq=[0,1]
    while True:
        prev,curr = curr,(prev+curr)%m
        periods+=1
        if prev==0 and curr==1:
            break
        seq.append(curr)
    seq.pop()
    return seq[(n%periods)]


if __name__ == '__main__':
    input_n ,input_m= map(int,input().split())
    print(get_periods(input_n,input_m))