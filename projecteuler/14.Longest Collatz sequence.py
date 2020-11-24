"""import sys
x=2500
sys.setrecursionlimit(x)"""

def recur(n, count=0):
    if n == 0:
        return "Finished count %s" % count
    return recur(n-1, count+1)

counter = 0
def from_n_to_1(n, count=0):
    global counter
    if n == 1:
        return counter
    if (n % 2) == 0:
        n = n/2
        counter +=1
        return from_n_to_1(n)
    else:
        n = 3*n+1
        counter += 1
        return from_n_to_1(n)


print(from_n_to_1(27))
MAXIMUM = 0
for i in range(1, 10**6):
    a = from_n_to_1(i)
    if a > MAXIMUM:
        MAXIMUM = a
        print(MAXIMUM)
        print(i)
    counter = 0








