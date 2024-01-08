# def perms(arr,ds,ind,freq,ans):
#     if len(ds)==len(arr):
#         ans.append(ds.copy())
#         return
#     for i in range(ind,len(arr)):
#         if not freq[i]:
#             freq[i] = True
#             ds.append(arr[i])
#             perms(arr,ds,ind,freq,ans)
#             ds.pop()
#             freq[i] = False
#     return ans


def perms(arr,ind,ans):
    if ind == len(arr):
        ans.append(arr.copy())
        return
    for i in range(ind,len(arr)):
        arr[i],arr[ind] = arr[ind],arr[i]
        perms(arr,ind+1,ans)
        arr[i],arr[ind] = arr[ind],arr[i]
    return ans

print(perms([1,2,3],0,[]) )
# print(perms([1,2,3],[],0,[None,None,None],[]))