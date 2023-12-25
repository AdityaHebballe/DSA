def edit_distance(A,B):
    if not A or not B:
        return 0
    return min(edit_distance(A,B[:-1])+1,edit_distance(A[:-1])+1,edit_distance(A[:-1],B[:-1])+1)

edit_distance(['a','b','c'],['a','b','c','d'])