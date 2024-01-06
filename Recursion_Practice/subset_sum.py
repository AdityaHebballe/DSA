# def subset_sum(arr,i,sum,ds):
#     if i == len(arr):
#         ds.append(sum)
#         return
#     subset_sum(arr,i+1,sum,ds)
#     subset_sum(arr,i+1,sum+arr[i],ds)
#     # subset_sum(arr,i+1,sum)
#     return ds
# sum_subset = subset_sum([3,1,2],0,0,[])
# sum_subset.sort()
# print(sum_subset)

def subset_sum2(arr,ind,ds,ans):
    ans.append(ds.copy())
    for i in range(ind,len(arr)):
        if i!=ind and arr[i]==arr[i-1]: continue
        ds.append(arr[i])
        subset_sum2(arr,i+1,ds,ans)
        ds.pop()
    return ans

        
subsum =subset_sum2([1,2,2,2,3,3],0,[],[])
subsum.sort()
print(subsum)