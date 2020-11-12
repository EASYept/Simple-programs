
def tom_hoar(A):
    """Tom'PATH Hoare sorting
     one element as a barrier
     recurrent sorting
     """
    if len(A) <= 1:
        return
    barrier = A[0]
    L=[]
    M=[]
    R=[]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    k = 0
    tom_hoar(L) #recurent part
    tom_hoar(R) #recurent part
    for x in L+M+R:
        A[k]=x
        k+=1