A = [3,1,2]
Result=[]
def subsequences(A,i,Result):
    if i == len(A):
        print(Result)
        return
    Result.append(A[i])
    subsequences(A,i+1,Result)
    Result.pop()    
    subsequences(A,i+1,Result)
    
    
print(subsequences(A,0,Result))