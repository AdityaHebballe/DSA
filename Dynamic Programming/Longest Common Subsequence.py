from time import time
import random
#SMALL EXAMPLE
# A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# B = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# m = len(A)
# n = len(B)

# LARGE EXAMPLE
length_A = 50
length_B = 20
A = [random.randint(1, 1000) for _ in range(length_A)]
B = [random.randint(1, 1000) for _ in range(length_B)]
m = len(A)
n = len(B)

dp = [[-1]*(n+1) for _ in range(m+1)] 
def LCS(A,B,m,n,dp):
    if m == 0 or n == 0:
        return 0
    if(dp[m][n] != -1):
        return dp[m][n]
    if A[m-1] == B[n-1]:
        dp[m][n] = 1 + LCS(A, B, m-1, n-1, dp)
        return dp[m][n]
    else:
        dp[m][n] = max(LCS(A, B, m-1, n, dp), LCS(A, B, m, n-1, dp))
        return dp[m][n]

def LCS2(A,B,m,n): 
    if m == 0 or n == 0:
        return 0
    if A[m-1] == B[n-1]:
        return 1 + LCS2(A, B, m-1, n-1)
    else:
        return max(LCS2(A, B, m-1, n), LCS2(A, B, m, n-1))
#TESTING DP
starttime=time()
print(LCS(A, B, m, n, dp))
endtime=time()
print("Time taken dp: ",endtime-starttime)
# TESTING RECURSION
starttime1=time()
print(LCS2(A, B, m, n))
endtime1=time()
print("Time taken rec: ",endtime1-starttime1)