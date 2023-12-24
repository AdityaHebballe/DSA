A = ['a', 'b', 'c']
B = ['a','b', 'c', 'd','e']

# def LCS(A,B,i=0,j=0):
#     if i>len(A)-1 or j>len(A)-1:
#         return 0
#     if A[i]==B[j]:
#         return 1+LCS(A,B,i+1,j+1)
#     else:
#         return max(LCS(A,B,i+1,j),LCS(A,B,i,j+1)) 
# print(LCS(A,B))

#USING DYNAMIC PROGRAMMING

i,j = len(A), len(B)
# Create a memoization table filled with -1
memo = [[-1] * (j + 1) for _ in range(i + 1)] 

def lcs_helper(i, j):
    if memo[i][j] != -1:
        return memo[i][j]

    if i == 0 or j == 0:
        result = 0
    elif A[i - 1] == B[j - 1]:
        result = 1 + lcs_helper(i - 1, j - 1)
    else:
        result = max(lcs_helper(i - 1, j), lcs_helper(i, j - 1))

    memo[i][j] = result
    return result
print(lcs_helper(i, j))