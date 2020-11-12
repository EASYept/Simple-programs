#https://www.youtube.com/watch?v=m4HOkVeN4Mo&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=11
def greatest_increasing_subseuquence(A):
    F=[0]*(len(A)+1)
    for i in range(1, len(A)+1):
        m=0 #maximum
        for j in range(0, i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    print(F[len(A)])
    return F[len(A)]

lol = [0, 8, 4, 12, 2, 10, 6, 99, 1, 9, 5, 13, 3, 11, 7, 15]

greatest_increasing_subseuquence(lol)
