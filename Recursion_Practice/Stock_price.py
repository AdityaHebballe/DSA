# def maxProfit(self, prices):


def maxProfit(prices,i,ans):
    if i+1>=len(prices):
        return ans 
    for j in range(i+1,len(prices)):
        if prices[j]>prices[i]:
            current = prices[j]-prices[i]
            ans = max(ans,current)
        maxProfit(prices,i+1,ans)
    return ans

print(maxProfit([7,1,5,3,6,4],0,0))