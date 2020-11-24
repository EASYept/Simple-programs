MAX_VALUE = 4000000


def fib(max_value):
    nums = [1, 2]
    while nums[-1] < max_value:
        nums.append(nums[-1]+nums[-2])
    nums.pop(-1)
    return nums
print(fib(MAX_VALUE))
print(fib(MAX_VALUE)[1]%2)

SUM = 0
for i in fib(MAX_VALUE):
    if i % 2 == 0:
        SUM = SUM + i
print(SUM)




