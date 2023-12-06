def binary_search(keys, query):
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