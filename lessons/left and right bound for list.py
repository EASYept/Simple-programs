#https://www.youtube.com/watch?v=EdhN_gEDfUM&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=10
#def find_num_in_list()

def left_bound(A, key):
    """find left bound in list"""

    left=-1
    right=len(A)

    while (right-left) > 1:
        middle = (left+right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left


def right_bound(A, key):
    """find right bound in list"""

    left = -1
    right = len(A)

    while (right - left) > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right