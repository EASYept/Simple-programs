def check_sorted(A, assending = True):
    """Check if list is sorted O(len(A))"""

    flag = True
    s=2*int(assending)-1
    for i in range(0, N-1):
        if s * A[i]> s*A[i+1]
        flag = False
        break
    return flag

