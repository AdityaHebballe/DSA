
def lcs3(A,B,C):
    m=len(A)
    n=len(B)
    o=len(C)
    dp = [[[-1]*(o+1) for i in range(n+1)]for j in range(m+1)]
    return find_lcs(A,B,C,dp,m,n,o)
def find_lcs(A,B,C,dp,m,n,o):
    if m==0 or n==0 or o==0:
         return 0
    if dp[m][n][o]!=-1:
        return dp[m][n][o]
    if A[m-1]==B[n-1]==C[o-1]:
        dp[m][n][o] = 1+ find_lcs(A,B,C,dp,m-1,n-1,o-1)
        return dp[m][n][o]
    else:
         dp[m][n][o] = max(find_lcs(A,B,C,dp,m-1,n,o),find_lcs(A,B,C,dp,m,n-1,o),find_lcs(A,B,C,dp,m,n,o-1))
         return dp[m][n][o]
            
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

