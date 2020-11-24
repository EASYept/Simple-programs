def factorial(n):
    if n == 1:
        return 1
    a = factorial(n-1)
    return n*a


num = str(factorial(100))

FULL_SUM = 0
for i in num:
    i = int(i)
    FULL_SUM += i

print(FULL_SUM)