from math import floor
def binary_search(keys, query):
    l=0
    h=len(keys)-1
    while l<=h:
        m = (l+h)//2
        if keys[m]==query:
            return m
        elif query<keys[m]:
            h=m-1
        else:
            l=m+1
    return -1

    

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
