from sys import stdin

def maximum_gold(capacity, weights):
    dp = [[-1]*(capacity+1) for _ in range(len(weights)+1)]
    for w in range(capacity+1):
        dp[0][w]=0
    for i in range(len(weights)+1):
        dp[i][0]=0
    for w in range(1,capacity+1):
        for i in range(1,len(weights)+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1]<=w:
                val = dp[i-1][w-weights[i-1]]+weights[i-1]
                dp[i][w]=max(val,dp[i][w])
    return dp[len(weights)][capacity]
            


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))