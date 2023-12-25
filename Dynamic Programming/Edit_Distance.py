def edit_distance(A,B):
    if not A:
        return 0
    if not B:
        return 0
    if A[-1]==B[-1]:
        return min(edit_distance(A,B[:-1])+1,  #Deletion
                   edit_distance(A[:-1],B)+1,  #Insertion
                   edit_distance(A[:-1],B[:-1]))    
    else:
        return min(edit_distance(A,B[:-1])+1,
                   edit_distance(A[:-1],B)+1,
                   edit_distance(A[:-1],B[:-1])+1)
print(edit_distance(['a','b','c'],['a','b','c','d']))