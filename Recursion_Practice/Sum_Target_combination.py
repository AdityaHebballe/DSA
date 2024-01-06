def combination_sum(arr,i,result,target,ans):
    if i==len(arr):
        if target==0:
            ans.add(result.copy())
            print(ans)
        return

    if target>=arr[i]:
        result.append(arr[i])
        combination_sum(arr,i,result,target-arr[i],ans)
        result.pop()
    if arr[i]==arr[i+1]:
        combination_sum(arr,i+2,result,target,ans)
    return ans

# ans = combination_sum([2,3,6,7],0,[],7,[])
# print(ans)

def combination_sum_no_rep(arr,ind,target,ds,ans):
    if target==0:
        ans.append(ds.copy())
        return
    for i in range(ind,len(arr)):
        if(i>ind and arr[i]==arr[i-1]): continue
        if(arr[i]>target): break
        ds.append(arr[i])
        combination_sum_no_rep(arr,i+1,target-arr[i],ds,ans)
        ds.pop()
    return ans
arr=[1,1,2,2,3,6,7]
arr.sort()
ans = combination_sum_no_rep(arr,0,7,[],[])
print(ans)

    