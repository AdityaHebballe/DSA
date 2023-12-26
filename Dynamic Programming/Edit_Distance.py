from time import time   
A = "kittennn"
B = "sitting"
m = len(A)
n = len(B)

def edit_distance_rec(A,B):
    if not A:
        return 0
    if not B:
        return 0
    if A[-1]==B[-1]:
        return min(edit_distance_rec(A,B[:-1])+1,  #Deletion
                   edit_distance_rec(A[:-1],B)+1,  #Insertion
                   edit_distance_rec(A[:-1],B[:-1]))    
    else:
        return 1+min(edit_distance_rec(A,B[:-1]),
                   edit_distance_rec(A[:-1],B),
                   edit_distance_rec(A[:-1],B[:-1]))


dp = [[-1] * (n + 1) for _ in range(m + 1)]
 
def edit_distance_dp(A, B, m, n, dp):
    if m == 0:
        return n
    if n == 0:
        return m

    if dp[m][n] != -1:
        return dp[m][n]

    if A[m - 1] == B[n - 1]:
        dp[m][n] = min(1 + edit_distance_dp(A, B, m, n - 1, dp),
                       1 + edit_distance_dp(A, B, m - 1, n, dp),
                       edit_distance_dp(A, B, m - 1, n - 1, dp))

    else:
        dp[m][n] =1+ min(edit_distance_dp(A, B, m, n - 1, dp),
                       edit_distance_dp(A, B, m - 1, n, dp),
                       edit_distance_dp(A, B, m - 1, n - 1, dp))
    return dp[m][n]

def find_edit_distance(A, B):
    m=len(A)
    n=len(B)
    dp = [[-1] * (n + 1) for _ in range(m + 1)]
    return edit_distance_dp(A, B, m, n, dp)

if __name__ == "__main__":
    print(find_edit_distance(input(), input()))

# starttimedp = time()
# result = edit_distance_dp(A, B, m, n, dp)
# print(result)
# print("Time taken dp: ",time()-starttimedp)
# endtimedp = time()

# starttimerec=time()
# print(edit_distance_rec(A, B))
# endttimerec=time()
# print("Time taken rec: ",endttimerec-starttimerec)



        

    
    