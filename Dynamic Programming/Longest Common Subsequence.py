A = ['a', 'b', 'c']
B = ['b', 'c', 'd','e']

def LCS(A,B,i=0,j=0):
    if i>len(A)-1 or j>len(A)-1:
        return 0
    if A[i]==B[j]:
        return 1+LCS(A,B,i+1,j+1)
    else:
        return max(LCS(A,B,i+1,j),LCS(A,B,i,j+1)) 
print(LCS(A,B))
        