

def coinschange(amount):
    dp = [amount+1]*(amount+1)
    dp[0]= 0
    for a in range(1,amount+1):
       for c in [1,3,5]:
           if a-c>=0:
               dp[a] = min(dp[a],dp[a-c]+1)
    return dp[amount] if dp[amount] != amount+1 else -1

print(coinschange(7))

def coinschange(amount,count=0):
    