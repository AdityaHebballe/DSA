A,B=['a','b','c'],['a','b','c','d']
# def edit_distance_rec(A,B):
#     if not A:
#         return 0
#     if not B:
#         return 0
#     if A[-1]==B[-1]:
#         return min(edit_distance_rec(A,B[:-1])+1,  #Deletion
#                    edit_distance_rec(A[:-1],B)+1,  #Insertion
#                    edit_distance_rec(A[:-1],B[:-1]))    
#     else:
#         return min(edit_distance_rec(A,B[:-1])+1,
#                    edit_distance_rec(A[:-1],B)+1,
#                    edit_distance_rec(A[:-1],B[:-1])+1)
# print(edit_distance_rec())

m=len(A)
n=len(B)
dp = [[-1]*(m+1) for _ in range(n+1) ]

def edit_distance_dp(A,B,dp,m,n):
    if m==0 or n==0:
        return 0
    if dp[m-1][n-1]!=-1:
        return dp[m-1][n-1]
    if A[m - 1] == B[n - 1]:
        dp[m][n] = min(
            edit_distance_dp(A, B, dp, m, n - 1) + 1,  # Deletion
            edit_distance_dp(A, B, dp, m - 1, n) + 1,  # Insertion
            edit_distance_dp(A, B, dp, m - 1, n - 1),  # No operation
        )
    else:
        dp[m][n] = 1 + min(
            edit_distance_dp(A, B, dp, m, n - 1),      # Deletion
            edit_distance_dp(A, B, dp, m - 1, n),      # Insertion
            edit_distance_dp(A, B, dp, m - 1, n - 1),  # Substitution
        )

    return dp[m][n]

# Example usage:
print(edit_distance_dp(A,B,dp))
        

    
    