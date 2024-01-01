

# def coinschange(amount):
#     dp = [amount+1]*(amount+1)
#     dp[0]= 0
#     for a in range(1,amount+1):
#        for c in [1,3,5]:
#            if a-c>=0:
#                dp[a] = min(dp[a],dp[a-c]+1)
#     return dp[amount] if dp[amount] != amount+1 else -1



dp = [float('inf')] * (7 + 1)
dp[0] = 0
def coinschange(amount, dp):
    if dp[amount] != float('inf'):
        return dp[amount]

    if amount >= 1:
        dp[amount] = min(1 + coinschange(amount - 1, dp), dp[amount])
    if amount >= 3:
        dp[amount] = min(1 + coinschange(amount - 3, dp), dp[amount])

    if amount >= 5:
        dp[amount] = min(1 + coinschange(amount - 5, dp), dp[amount])

    return dp[amount]

# print(coinschange(3, dp))

