# 3
def frog(arr,ind):
    if ind == 0:
        return 0
    left = frog(arr,ind-1)+ abs(arr[ind-1]-arr[ind])
    right= float('inf')
    if ind>1:
        right = frog(arr,ind-2)+ abs(arr[ind-2]-arr[ind])
    return min(left,right)



def frogdp(arr,ind,dp):
    if ind == 0:
        return 0
    if dp[ind]!= -1:
        return dp[ind]
    left = frog(arr,ind-1)+ abs(arr[ind-1]-arr[ind])
    right= float('inf')
    if ind>1:
        right = frog(arr,ind-2)+ abs(arr[ind-2]-arr[ind])
    dp[ind] = min(left,right)
    return min(left,right)


def frogTab(arr):
    dp=[-1]*len(arr)
    dp[0]=0
    dp[1]=abs(arr[0]-arr[1])
    for i in range(2,len(arr)):
        dp[i]= min(dp[i-1]+abs(arr[i]-arr[i-1]),dp[i-2]+abs(arr[i]-arr[i-2]))
    return dp[len(arr)-1]

def frogopt(arr):
    prev= prev2 = 0
    for i in range(1,len(arr)):
        fs = prev+abs(arr[i]-arr[i-1])
        ss=float('inf')
        if i>1:
            ss= prev2+abs(arr[i]-arr[i-2])
        curr = min(fs,ss) 
        prev2= prev
        prev = curr
    return prev

def frogk(arr,k,ind):
    dp
    for i in range(1,len(arr)):
        minsteps = float('inf')
        for j in range(1,k+1):
            if i-j>= 0:
                jump = dp[i-j]+ abs(arr[ind]-arr[ind-j])
                minsteps = min(minsteps,jump)
        dp
arr = [10,20,30,10]
dp = [-1]*len(arr)

print(frogk([10,20,30,40],5,0))
print(frogopt([10,20,30,10]))
# print(frogTab(arr))
# print(frogdp(arr,len(arr)-1,dp))
# print(frog([10,20,30,10],3))