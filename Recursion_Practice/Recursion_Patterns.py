# 10
def subsum(arr,i,target,Result):
    if i==len(arr):
        if sum(Result)==target:
            print(Result)
            return
        else:
            return
    Result.append(arr[i])
    subsum(arr,i+1,target,Result)
    Result.pop()
    subsum(arr,i+1,target,Result)


# 11
def subsumAnyOne(arr,i,target,Result):
    if i==len(arr):
        if sum(Result)==target:
            print(Result)
            return True
        else:
            return False
    Result.append(arr[i])
    
    if subsumAnyOne(arr,i+1,target,Result)== True :
        return True
    Result.pop()
    if subsumAnyOne(arr,i+1,target,Result)== True :
        return True
    return False

def Count(arr,i,target,Result):
    if i==len(arr):
        if sum(Result)==target:
            print(Result)
            return 1
        else:
            return 0
    Result.append(arr[i])
    
    l = Count(arr,i+1,target,Result)
    Result.pop()
    r = Count(arr,i+1,target,Result)
    return l+r

arr=[1,2,3]
Result = []
# subsum(arr,0,3,Result)
# subsum2(arr,0,3,Result,0)
# subsumAnyOne(arr,0,3,Result)
print(Count(arr,0,3,Result))