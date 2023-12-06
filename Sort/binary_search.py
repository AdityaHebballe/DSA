from math import floor
# def binary_search(keys, query):
#     l=0
#     h=len(keys)-1
#     while l<=h:
#         m = (l+h)//2
#         if keys[m]==query:
#             return m
#         elif query<keys[m]:
#             h=m-1
#         else:
#             l=m+1
#     return -1
def binary_search(keys,query,low,high):
    if high>=1:
        m=((high-1)+low)//2
        if keys[m]==query:
            return m
        elif keys[m]<query:
            binary_search(keys,query,low,m-1)
        else:
            binary_search(keys,query,m+1,high)
    else:
        return -1
# arr=[1,2,3,4,5]
# print(binary_search(arr,3,0,len(arr)))
if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
